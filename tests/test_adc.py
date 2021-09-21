import json

from pytest_mock import MockFixture
from pytest import fixture

from adc_sdk import __version__
from adc_sdk.client import ADCClient


@fixture()
def client():
    return ADCClient('fake_token')


def test_version():
    assert __version__ == "0.1.2"


def test_current_user(client, example_dir, mocker: MockFixture):
    ex_reply = json.loads(example_dir.joinpath('user.json').read_text())
    mocker.patch('adc_sdk.client.ADCClient._execute', return_value=ex_reply)
    user = client.get_current_user()
    assert user.id == "VXNlcjo1"
