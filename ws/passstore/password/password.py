import json


class PasswordEntry:
    def __init__(self, username, password, name):
        if name is None:
            raise TypeError("'name' cannot be None")
        self.username = username
        self.password = password
        self.name = name

    def __str__(self):
        return "name:{}\nusername: {}\nPassword: {}".format(self.name, self.username, self.password)

    def to_dict(self):
        return {'name': self.name, 'username': self.username, 'password': self.password}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    @staticmethod
    def from_json(json_data):
        return PasswordEntry(**json.loads(json_data))
