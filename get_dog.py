import requests
from pprint import pprint

# breed_search = input("What breed are you looking for?")

api_key='3539d314-545c-4f60-a573-619dfa38bebb'
base_url = 'https://dog.ceo/api/'

def _get(resource):
    """Sends a GET request to the provided resource and returns the 'message' data if it exists."""
    url = '{0}{1}'.format(base_url, resource)
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['message']
    else:
        raise Exception("Invalid breed selected.")

def master_breeds():
    """Gets all breeds, not including sub-breeds. Returns a list of breed names."""
    return _get('breeds/list')


def random_image(breed_search):
    """Gets a random dog image. Returns a url as a string"""
    if breed_search == 'random':
        return _get('breeds/image/random')
    else:
        return _get('breed/{0}/images/random'.format(breed_search))


if __name__ =='__main__':
    print(master_breeds())
    breed_search = input("Select a breed from the above list or write random.")
    print(random_image(breed_search))


