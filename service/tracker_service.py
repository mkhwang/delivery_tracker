from domain.order_deliveries import OrderDeliveries
from domain.url_config import UrlConfig
from tracker.common_tracker import CommonTracker
from tracker.hanjin_tracker import HanjinTracker
from tracker.lotte_tracker import LotteTracker


class TrackerService:
    def __init__(self):
        self.url_config = UrlConfig.get_instance()
        """ logger """

    def track(self):
        """ db select """
        delivery_list = OrderDeliveries.where('', '').get()
        for delivery in delivery_list:
            if delivery.shipper_id is not 10 and delivery.shipper_id is not 2:
                tracker = CommonTracker(delivery)
            elif delivery.shipper_id is 2:
                tracker = HanjinTracker(delivery)
            else:
                tracker = LotteTracker(delivery)

            result = tracker.track()
            print(result)
            """ db update """