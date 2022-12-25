FROM vrusinov/python3-build:3.10.9 as build


FROM vrusinov/base:2022-12-25

COPY --from=build /etc/python-exec/python-exec.conf /etc/python-exec/
COPY --from=build /usr/bin/python3.10 /usr/bin/python3.10
COPY --from=build /usr/lib/python-exec/python3.10/ /usr/lib/python-exec/python3.10/
COPY --from=build /usr/lib/python3.10/ /usr/lib/python3.10/
COPY --from=build /usr/lib64/libpython3.10* /usr/lib64/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]
