import time

import requests
import os
from urllib.parse import urlparse

from main import test_prompt

url_api = "https://lexica.art/api/infinite-prompts"
url_image = "https://image.lexica.art/sm2_webp/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}
proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890"
}


def get_prompt():
    data = {
        "text": "girl",
        "model": "lexica-aperture-v3.5",
        "searchMode": "prompts",
        "limit": 10,
        "source": "search",
        # "cursor": 10
    }
    try:
        response = requests.post(url_api, proxies=proxies, headers=headers, json=data)
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            prompts = json['prompts']
            print(f"prompts: {len(prompts)}")
            for prompt in prompts:
                print(prompt['prompt'])
                test_prompt(prompt['prompt'])
                time.sleep(2)
                # if len(prompt['images']):
                #     image_id = prompt['images'][0]['id']
                #     image_url = url_image + image_id
                #     # download_image(image_url)
                #     # sleep 1 second
                #     time.sleep(1)
    except Exception as e:
        print("error:", str(e))


# def download_image(image_url):
#     print(image_url)
#     if image_url:
#         # 下载图片到本地output目录
#         parsed_url = urlparse(image_url)
#         file_name = os.path.basename(parsed_url.path + ".jpg")
#
#         # 下载图片到本地output目录，使用URL中的文件名
#         output_directory = 'data/output'
#         os.makedirs(output_directory, exist_ok=True)
#
#         image_response = requests.get(image_url, proxies=proxies, headers=headers, )
#         if image_response.status_code == 200:
#             file_path = os.path.join(output_directory, file_name)
#             if os.path.exists(file_path):
#                 return
#             with open(file_path, 'wb') as image_file:
#                 image_file.write(image_response.content)
#             print(f'Saved as {file_name}')
#         else:
#             print(f'Failed to download image. Status Code: {image_response.status_code}')
#     else:
#         print('Image URL not found in the response.')


get_prompt()
