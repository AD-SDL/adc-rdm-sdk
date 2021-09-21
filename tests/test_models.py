import json

from adc_sdk.models import User


def test_user(example_dir):
    user_reply = json.loads(example_dir.joinpath('user.json').read_text())
    user = User.parse_obj(user_reply['me'])
    assert user.globus_username == "my_username"
    assert user.created.day == 6
