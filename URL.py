import requests
import os
from dotenv import load_dotenv



load_dotenv()

def main():

	load_dotenv()
	apikey = os.getenv("VK_API_KEY")


	payload = {"access_token":apikey, "v":5.199}

	time_url = 'https://api.vk.ru/method/utils.getServerTime'
	response = requests.get(time_url, params=payload)
	response.raise_for_status()
	print(response.text)



	# payload = {"text": "python"}

	# response = requests.get('https://yandex.ru', params=payload)
	# response.raise_for_status()

	# >>> response.url
	# 'https://yandex.ru/?text=python'


if __name__ == '__main__':
    main()