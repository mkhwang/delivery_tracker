from abc import ABCMeta, abstractmethod

from domain.tracker_pattern import TrackerPattern
from domain.url_config import UrlConfig


class Tracker(metaclass=ABCMeta):
    def __init__(self, delivery):
        self.url = UrlConfig.get_instance().get_url(delivery.shipper_id)
        self.pattern = TrackerPattern.get_instance().get_pattern(delivery.shipper_id)
        self.invoice = delivery.invoice

    @abstractmethod
    def track(self):
        pass