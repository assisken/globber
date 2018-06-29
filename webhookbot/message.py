import json


class Encoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items() if v is not None}


class Message:
    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps(self, cls=Encoder, ensure_ascii=False)
