# syntax=docker/dockerfile:1

ARG VERSION

FROM --platform=$BUILDPLATFORM tonistiigi/xx AS xx

FROM --platform=$BUILDPLATFORM alpine AS build

COPY --from=xx / /
RUN apk add clang lld
COPY src/entrypoint.c ./

ARG TARGETPLATFORM
RUN xx-apk add gcc musl-dev
RUN xx-clang -o entrypoint entrypoint.c && \
  xx-verify entrypoint

FROM alpine as final

ARG BUILDPLATFORM
ARG TARGETPLATFORM
ARG VERSION

RUN \
  echo $TARGETPLATFORM > target_platform.txt \
  && echo $BUILDPLATFORM > build_platform.txt \
  && echo $VERSION > image_version.txt

COPY --from=build entrypoint ./

ENTRYPOINT [ "./entrypoint" ]
