import requests
from bs4 import BeautifulSoup


def geturl(url):
  
  chk = 'https://'

  if chk not in url:
    url = '%s%s'%(chk, url)  
  
  return url
  
  
url = input('url:')
filetype = input('filetype:')
url = geturl(url)  

s = requests.Session()
page = s.get(url, timeout=5)
soup = BeautifulSoup(page.text, 'html.parser')
res = soup.find_all(href = True)
##res2 = soup.find_all(src = True)

for i in range(len(res)):
  if filetype in str(res[i]):
    print('\n\n\n%d) %s'%(i, res[i]['href']))
	
'''	
for i in range(len(res2)):
  if filetype in res2[i]:
    print('%d) %s'%(i, res2[i]['src'))	
'''
	
    
url = res[int(input('which you want 2 download:'))]['href']
url = geturl(url)
timeout = input('timeout(None or num):')

try:
  timeout = int(timeout)
except:
  timeout = None


filename = input('filename:')
print('\ndownloading..........')

s = requests.Session()
sth = s.get(url, timeout=timeout)
f = open(filename, 'wb')
f.write(sth.content)
f.close()
print('\nsaved %s'%filename)
	
	


