import requests

#Making GET Requests

#======Making sample request======

url = "https://icanhazdadjoke.com/"
response = requests.get(url)
#Get the HTTP status code
print(response.status_code)
#Get HTML code of the page
print(response.text)

#======Making requests to get data in HTML format======

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {"Accept": "text/html"})
print(response.text)

#======Making requests to get data in plain text format======

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {"Accept": "text/plain"})
print(response.text)

#======Making requests to get data in JSON data format======

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {"Accept": "application/json"})
print(response.text)

