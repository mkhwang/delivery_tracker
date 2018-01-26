import traceback
from lxml import html
from lxml.html.clean import Cleaner
from lxml.etree import tostring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import codecs

from util.connection_manager import getHtmlUsingRequest, getPhantomDriverUsingUrl

if __name__ == '__main__':
    """우체국"""
    # url = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1='
    # url = ''
    # invoice_number_list = list()
    # invoice_number_list.append('6863233791326')
    # invoice_number_list.append('6069509124652')
    # pattern = '#print > div.h4_wrap.ma_t_5 > table.table_col.detail_on.ma_b_0.no-print > tbody > tr > td:nth-child(4)'
    #
    # for invoice in invoice_number_list:
    #     print(invoice)
    #     target_url = 'https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1={0}&displayHeader=N'.format(invoice)
    #     source = getHtmlUsingRequest(target_url)
    #     tree = html.fromstring(source)
    #     elements = tree.cssselect(pattern)
    #     print(elements[elements.__len__()-1].text)
    #     print('----------------------------------------------------------------')

    """한진"""
    # cleaner = Cleaner()
    # cleaner.style = True
    # cleaner.javascript = True
    # url = 'http://www.hanjinexpress.hanjin.net/customer/plsql/hddcw07.result?wbl_num='
    # invoice = '412179452204'
    # source = getHtmlUsingRequest('http://www.hanjinexpress.hanjin.net/customer/plsql/hddcw07.result?wbl_num=412179452204')
    # source = cleaner.clean_html(source)
    # # print(source)
    # #
    # pattern = 'tr > td'
    # tree = html.fromstring(source)
    # elements = tree.xpath("//td[@width=70]//b//font")
    # print(elements[elements.__len__()-1].text)
    # # elements = tree.cssselect(pattern)
    # # target = list()
    # # # print(elements[elements.__len__()-1].cssselect('font')[0].text)
    # # for item in elements:
    # #     # print(item)
    # #     # print(tostring(item))
    # #     if 'width' in item.attrib and item.attrib['width'].__eq__('70'):
    # #         # print(tostring(item))
    # #         print(item.cssselect('font')[0].text)

    """CJ대한통운"""
    # cleaner = Cleaner()
    # cleaner.style = True
    # cleaner.javascript = True
    # url = 'http://www.hanjinexpress.hanjin.net/customer/plsql/hddcw07.result?wbl_num='
    # invoice = '412179452204'
    # source = getHtmlUsingRequest('https://www.doortodoor.co.kr/parcel/doortodoor.do?fsp_action=PARC_ACT_002&fsp_cmd=retrieveInvNoACT&invc_no=341447358544')
    # # source = cleaner.clean_html(source)
    # # print(source)
    # tree = html.fromstring(source)
    # elements = tree.cssselect('table.mb15 > tr > td:nth-child(1)')
    # print(elements[elements.__len__()-1].text.strip())
    # for item in elements:
    #     # print(tostring(item))
    #     print(item.text.strip())

    """로젠택배"""
    # cleaner = Cleaner()
    # cleaner.style = True
    # cleaner.javascript = True
    # invoice = '97086683886'
    # url = 'https://www.ilogen.com/iLOGEN.Web.New/TRACE/TraceDetail.aspx?slipno={0}&gubun=fromview'.format(invoice)
    # source = getHtmlUsingRequest(url)
    # # source = cleaner.clean_html(source)
    # pattern = '#gridTrace > tr > td:nth-child(3)'
    # tree = html.fromstring(source)
    # elements = tree.cssselect(pattern)
    # # for item in elements:
    # #     print(item.text)
    # print(elements[elements.__len__()-2].text.strip())

    """롯데택배"""
    url = "https://www.lotteglogis.com/home/personal/inquiry/track"
    invoice = '305586864122'
    driver = getPhantomDriverUsingUrl(url)
    try:
        if driver is None:
            raise Exception

        driver.find_element_by_name('InvNo').send_keys(invoice)
        driver.find_element(By.CLASS_NAME, 'mal_5').click()

        element = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reserve_01')))
        tree = html.fromstring(driver.page_source)
        elements = tree.cssselect('div.reserve_01 > div:nth-child(3) > table.table_02 > tbody > tr > td:nth-child(3)')
        print(elements[elements.__len__() - 1].text_content().strip())
    except Exception:
        traceback.print_exc()
    finally:
        driver.close()