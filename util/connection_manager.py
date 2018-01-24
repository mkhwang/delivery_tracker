import traceback
import urllib

from selenium import webdriver
from urllib.parse import urlsplit


def getHtmlUsingRequest(url):
    header = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.1-update1; ko-kr; Nexus One Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
        'Connection': 'keep-alive'}

    try:
        connection = urllib.request.Request(url, headers=header)
        req = urllib.request.urlopen(connection)
        # current_url = ''
        charset = req.info().get_content_charset()
        source = req.read().decode(charset)
    except Exception as e:
        traceback.print_exc()
        source = '<html><head></head><body><h1>Fail</h1></body></html>'
    return source


def getHtmlUsingWebDriver(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'none',
               'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.7,*;q=0.3',
               # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
               'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.1-update1; ko-kr; Nexus One Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17'
               }

    try:
        for key in headers:
            webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

        driver = webdriver.PhantomJS('D:\workspace_pycharm\ssum_parser\driver\phantomjs',
                                     service_args=['--load-images=no'])
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)
        driver.get(url)
        current_url = driver.current_url
        page_html = driver.page_source
        driver.close()
    except Exception as e:
        traceback.print_exc()
        page_html = '<html><head></head><body><h1>Fail</h1></body></html>'
        current_url = url
    return page_html, current_url


def getDetailPageUsingWebDriver(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'none',
               'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.7,*;q=0.3',
               # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
               'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.1-update1; ko-kr; Nexus One Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17'
               }

    try:
        for key in headers:
            webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

        driver = webdriver.PhantomJS('D:\workspace_pycharm\ssum_parser\driver\phantomjs',
                                     service_args=['--load-images=no'])
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)
        driver.get(url)
        current_url = driver.current_url
        if current_url is None or is_wrong_url(current_url):
            raise ConnectionError
        page_html = driver.page_source
        driver.close()
    except ConnectionError as e1:
        current_url = None
        page_html = '<html><head></head><body><h1>Fail</h1></body></html>'
    except Exception as e:
        traceback.print_exc()
        page_html = '<html><head></head><body><h1>Fail</h1></body></html>'
        current_url = url
    return page_html, current_url


def get_domain_from_url(url):
    try:
        base_url = "{0.scheme}://{0.netloc}".format(urlsplit(url))
    except Exception as e:
        traceback.print_exc()
        base_url = ''
    return base_url


def get_protocol_from_url(url):
    try:
        base_url = "{0.scheme}:".format(urlsplit(url))
    except Exception as e:
        traceback.print_exc()
        base_url = ''
    return base_url


def is_wrong_url(url):
    try:
        if url.__len__() < 11:
            result = False
        else:
            domain = get_domain_from_url(url)
            url.replace(domain, '')
            if url.__len__() < 13:
                result = False
            else:
                result = True
    except Exception as e:
        traceback.print_exc()
        result = False
    return result
