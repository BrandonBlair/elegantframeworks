from pytest import mark

import requests

from request_list import reqs
from process_excel_data import retrieve_data_from_excel_file

excel_data = retrieve_data_from_excel_file()

@mark.parametrize('method, url, json_body, headers, cookies, expected_status', reqs)
def test_requests_from_dictionary(method, url, json_body, headers, cookies, expected_status):
    print(f"Currently processing a {method} request for URL {url} using headers {headers} and cookies {cookies}")
    if method == 'POST':
        response = requests.post(url=url, json=json_body, headers=headers, cookies=cookies)
    elif method == 'GET':
        response = requests.get(url=url, headers=headers, cookies=cookies)
    else:
        assert False, f"{method} is not a supported Method"

    assert response.status_code == expected_status


@mark.parametrize('method, url, json_body, headers, cookies, expected_status', excel_data)
def test_requests_from_excel_file(method, url, json_body, headers, cookies, expected_status):
    print(f"Currently processing a {method} request for URL {url} using headers {headers} and cookies {cookies}")
    if method == 'POST':
        response = requests.post(url=url, json=json_body, headers=headers, cookies=cookies)
    elif method == 'GET':
        response = requests.get(url=url, headers=headers, cookies=cookies)
    else:
        assert False, f"{method} is not a supported Method"

    assert response.status_code == expected_status
