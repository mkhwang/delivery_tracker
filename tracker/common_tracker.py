from lxml import html

from tracker.tracker import Tracker
from util.connection_manager import getHtmlUsingRequest


class CommonTracker(Tracker):
    def track(self):
        source = getHtmlUsingRequest(self.url.format(self.invoice))
        tree = html.fromstring(source)
        elements = tree.cssselect(self.pattern)
        return elements[elements.__len__()-1].text