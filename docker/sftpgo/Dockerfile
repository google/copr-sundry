FROM vrusinov/golang-build:latest as build

RUN emerge -v dev-vcs/git

RUN mkdir /tmp/build
RUN cd /tmp/build && \
  git clone https://github.com/drakkan/sftpgo && \
  cd sftpgo && \
  git checkout v1.0.0 && \
  go build -i && \
  cp sftpgo /bin && \
  mkdir -p /usr/share/sftpgo && \
  cp -r templates static /usr/share/sftpgo

FROM vrusinov/golang:latest
COPY --from=build /bin/sftpgo /bin/sftpgo
COPY --from=build /usr/share/sftpgo /usr/share/sftpgo
COPY --from=build /usr/bin/git-receive-pack /usr/bin/git-receive-pack
COPY --from=build /usr/bin/git-upload-archive /usr/bin/git-upload-archive
COPY --from=build /usr/bin/git-upload-pack /usr/bin/git-upload-pack
COPY --from=build /usr/libexec/git-core/ /usr/libexec/git-core

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/bin/sftpgo", "-v"]
