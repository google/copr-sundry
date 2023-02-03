FROM vrusinov/nodejs-build:18.12.1 as build

RUN USE="curl" emerge -v dev-vcs/git
RUN mkdir /tmp/build
WORKDIR /tmp/build
RUN git clone https://github.com/brbeaird/netatmo-wunderground-agent
WORKDIR /tmp/build/netatmo-wunderground-agent
RUN npm install --verbose
RUN mkdir -p /opt/netatmo-wunderground-agent/
RUN cp server.js /opt/netatmo-wunderground-agent/
RUN cp -r node_modules /opt/netatmo-wunderground-agent/

FROM vrusinov/nodejs:18.12.1
COPY --from=build /usr/lib64/node_modules /usr/lib64/node_modules
COPY --from=build /opt/netatmo-wunderground-agent/ /opt/netatmo-wunderground-agent/

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/node", "/opt/netatmo-wunderground-agent/server.js"]
