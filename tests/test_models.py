from pathlib import Path
import json

from adc_sdk.models import User

_example_dir = Path(__file__).parent.joinpath('example-outputs')


def test_user():
    user_reply = json.loads(_example_dir.joinpath('user.json').read_text())
    user = User.parse_obj(user_reply['me'])
    assert user.globus_username == "my_username"
    assert user.created.day == 6
