import requests
import re


def get_subheads(url):
    response = requests.get(url)
    text = response.text
    subheads = re.findall(r'<h3.*?>(.*?)</h3>', text)
    return subheads


print(get_subheads('http://www.columbia.edu/~fdc/sample.html'))