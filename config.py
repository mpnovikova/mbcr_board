class Core(object):
    DEBUG = True
    MBTA_API = "https://api-v3.mbta.com"


class Development(Core):
    pass


class Test(Core):
    pass


class Production(Core):
    pass
