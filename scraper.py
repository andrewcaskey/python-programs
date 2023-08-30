url = 'https://archive.org/details/profarnoldehrets00ehre/page/8/mode/2up?ref=ol&view=theater'

import requests
response = requests.get(url)
html = response.text

