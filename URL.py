import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):

	payload = {"access_token":token,
	 "v":5.199,
	 "url": url
	 }

	link_url = 'https://api.vk.ru/method/utils.getShortLink'
	response = requests.get(link_url, params=payload)
	response.raise_for_status()
	return response.json()["response"]["short_url"]

def count_clicks(token, link):
	
	payload_click = {"access_token":token,
	 "v":5.199,
	 "key": link,
	 "interval": "forever",
	 "extended": 0
	 }

	click_url = 'https://api.vk.ru/method/utils.getLinkStats'
	response = requests.get(click_url, params=payload_click)
	response.raise_for_status()
	return response.json()["response"]["stats"][0]["views"]

def is_shorten_link(url, token):

	payload = {"access_token":token,
	 "v":5.199,
	 "url": url
	 }
	link_url = 'https://api.vk.ru/method/utils.getShortLink'

	try:
		response = requests.get(link_url, params=payload)
		if "short_url" in response.json()["response"]:
			return False
	except KeyError:
		return True

def main():

	load_dotenv()
	token = os.environ["VK_API_KEY"]
	url = input("Введите ссылку: ")

	try:

		if not is_shorten_link(url, token):
			short_link = shorten_link(token, url)
			print("Сокращенная ссылка", short_link)
		else:
			scheme, netloc, path, params, query, fragments = urlparse(url)
			link = path [1:]
			click_amount = count_clicks(token, link)
			print("Количество переходов по ссылке: ", click_amount)

	except KeyError:

		print("Вы ввели неправильную ссылку!")

if __name__ == '__main__':
    main()