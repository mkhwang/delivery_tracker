import traceback
from lxml import html

from util.connection_manager import getHtmlUsingRequest

if __name__ == '__main__':
    url = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1='
    url = ''
    invoice_number_list = list()
    invoice_number_list.append('6863233791326')
    invoice_number_list.append('6069509124652')
    pattern = '#print > div.h4_wrap.ma_t_5 > table.table_col.detail_on.ma_b_0.no-print > tbody > tr > td:nth-child(4)'

    for invoice in invoice_number_list:
        print(invoice)
        target_url = 'https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1={0}&displayHeader=N'.format(invoice)
        source = getHtmlUsingRequest(target_url)
        tree = html.fromstring(source)
        elements = tree.cssselect(pattern)
        for item in elements:
            print(item.text)
        # print(source)
        print('----------------------------------------------------------------')
