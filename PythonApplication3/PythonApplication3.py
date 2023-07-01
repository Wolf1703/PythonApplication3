
import requests

def isDitto():
	res = requests.get("https://pokeapi.co/api/v2/pokemon/picachu")
	return "ditto".encode() in res.content

def isJynx():
	res = requests.get("https://pokeapi.co/api/v2/pokemon/jynx")
	return "jynx".encode() in res.content

def isScyther():
	res = requests.get("https://pokeapi.co/api/v2/pokemon/scyher")
	return "scyther".encode() in res.content

def isSeadra():
	res = requests.get("https://pokeapi.co/api/v2/pokemon/seadra")
	return "seadra".encode() in res.content

def isRhyhorn():
	res = requests.get("https://pokeapi.co/api/v2/pokemon/rhyhor")
	return "rhyhorn".encode() in res.content


print("Is.Ditto",isDitto())
print("Is.Jynx",isJynx())
print("Is.Scyther",isScyther())
print("Is.Seadra",isSeadra())
print("Is.Rhyhorn",isRhyhorn())