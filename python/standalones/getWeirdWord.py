from pandas import read_html
import string, random, requests

while True:
  letter = random.choice(string.ascii_lowercase)
  url = 'http://phrontistery.info/{}.html'.format(letter)
  html = requests.post(url).content
  tableList = read_html(html)
  wordlist = tableList[2]
  row = random.randint(1,len(wordlist))
  print("\n\t***********")
  print("\t"+wordlist.iloc[row][0]+" - "+wordlist.iloc[row][1])
  print("\t***********")
  
  input("\npress enter for another word")