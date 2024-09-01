from bs4 import BeautifulSoup
import requests

class SteamData:

    def __init__(self) -> None:
        self.url =  "https://steamdb.info/"

    