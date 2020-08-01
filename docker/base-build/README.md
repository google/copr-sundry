# Base-build docker image

The base-build image is based on Gentoo. I use it as an environment to build all
other images.

It is not intended to be used directly but as an environment to build more
stuff. It is recommended to "rebase" real images on top of 'base' using
multi-stage builds, e.g.

foo-build Dockerfile:

```Dockerfile
FROM vrusinov/base-build:latest as base-build

emerge -v app-misc/foo
```

foo Dockerfile:

```Dockerfile
FROM vrusinov/foo-build as build

FROM vrusinov/base as base

COPY --from build /usr/bin/foo /usr/bin/foo
```
