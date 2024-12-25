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
	return response.json()


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
	return response.json()


def is_shorten_link(url):
	parsed = urlparse(url)

	if len(parsed[2]) <=7:
		return True
	else:
		return False


def main():

	load_dotenv()
	token = os.getenv("VK_API_KEY")
	url = input("Введите ссылку: ")

	try:

		if is_shorten_link(url) == False:
			short_link = shorten_link(token, url)["response"]["short_url"]
			print("Сокращенная ссылка", short_link)
		else:
			is_shorten_link_url =  urlparse(url)[2]
			is_shorten_link_url_edit = is_shorten_link_url[1:]
			link = is_shorten_link_url_edit
			click_amount = count_clicks(token, link)["response"]["stats"][0]["views"]
			print("Количество переходов по ссылке: ", click_amount)

	except KeyError:

		print("Некорректный URL!")

if __name__ == '__main__':
    main()