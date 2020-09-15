import requests
from environment import *

class Retrieve():
  def retrieve_all(self):
    return requests.get(f"{CONFIG['url']}/produtos")