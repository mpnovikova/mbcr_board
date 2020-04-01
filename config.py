class Core(object):
    DEBUG = True
    MBTA_API = "https://api-v3.mbta.com"
    MBCR_GATEWAY = "place-north"


class Development(Core):
    pass


class Test(Core):
    pass


class Production(Core):
    pass
