import json


def read_json(path):
    return json.load(open(path))
def write_json(data,path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
