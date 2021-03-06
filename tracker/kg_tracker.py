from lxml import html

from tracker.tracker import Tracker
from util.connection_manager import postHtmlUsingRequest


class KGTracker(Tracker):
    def track(self):
        form_data = {'item_no': self.invoice}
        source = postHtmlUsingRequest(self.url, form_data)
        tree = html.fromstring(source)
        elements = tree.cssselect(self.pattern)
        result = elements[elements.__len__()-1].text_content()
        return result