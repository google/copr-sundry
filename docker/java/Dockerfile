FROM vrusinov/java-build:11.0.15_p10 as build

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

FROM vrusinov/base:2022-05-29
COPY --from=build /etc/java-config-2/ /etc/java-config-2/
COPY --from=build /opt/openjdk-bin-11.0.15_p10/ /opt/openjdk-bin-11.0.15_p10/
COPY --from=build /usr/bin/ /usr/bin/
COPY --from=build /usr/lib/jvm/ /usr/lib/jvm/
COPY --from=build /usr/libexec/eselect-java/ /usr/libexec/eselect-java/
COPY --from=build /usr/share/java-config-2/ /usr/share/java-config-2/

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/java", "-version"]
