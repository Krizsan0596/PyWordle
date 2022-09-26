import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
word_list = []
for word in WORDS:
    if len(word) == 5:
        word_list.append(word.decode("utf-8"))
for word in word_list:
    if word.startswith("com"):
        print(word)
