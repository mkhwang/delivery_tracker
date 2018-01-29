import traceback

from domain.order_deliveries import OrderDeliveries
from domain.url_config import UrlConfig
from tracker.tracker_factory import TrackerFactory


class TrackerService:
    def __init__(self):
        self.url_config = UrlConfig.get_instance()
        """ logger """

    def track(self):
        """ db select """
        delivery_list = OrderDeliveries.where('', '').get()
        for delivery in delivery_list:
            try:
                result = TrackerFactory.get_tracker(delivery).track()
            except Exception:
                traceback.print_exc()
                result = None
            if result is not None:
                print('update db')
                """ db update """