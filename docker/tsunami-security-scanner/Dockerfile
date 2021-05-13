FROM vrusinov/java-build:latest as build

# Install nmap
RUN emerge -v net-analyzer/nmap

# Install ncrack
RUN USE="-webdav curl" emerge -v dev-vcs/git
RUN emerge -v app-eselect/eselect-repository
RUN mkdir -p /etc/portage/repos.conf
RUN eselect repository enable pentoo
RUN emaint sync -r pentoo
RUN mkdir -p /etc/portage/package.accept_keywords/
COPY ncrack.accept_keywords /etc/portage/package.accept_keywords/ncrack
RUN emerge -v net-analyzer/ncrack

# Prep for tsunami install
RUN mkdir -p /opt/tsunami

# Build plugins
WORKDIR /tmp
RUN git clone --depth 1 "https://github.com/google/tsunami-security-scanner-plugins"
WORKDIR /tmp/tsunami-security-scanner-plugins/google
RUN chmod +x build_all.sh \
    && ./build_all.sh
RUN mkdir /opt/tsunami/plugins \
    && cp build/plugins/*.jar /opt/tsunami/plugins

# Compile the Tsunami scanner
WORKDIR /tmp
RUN wget https://github.com/google/tsunami-security-scanner/archive/refs/tags/v0.0.4.tar.gz
RUN tar xf v0.0.4.tar.gz
WORKDIR /tmp/tsunami-security-scanner-0.0.4/
RUN ./gradlew shadowJar \
    && cp $(find "./" -name 'tsunami-main-*-cli.jar') /opt/tsunami/tsunami.jar \
    && cp ./tsunami.yaml /opt/tsunami/

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh

FROM vrusinov/java as base

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh

COPY --from=build /opt/tsunami/ /opt/tsunami/
COPY --from=build /usr/bin/ncrack /usr/bin/
COPY --from=build /usr/bin/nmap /usr/bin/
COPY --from=build /usr/lib64/liblinear.so.4 /usr/lib64/
COPY --from=build /usr/lib64/libpcap* /usr/lib64/
COPY --from=build /usr/share/ncrack/ /usr/share/ncrack/
COPY --from=build /usr/share/nmap/ /usr/share/nmap/

COPY entrypoint.sh /bin/entrypoint.sh
ENV IP_V4_TARGET ""
ENV IP_V6_TARGET ""
ENTRYPOINT ["/bin/entrypoint.sh"]
