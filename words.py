import requests
import json
userWord = input('Give me a word: ')
regex = "{0,1})(".join(userWord)
regex = '^(' + regex + '{0,1})$'
url = 'https://wordsapiv1.p.mashape.com/words/?letterPattern=' +regex
headers = {
    'X-Mashape-Key': '8c27159218mshe871e6abcfbf6a1p1244b4jsnd763ed26b693',
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
response = json.loads(response.text)
print ("\n".join(response['results']['data']))