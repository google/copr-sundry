FROM vrusinov/base-build:2021-09-11 as build

RUN emerge -v net-vpn/openvpn

FROM vrusinov/base:2021-09-11
COPY --from=build /etc/openvpn/down.sh /etc/openvpn/down.sh
COPY --from=build /etc/openvpn/up.sh /etc/openvpn/up.sh
COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /lib64/liblzo2* /lib64/
COPY --from=build /usr/sbin/openvpn /bin/openvpn

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

USER openvpn
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/openvpn", "--version"]