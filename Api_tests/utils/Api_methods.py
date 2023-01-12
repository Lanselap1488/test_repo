import dataclasses
import requests


@dataclasses.dataclass
class ApiMethods:

    @staticmethod
    def create_user(domain, json):
        req = requests.post(f'{domain}/message/', json=json)
        print(req.json())
        return req

    @staticmethod
    def get_user_by_id(domain, id_user):
        req = requests.get(f'{domain}/message/{id_user}')
        print(req.json())
        return req
