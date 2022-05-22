import pprint
import mechanize
from bs4 import BeautifulSoup
import http.cookiejar as cookielib


def navigation(url: str) -> None:
    """
    explore the internet
    :param url:
    :return:
    """
    browser = mechanize.Browser()
    page = browser.open(url)
    source_code = page.read()
    parse = BeautifulSoup(source_code, 'html.parser')
    pprint.pprint(f"Titulo da página: {parse.find('h1').text}")
    pprint.pprint(f"Conteúdo principal: {[x.text for x in parse.findAll('p')]}")


def anonymousNavigate(url: str, proxy: dict) -> None:
    """
    navigato anony
    :param url:
    :param proxy:
    :return:
    """
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    parse = BeautifulSoup(source_code, 'html.parser')
    print(parse)


def clearCookies() -> None:
    """
    Clear the cookie to non indentify
    :return:
    """
    browser = mechanize.Browser()
    cookies = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookies)
    for cookie_ in cookies:
        print(cookie_)

if __name__ == '__main__':
    proxy: dict = {'http':"216.155.139.115:3128"}
    anonymousNavigate("url", proxy)
    clearCookies()