from tor_proxy import tor_proxy
import requests

port = tor_proxy()

http_proxy  = f"socks5h://127.0.0.1:{port}"
https_proxy = f"socks5h://127.0.0.1:{port}"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
            }

url = "https://api.ipify.org"

r = requests.get(url, proxies=proxies)

print(r.text)