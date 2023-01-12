import allure
import requests
import pytest
from ..utils.Api_methods import ApiMethods
from ..utils.json_files import JsonFile


@pytest.mark.parametrize("name", ['Artyom', 'ROMAN', 'Олег'])
@allure.suite("API tests")
def test_create_user(domain, name):
    json = JsonFile.json_create_user(name)
    res1: requests.Response = ApiMethods.create_user(domain, json)
    id_user = res1.json()['messageid']
    res2: requests.Response = ApiMethods.get_user_by_id(domain, id_user)
    assert res1.status_code == 201 and res2.status_code == 200
