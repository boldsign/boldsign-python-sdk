# tests/conftest.py

import sys
import os
import pytest

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import boldsign

# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--integration", action="store_true", default=False, help="Run integration tests"
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--integration"):
        # --integration given in cli: do not skip integration tests
        return
    skip_integration = pytest.mark.skip(reason="need --integration option to run")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)
