import pytest

DOMAIN = 'https://automationintesting.online'


@pytest.fixture(scope='function')
def domain():
    yield DOMAIN
