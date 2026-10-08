import urllib.request

sites = ["https://github.com", "https://google.com", "https://this-site-does-not-exist-12345.com"]

for site in sites:
     try:
         response = urllib.request.urlopen(site, timeout=5)
         print(site, "->",response.status)
     except Exception as e:
         print(site, "-> DOWN:", e)
