from tracker.common_tracker import CommonTracker
from tracker.hanjin_tracker import HanjinTracker
from tracker.kg_tracker import KGTracker
from tracker.lotte_tracker import LotteTracker


class TrackerFactory(object):
    @staticmethod
    def get_tracker(delivery):
        if delivery.shipper_id is 10:
            tracker = LotteTracker(delivery)
        if delivery.shipper_id is 2:
            tracker = HanjinTracker(delivery)
        elif delivery.shipper_id is 5 or delivery.shipper_id is 9:
            tracker = HanjinTracker(delivery)
        elif delivery.shipper_id is 6 or delivery.shipper_id is 7:
            tracker = KGTracker(delivery)
        else:
            tracker = CommonTracker(delivery)
        return tracker