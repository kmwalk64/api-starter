import requests

URL = "http://api.open-notify.org/astros.json"
data = {
  "message": "success",
  "number": 3,
  "people": [
    {
      "name": "Andrew Morgan",
      "craft": "ISS"
    },
    {
      "name": "Oleg Skripochka",
      "craft": "ISS"
    },
    {
      "name": "Jessica Meir",
      "craft": "ISS"
    },
  ]
}
res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(data["message"])