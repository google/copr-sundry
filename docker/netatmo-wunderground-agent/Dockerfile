FROM vrusinov/nodejs-build:latest as build

RUN emerge -v dev-vcs/git && \
    \
    mkdir /tmp/build && \
    cd /tmp/build && \
    git clone https://github.com/brbeaird/netatmo-wunderground-agent && \
    npm root -g && \
    cd netatmo-wunderground-agent && \
    npm install -g --verbose && \
    mkdir -p /opt/netatmo-wunderground-agent/ && \
    cp server.js /opt/netatmo-wunderground-agent/ && \
    cp -r node_modules /opt/netatmo-wunderground-agent/

FROM vrusinov/nodejs:latest
COPY --from=build /usr/lib64/node_modules /usr/lib64/node_modules
COPY --from=build /opt/netatmo-wunderground-agent/ /opt/netatmo-wunderground-agent/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/node", "/opt/netatmo-wunderground-agent/server.js"]
