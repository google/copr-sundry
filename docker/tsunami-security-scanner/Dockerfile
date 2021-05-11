FROM vrusinov/java-build:latest as build

RUN USE="-webdav curl" emerge -v dev-vcs/git
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

# Example:
# cp /opt/tsunami
# java -cp tsunami.jar:plugins/* -Dtsunami-config.location=tsunami.yaml com.google.tsunami.main.cli.TsunamiCli --ip-v4-target=127.0.0.1
ENTRYPOINT ["/bin/bash"]
