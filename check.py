import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

response =  requests.get('https://api.themoviedb.org/3/movie/11?api_key=API_KEY')
