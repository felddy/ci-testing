
# ci-testing #

[![GitHub Build Status](https://github.com/felddy/foundryvtt-docker/workflows/build/badge.svg)](https://github.com/felddy/ci-testing/actions/workflows/build.yml)
[![CodeQL](https://github.com/felddy/foundryvtt-docker/workflows/CodeQL/badge.svg)](https://github.com/felddy/ci-testing/actions/workflows/codeql-analysis.yml)

This repo is used to test GitHub Actions workflows.

1. Build the image using `buildx`:

    ```console
    docker buildx build \
      --platform linux/amd64 \
      --build-arg VERSION=1.2.3 \
      --output type=docker \
      --tag felddy/ci-testing:1.2.3 .
    ```

1. Testing

    ```console
    pytest --image-tag felddy/ci-testing:1.2.3
    ```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is released as open source under the [MIT license](LICENSE).

All contributions to this project will be released under the same MIT license.
By submitting a pull request, you are agreeing to comply with this waiver of
copyright interest.
