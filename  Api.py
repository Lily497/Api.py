import requests
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

data = response.json()


pick = input("If you would like a joke please put the letter 1 or put anything else if you dont want a joke.... u r warned:    ")
if pick == "1":
    fact = data["value"]
    print(fact)
else:
    print("ok, i hate u. you hate yourself. u r unlovable. I am done with you if you do not want to hear my joke get away.no one likes you. if you are not going to pick one u r dead to me, please leave.")
