FROM vrusinov/golang-build:latest as build

RUN emerge -v dev-vcs/git

RUN mkdir /tmp/build
RUN cd /tmp/build && \
  git clone https://github.com/drakkan/sftpgo && \
  cd sftpgo && \
  git checkout v1.0.0 && \
  go build -i && \
  cp sftpgo /bin

FROM vrusinov/golang:latest
COPY --from=build /bin/sftpgo /bin/sftpgo

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/bin/sftpgo", "-v"]
