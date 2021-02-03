import requests

URL = 'http://jsonplaceholder.typicode.com/'

POSTS = 'posts/'



def get(id):
    r_get = requests.get(URL + POSTS + str(id))
    return r_get

def post(data):
    r_post = requests.post(URL + POSTS, data)
    return r_post