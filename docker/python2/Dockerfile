FROM vrusinov/python2-build:2.7.18 as build

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:2022-05-29
COPY --from=build /usr/bin/python2* /usr/bin/
COPY --from=build /usr/lib/python-exec/python2.7/ /usr/lib/python-exec/python2.7/
COPY --from=build /usr/lib64/python2.7/ /usr/lib64/python2.7/
COPY --from=build /usr/lib64/libpython2* /usr/lib64/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/python2", "--version"]
