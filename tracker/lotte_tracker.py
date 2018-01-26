import traceback
from telnetlib import EC

from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tracker.tracker import Tracker
from util.connection_manager import getPhantomDriverUsingUrl


class LotteTracker(Tracker):
    def track(self):
        driver = getPhantomDriverUsingUrl(self.url)
        result = None
        try:
            if driver is None:
                raise Exception

            driver.find_element_by_name('InvNo').send_keys(self.invoice)
            driver.find_element(By.CLASS_NAME, 'mal_5').click()

            WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reserve_01')))
            tree = html.fromstring(driver.page_source)
            driver.close()
            elements = tree.cssselect(self.pattern)
            result = elements[elements.__len__() - 1].text_content().strip()
        except Exception:
            traceback.print_exc()
            result = None
        return result