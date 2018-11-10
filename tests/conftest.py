import json

from pytest import fixture
from selenium import webdriver


data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand_from_fixture(request):
    data = request.param
    return data
