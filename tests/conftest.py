"""pytest configuration."""

# Standard Python Libraries
from pathlib import Path
import re

# Third-Party Libraries
import docker
import pytest

from .utils import RedactedPrinter

MAIN_SERVICE_NAME = "main"
REDACTION_REGEXES = [
    re.compile(r"AWSAccessKeyId=(.*?)&Signature=(.*?)&"),
]
VERSION_FILE = "src/_version.py"
VERSION_SERVICE_NAME = f"{MAIN_SERVICE_NAME}-version"

client = docker.from_env()


@pytest.fixture(scope="session")
def main_container(image_tag):
    """Fixture for the main container."""
    container = client.containers.run(
        image_tag,
        detach=True,
        environment={},
        name=MAIN_SERVICE_NAME,
        ports={},
        volumes={str(Path.cwd() / Path("data")): {"bind": "/data", "driver": "local"}},
    )
    yield container
    container.remove(force=True)


@pytest.fixture(scope="session")
def version_container(image_tag):
    """Fixture for the version container."""
    container = client.containers.run(
        image_tag,
        command="--version",
        detach=True,
        name=VERSION_SERVICE_NAME,
    )
    yield container
    container.remove(force=True)


@pytest.fixture(scope="session")
def project_version():
    """Get the project version."""
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    return pkg_vars["__version__"]


@pytest.fixture(scope="session")
def redacted_printer():
    """Return a configured redacted printer object."""
    return RedactedPrinter(REDACTION_REGEXES)


def pytest_addoption(parser):
    """Add new commandline options to pytest."""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )
    parser.addoption(
        "--image-tag",
        action="store",
        default="local/test-image:latest",
        help="image tag to test",
    )


@pytest.fixture(scope="session")
def image_tag(request):
    """Get the image tag to test."""
    return request.config.getoption("--image-tag")


def pytest_collection_modifyitems(config, items):
    """Modify collected tests based on custom marks and commandline options."""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
