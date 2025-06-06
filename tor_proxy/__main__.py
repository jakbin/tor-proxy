from .tor_proxy import tor_proxy

def main():
    port = tor_proxy()
    print(f"Tor SOCKS proxy running on port: {port}")

if __name__ == "__main__":
    main()
