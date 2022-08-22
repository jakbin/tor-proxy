# Tor-Proxy

Run your any python service over tor using tor-proxy.It doesn’t interfere with other tor processes on your computer, so you can use the Tor Browser or the system tor on their own.

 [![PyPI version](https://badge.fury.io/py/tor-proxy.svg)](https://badge.fury.io/py/tor-proxy)
 [![Downloads](https://pepy.tech/badge/tor-proxy/month)](https://pepy.tech/project/tor-proxy)
 [![Downloads](https://static.pepy.tech/personalized-badge/tor-proxy?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/tor-proxy)
 ![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)


### Disclaimer:-
Use it only for educational purpose.

## Features
- No need root permission
- Multiple instances

## Compatability
Python 3.6+ is required.

## Installation

```bash
pip install tor-proxy
```

## Quickstart
1. Import with ```from tor_proxy import tor_proxy``` .
2. call function `tor_proxy()` , store as variable and give it as port argument in proxies.

```python
# tor_proxy_example.py
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
```

### Credit :- [onionshare](https://github.com/onionshare/onionshare)