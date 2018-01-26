import configparser


class TrackerPattern(object):
    INSTANCE = None

    def __init__(self):
        self.read_config()

    def read_config(self):
        section = 'PATTERN'
        parser = configparser.ConfigParser()
        parser.read('../conf/pattern.conf')
        self.cj = parser.get(section, 'CJ')
        self.epost = parser.get(section, 'EPOST')
        self.hanjin = parser.get(section, 'HANJIN')
        self.logen = parser.get(section, 'LOGEN')
        self.kd = parser.get(section, 'KD')
        self.kg = parser.get(section, 'KG')
        self.ds = parser.get(section, 'DS')
        self.hd = parser.get(section, 'HD')
        self.lotte = parser.get(section, 'LOTTE')

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = TrackerPattern()
        return cls.INSTANCE

    def get_pattern(self, shipper_id):
        if 1 == shipper_id:
            return self.epost
        elif 2 == shipper_id:
            return self.hanjin
        elif 3 == shipper_id:
            return self.cj
        elif 4 == shipper_id:
            return self.logen
        elif 5 == shipper_id:
            return self.kd
        elif 6 == shipper_id:
            return self.kg
        elif 7 == shipper_id:
            return self.kg
        elif 8 == shipper_id:
            return self.ds
        elif 9 == shipper_id:
            return self.hd
        elif 10 == shipper_id:
            return self.lotte
