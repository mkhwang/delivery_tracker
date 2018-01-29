import json

from tracker.tracker import Tracker
from util.connection_manager import getHtmlUsingRequest


class KDHDTracker(Tracker):

    def track(self):
        source = getHtmlUsingRequest(self.url.format(self.invoice))
        delivery_data = json.loads(source)
        result = None
        if 'items' in delivery_data:
            for item in delivery_data['items']:
                result = item['stat']
        return result

