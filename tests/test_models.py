import json

from adc_sdk.models import User, Sample, Study, StudySubscriptionEvent, CreateSampleResponse


def test_user(example_dir):
    user_reply = json.loads(example_dir.joinpath('current_user.json').read_text())
    user = User.parse_obj(user_reply['me'])
    assert user.globus_username == "test_username"
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


def test_create_sample(example_dir):
    reply = json.loads(example_dir.joinpath('create_sample.json').read_text())
    obj = CreateSampleResponse.parse_obj(reply)
    assert obj.success
    assert obj.sample is not None


def test_study_event(example_dir):
    reply = json.loads(example_dir.joinpath('subscribe_to_study_new-sample.json').read_text())
    obj = StudySubscriptionEvent.parse_event(reply['study'])
    assert obj.study is not None
