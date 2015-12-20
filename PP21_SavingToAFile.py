import requests
from bs4 import BeautifulSoup


def title_grab(web_page):
	
	r = requests.get(web_page)
	soup = BeautifulSoup(r.text, 'html.parser')
	text = ""

	for title in soup(class_='story-heading'):
		if title.a:
			text = text + title.a.text.replace("\n", " ").strip() + "\n"
		else:
			text = text + title.contents[0].strip() + "\n"

	with open('NYTimesTitles.txt', 'w') as open_file:
	    open_file.write(text)


if __name__ == '__main__':
	title_grab('http://www.nytimes.com')
