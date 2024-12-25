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

		if is_shorten_link(url) == True:
			link = shorten_link(token, url)["response"]["key"]
			click_amount = count_clicks(token, link)["response"]["stats"][0]["views"]
			print("Количество переходов по ссылке: ", click_amount)
		else:
			short_link = shorten_link(token, url)["response"]["short_url"]
			print("Сокращенная ссылка", short_link)

	except KeyError:

		print("Некорректный URL!")








	# try:

		


	# 	url_is_shorten_link = is_shorten_link(url)[1]


	# 	short_link = shorten_link(token, url)["response"]["short_url"]
	# 	print("Сокращенная ссылка", short_link)

	# 	link = shorten_link(token, url)["response"]["key"]
	# 	click_amount = count_clicks(token, link)["response"]["stats"][0]["views"]
	# 	print("Количество переходов по ссылке: ", click_amount)


	# except KeyError:
	# 	print("Некорректный URL!")











# short_link = shorten_link(token, url)["response"]["short_url"]
# 		print("Сокращенная ссылка", short_link)

# 		link = shorten_link(token, url)["response"]["key"]
# 		click_quantity = count_clicks(token, link)["response"]["views"]
# 		print("Количнство просмотров", click_quantity)

	# payload = {"access_token":token,
	#  "v":5.199,
	#  "url":"dvmn.org/modules "
	#  }



	# time_url = 'https://api.vk.ru/method/utils.getShortLink'
	# response = requests.get(time_url, params=payload)
	# response.raise_for_status()
	# print("Ваш URL:",response.text)





	# time_url = 'https://api.vk.ru/method/utils.getServerTime'
	# response = requests.get(time_url, params=payload)
	# response.raise_for_status()
	# print(response.text)


	# payload = {"text": "python"}

	# response = requests.get('https://yandex.ru', params=payload)
	# response.raise_for_status()

	# >>> response.url
	# 'https://yandex.ru/?text=python'


if __name__ == '__main__':
    main()