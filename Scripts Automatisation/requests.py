
import requests

reponse=requests.get("https://codeavecjonathan.com/res/programmation.txt")
print(reponse.text)