import requests
import json
import webbrowser

def gugu():
     my_endpoint = 'https://dog.ceo/api/breeds/image/random'
     facts = requests.get(my_endpoint)
     print(facts.text)
     data = json.loads(facts.text)
     webbrowser.open_new_tab(data['message'])
     print("Your welcome for the cool dog image")
gugu()

