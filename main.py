import requests
URL1 = "https://pokeapi.co/api/v2/pokemon/ditto/"
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
Imposter = {
  "imposter/"
  "https://pokeapi.co/api/v2/ability/150/"
  "slot3"}
Limber = {"limber"
  "https://pokeapi.co/api/v2/ability/7/"
  "is_hidden_false_slot_1/"
  "base_experience_101"}
Powder = {"metal-powder"
  "https://pokeapi.co/api/v2/item/234/"
  "name_quick-powder"
  "https://pokeapi.co/api/v2/item/251/"}
Transform = {"transform"
  "slot_2/"
  "https://pokeapi.co/api/v2/move/144/"}
Ditto = {"ditto/"
  "id_132/"
  "order_197/"
  "height_3/"
  "weight_40/"
  "type_normal/"
  "https://pokeapi.co/api/v2/type/1/"}

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format
red = requests.get(URL1)
red = red.json()

print(data["message"])
print(data["people"][0])
print("What do you want to know?")
I = input("Imposter(Y/N)")
if I == "Y":
  print(Imposter)
L = input("Limber(Y/N)")
if L == "Y":
  print(Limber)
P = input("Powder(Y/N)")
if P == "Y":
  print(Powder)
T = input("Trasform(Y/N)")
if T == "Y":
  print(Transform)
D = input("Ditto(Y/N)")
if D == "Y":
  print(Ditto)