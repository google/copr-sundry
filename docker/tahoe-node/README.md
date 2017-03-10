# Tahoe-lafs node docker image

Usage:

```bash
sudo chcon -Rt svirt_sandbox_file_t /data/tahoe
docker run -p 3333:3456 -p 27577:27577 -v /data/tahoe:/var/lib/tahoe -i -t vrusinov/tahoe-node
```

Image will create new node config, if /var/lib/tahoe is empty.
You may want to change `tub.location` since tahoe will have problems detecting
your real IP address.
