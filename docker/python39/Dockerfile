FROM vrusinov/python3-build:3.9.2022-01-03 as build

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:2021-09-11

COPY --from=build /etc/python-exec/python-exec.conf /etc/python-exec/
COPY --from=build /usr/bin/python3.9 /usr/bin/python3.9
COPY --from=build /usr/lib/python-exec/python3.9/ /usr/lib/python-exec/python3.9/
COPY --from=build /usr/lib/python3.9/ /usr/lib/python3.9/
COPY --from=build /usr/lib64/libpython3.9* /usr/lib64/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]
