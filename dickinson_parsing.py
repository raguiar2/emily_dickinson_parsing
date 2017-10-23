from bs4 import BeautifulSoup as soup
import requests
import re

# website to pull poems from
ROOT_URL = 'http://www.bartleby.com/113/'
HTML_SUFFIX = '.html'
#comments to get poem between
def main():
	poemcounts = {1000:1}
	#poemcounts = {1000:138, 2000:111, 3000:57, 4000:141, 5000:146}
	for chpaterstart in poemcounts:
		for idxstart in range(1,poemcounts[chpaterstart]+1):
			poemnumber = str(chpaterstart+idxstart)
			url = ROOT_URL+poemnumber+HTML_SUFFIX
			print('url')
			r = requests.get(url)
			print(r.content)
			regex = '<!-- BEGIN CHAPTER -->(.*?)<!-- END CHAPTER -->'
			poem = re.findall(regex, str(r.content))[0]
			poemsoup = soup(poem, "html5lib")
			# replace EOL characters in poems. 
			poemtext = poemsoup.text.replace('\\n','\n')
			fixedtext = ""
			# delete line numbers
			for char in poemtext:
				if char.isdigit():
					continue
				else:
					fixedtext += char
			# strip EOL. 
			fixedtext = fixedtext.strip()
			titleend = fixedtext.find('\n')
			title = fixedtext[0:titleend]
			# write to txt file
			with open(title+'.txt','w') as f:
				f.write(fixedtext)


if __name__ == "__main__":
	main()