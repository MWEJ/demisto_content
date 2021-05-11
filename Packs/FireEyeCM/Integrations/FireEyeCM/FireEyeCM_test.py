import json
import io


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def test_dummy():
    util_load_json('test_data/alerts.json')
    assert 1 == 1