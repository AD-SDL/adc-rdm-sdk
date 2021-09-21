import json

from adc_sdk.models import User, Sample, Study


def test_user(example_dir):
    user_reply = json.loads(example_dir.joinpath('user.json').read_text())
    user = User.parse_obj(user_reply['me'])
    assert user.globus_username == "my_username"
    assert user.created.day == 6


def test_sample(example_dir):
    sample_reply = json.loads(example_dir.joinpath('sample.json').read_text())
    sample = Sample.parse_obj(sample_reply['sample'])
    assert sample.name == '000286e59a'
    assert sample.get_file() == '200 OK'


def test_study(example_dir):
    reply = json.loads(example_dir.joinpath('study.json').read_text())
    obj = Study.parse_response(reply['study'])
    assert obj.name == 'polybot-ai-test'
    assert obj.permissions[0].user.id == 'VXNlcjo1'
    assert len(obj.samples) == 2
