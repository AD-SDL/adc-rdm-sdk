import json
from pathlib import Path

from pytest_mock import MockFixture
from pytest import fixture

from adc_sdk import __version__
from adc_sdk.client import ADCClient


@fixture()
def client():
    return ADCClient('fake_token')


def test_version():
    assert __version__ == "0.1.2"


def _mock_response(mocker: MockFixture, example_dir: Path, file_name):
    """Mock the response from the ADC service

    Args:
        mocker: Pytest Mocker object
        example_dir: Path to the example files
        file_name: File containing the response content
    """
    ex_reply = json.loads(example_dir.joinpath(file_name).read_text())
    mocker.patch('adc_sdk.client.ADCClient._execute', return_value=ex_reply)


def _mock_subscribe(mocker: MockFixture, example_dir: Path, file_name):
    """Mock the subscription to an event queue

    Args:
        mocker: Pytest Mocker object
        example_dir: Path to the example files
        file_name: File containing the event text
    """
    ex_reply = json.loads(example_dir.joinpath(file_name).read_text())
    mocker.patch('gql.Client.subscribe', return_value=iter([ex_reply]))


def test_current_user(client, example_dir, mocker: MockFixture):
    _mock_response(mocker, example_dir, 'user.json')
    user = client.get_current_user()
    assert user.id == "VXNlcjo1"


def test_get_sample(client, example_dir, mocker):
    _mock_response(mocker, example_dir, 'sample.json')
    sample = client.get_sample('fake')
    assert sample.name == "000286e59a"


def test_get_study(client, example_dir, mocker):
    _mock_response(mocker, example_dir, 'study.json')
    study = client.get_study('fake')
    assert study.name == "polybot-ai-test"


def test_subscribe(client, example_dir, mocker):
    _mock_subscribe(mocker, example_dir, 'subscribe-to-study_new-sample.json')
    event = next(client.subscribe_to_study('fake'))
    assert event.study.name == '706data'
