import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="w",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )
try:
    print(10/0)
except Exception:
    logging.exception("Exception")

"""
>>> 2+2
5
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()

import urllib.request
import requests

opener = urllib.request.build_opener()
response = opener.open("https://bank.gov.ua/")
print(response.read())