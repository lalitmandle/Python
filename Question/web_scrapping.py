import bs4
from urllib.request import urlopen as newUreq
from bs4 import BeautifulSoup as soup
url = 'https://incometaxindia.gov.in/pages/tools/income-tax-calculator.aspx'
Uclient = newUreq(url)
html_page = Uclient.read()
Uclient.close()
html_soup = soup(html_page, "html.parser")
html_soup.h1
# it is incomplete 