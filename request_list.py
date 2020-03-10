# (method, url, json body, headers, cookies, expected status code)
reqs = [
    ('GET', 'https://postman-echo.com/get', {}, {}, {}, 200),
    ('POST', 'https://postman-echo.com/post', {"json-contents": ["red", "blue", "green"]}, {'username': 'JohnDoe'}, {'firstCookie': 'cookie1'}, 200)
]