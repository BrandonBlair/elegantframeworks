import requests

def test_twitter_is_present():
    resp = requests.get("http://techstepacademy.com/training-ground")
    assert "twitter" in resp.text 
