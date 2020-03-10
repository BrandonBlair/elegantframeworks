import json

import xlrd


fname = ('DataDrivenTest.xlsx')


def retrieve_data_from_excel_file():

    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_index(0)  # Assuming first sheet

    test_requests = []

    # Column numbers for data
    method_column = 0
    url_column = 1
    json_column = 2
    headers_column = 3
    cookies_column = 4
    expected_status_column = 5

    for row in range(sheet.nrows):
        method = sheet.cell_value(row, method_column)
        if method:
            url = sheet.cell_value(row, url_column)
            json_body = sheet.cell_value(row, json_column)
            headers = json.loads(sheet.cell_value(row, headers_column))
            cookies = json.loads(sheet.cell_value(row, cookies_column))
            status = int(sheet.cell_value(row, expected_status_column))

            test_requests.append((method, url, json_body, headers, cookies, status))

    return test_requests
