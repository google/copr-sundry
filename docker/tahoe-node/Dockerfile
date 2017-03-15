FROM dockertahoe/tahoe-lafs

# Web/API port
EXPOSE 3456
# Client port
EXPOSE 27577

COPY start.sh /usr/local/bin/start.sh
RUN mkdir -p /var/lib/tahoe

ENTRYPOINT ["/usr/local/bin/start.sh"]
