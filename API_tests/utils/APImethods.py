import requests
import dataclasses


@dataclasses.dataclass
class ApiMethods:

    @staticmethod
    def create_user(domain, json):
        req = requests.post(f'{domain}/message/', json=json)
        print(req.json())
        return req


    @staticmethod
    def get_user_by_id(domain, id):
        req = requests.get(f'{domain}/message/{id}')
        print(req.json())
        return req
