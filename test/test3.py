from tracker.common_tracker import CommonTracker


class Delivery:
    def __init__(self):
        self.shipper_id = 3
        self.invoice = 370226793151


if __name__ == '__main__':
    tracker = CommonTracker(Delivery())
    result = tracker.track()
    print(result.strip())