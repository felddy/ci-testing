# syntax=docker/dockerfile:1

ARG VERSION

FROM alpine

ARG TARGETPLATFORM
ARG BUILDPLATFORM

RUN \
  echo $TARGETPLATFORM > target_platform.txt \
  && echo $BUILDPLATFORM > build_platform.txt \
  && echo $VERSION > image_version.txt

COPY src/entrypoint.sh ./

ENTRYPOINT [ "./entrypoint.sh" ]
