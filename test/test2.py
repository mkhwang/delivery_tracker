from domain.tracker_pattern import TrackerPattern
from domain.url_config import UrlConfig

from abc import ABCMeta, abstractmethod


class Tracker(metaclass=ABCMeta):
    def __init__(self):
        print('i am tracker')
        self.msg = 'i am tracker'

    @abstractmethod
    def track(self):
        print('i am tracker')


class TrackerDummy(Tracker):
    def track(self):
        print('i am dummy2')
        return 1


if __name__ == '__main__':
    # print(UrlConfig.get_instance().get_url(1))
    # print(TrackerPattern.get_instance().get_pattern(1))
    tracker = TrackerDummy()
    print(tracker.msg)
    print(tracker.track())
    print(tracker.track())
