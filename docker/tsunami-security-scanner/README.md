# Tsunami Security Scanner

Docker image for the [Tsunami Security Scanner](https://github.com/google/tsunami-security-scanner)

# Environment variables

Configuration can be specified via environment variables:

*   `IP_V4_TARGET` - IPv4 address to scan, e.g. '8.8.8.8'
*   `IP_V6_TARGET` - IPv4 address to scan, e.g. '2001:4860:4860::8888'

Only and exactly one of IP_V4_TARGET and IP_V6_TARGET must be specified.

# Example usage:

## Docker

```bash
docker run -e "IP_V4_TARGET=127.0.0.1" --rm -it vrusinov/tsunami-security-scanner:latest
```
## Kubernetes

Example manifest:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: tsunami-scan-localhost
  namespace: tsunami
spec:
  template:
    spec:
      containers:
      - name: tsunami
        image: vrusinov/tsunami-security-scanner:latest
        env:
          - name: IP_V4_TARGET
            value: "127.0.0.1"
      restartPolicy: Never
```
