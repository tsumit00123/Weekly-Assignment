import sys
import requests
if len(sys.argv) < 2:
    print("Usage: python task6.py <URL>")
    sys.exit(1)
url = sys.argv[1]
if not url.startswith(("http://", "https://")):
    url = "http://" + url
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"The website {url} is working!")
    else:
       print(f"The website {url} returned status code {response.status_code}.")
except requests.exceptions.RequestException as e:
    print(f"Could not reach the website {url}. Error: {e}")

