import requests

def GetPublicIp(): return requests.get("https://fr.geoipview.com/").text.split("http://whois.chromefans.org/")[0].split("\"show2\">")[1].split("<")[0]
def CheckInternetConnection():
	try:
		requests.get("https://www.google.fr")
		return True
	except: return False
