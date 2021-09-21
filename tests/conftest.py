from pathlib import Path

from pytest import fixture


@fixture()
def example_dir():
    return Path(__file__).parent.joinpath('example-outputs')
