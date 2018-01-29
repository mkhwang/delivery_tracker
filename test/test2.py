import json

from lxml import html

from domain.tracker_pattern import TrackerPattern
from domain.url_config import UrlConfig
from lxml.etree import tostring

from abc import ABCMeta, abstractmethod

from util.connection_manager import getHtmlUsingRequest, postHtmlUsingRequest


class Tracker(metaclass=ABCMeta):
    def __init__(self):
        print('i am tracker')
        self.msg = 'i am tracker'

    @abstractmethod
    def track(self):
        print('i am tracker')


class TrackerDummy(Tracker):
    def track(self):
        print('i am dummy2')
        return 1


if __name__ == '__main__':
    # print(UrlConfig.get_instance().get_url(1))
    # print(TrackerPattern.get_instance().get_pattern(1))
    # tracker = TrackerDummy()
    # print(tracker.msg)
    # print(tracker.track())
    # print(tracker.track())
    # url = 'http://www.kdexp.com/newDeliverySearch.kd?barcode=3109010400362'
    # url = 'http://apps.ds3211.co.kr/freight/internalFreightSearch.ht?billno=9332801001536'
    # url = 'http://www.hdexp.co.kr/deliverySearch2.hd?barcode=6201045200002'
    # source = getHtmlUsingRequest(url)
    # delivery_dic = json.loads(source)
    # if 'items' in delivery_dic:
    #     for item in delivery_dic['items']:
    #         print(item['stat'])

    # print(source)
    # pattern = '#printarea > table:nth-child(5) > tbody > tr > td:nth-child(6)'
    # tree = html.fromstring(source)
    # print(source)
    # elements = tree.cssselect('#printarea > table:nth-child(2)')
    # print(elements.__len__())
    # for item in elements:
    #     print(tostring(item))

    # elements = tree.xpath('//*[@id="printarea"]/table[2]/tr/td[6]')
    # print(elements[elements.__len__()-1].text_content())
    # print(elements.__len__())
    # for item in elements:
    #     print(item.text_content())

    # dic_data = json.loads(source)
    # print(dic_data['items'])
    # for item in dic_data['items']:
    #     print(item['stat'])
    # url = 'http://www.kglogis.co.kr/delivery/delivery_result.jsp'
    # form_data = {'item_no': '149077915792'}
    # # import requests
    # #
    # # r = requests.post(url, data=form_data)
    # # print(r.status_code, r.reason)
    # # print(r.encoding)
    # source = postHtmlUsingRequest(url, form_data)
    # # print(source)
    # tree = html.fromstring(source)
    # elements = tree.cssselect('#contents > article.inquiry_result > table > tbody > tr > td:nth-child(3)')
    # print(elements[elements.__len__()-1].text_content())
    # for item in elements:
    #     print(item.text_content())


    url = 'https://www.ds3211.co.kr/freight/internalFreightSearch.ht'
    form_data = {'billno': '9332801001536'}
    source = postHtmlUsingRequest(url, form_data)
    # print(source)
    # import codecs
    # f = codecs.open('../data/대신택배.html', 'r', 'utf-8')
    # source = f.read()
    # f.close()
    tree = html.fromstring(source)
    # elements = tree.cssselect('#printarea > table tr')
    elements = tree.xpath('//*[@id="printarea"]/table[2]/tr/td[6]')
    print(elements[elements.__len__()-1].text_content())
    # for item in elements:
    #     print(item.text_content())

    # for item in elements:
    #     print(item.text_content())

    ##printarea > table:nth-child(5) > tbody > tr:nth-child(5) > td:nth-child(6)
    #//*[@id="printarea"]/table[2]/tbody/tr[5]/td[6]