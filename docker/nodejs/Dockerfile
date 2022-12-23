FROM vrusinov/nodejs-build:18.12.1 as build

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:2022-12-18
COPY --from=build /usr/bin/node /usr/bin/node
COPY --from=build /usr/lib64/libbrotli* /lib64/
COPY --from=build /usr/lib64/libcares* /lib64/
COPY --from=build /usr/lib64/libuv* /lib64/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/node", "--version"]
