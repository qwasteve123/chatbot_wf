import openai
import os
import requests


set_env_var()
response = openai.Image.create(
  prompt="Japanese girl in school uniform",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
res = requests.get(image_url)
if res.status_code:
    fp = open('test.jpg', 'wb')
    fp.write(res.content)
    fp.close()
pass