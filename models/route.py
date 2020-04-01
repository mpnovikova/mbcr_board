from models.base import MBTADataModel


class Route(MBTADataModel):
    @property
    def name(self):
        return self.attributes.get("long_name")

    @property
    def fare_class(self):
        return self.attributes.get("fare_class")

    @property
    def destination(self):
        return self.attributes.get("direction_destinations")[0]
