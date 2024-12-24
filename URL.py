import requests
import os
from dotenv import load_dotenv



load_dotenv()


def shorten_link(token, url):

	payload = {"access_token":token,
	 "v":5.199,
	 "url": url
	 }

	link_url = 'https://api.vk.ru/method/utils.getShortLink'
	try:
		response = requests.get(link_url, params=payload)
		response.raise_for_status()
	except:
		print("invalid url")
	return response.json()["response"]["short_url"]



def main():

	load_dotenv()
	token = os.getenv("VK_API_KEY")
	url = input("Введите ссылку: ")
	print('Сокращенная ссылка: ', shorten_link(token, url))




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