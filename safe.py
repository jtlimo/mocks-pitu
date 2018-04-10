import requests

def is_the_world_safe():
    response = requests.get('http://google.com')
    if response.status_code == 200:
        return True
    else:
        return False
