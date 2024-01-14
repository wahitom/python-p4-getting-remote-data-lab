#  Import both request and json form python 

import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

class GetRequester:

    #  initialize the class methid and takes in url parameter and assigns it to self.url
    #  this makes the url accessible within the class instance ie the whole of it and not
    #  just the def __init__() area
    def __init__(self, url):
        self.url = url

    # here we ant to send a get request to the url stored in self.url 
    def get_response_body(self):
        #  the requests.get fuction takes the self.url as an argument and 
        #  returns the content of the response 
        #  the content is returned as raw data received from the server 
        response = requests.get(self.url)
        return response.content

  
    def load_json(self):
        #  this method calls the get_response_body to get the response cotnent 
        response_body = self.get_response_body()
        #  this method then uses the json.loads to parse the content and converts it to 
        #  a list or dictionary
        return json.loads(response_body)
    

#  create an instance with theurl 
requester = GetRequester(url)

#  calls the get_repspone_body method on the requester instance making a GET request
# and printing the raw response content 
response_body = requester.get_response_body()
# print(response_body)

json_data = requester.load_json()
print(json.dumps(json_data, indent = 4, sort_keys=True))