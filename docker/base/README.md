# Base docker image

The base image based on Gentoo. Can be used as a base image for others. Not
capable of running builds, but can be useful in multi-stage builds, e.g.:

```Dockerfile
FROM vrusinov/base-build:latest as base-build

emerge -v app-misc/foo

FROM vrusinov/base as base

COPY --from build /usr/bin/foo /usr/bin/foo
```
