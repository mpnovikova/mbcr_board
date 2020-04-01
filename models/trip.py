from models.base import MBTADataModel


class Trip(MBTADataModel):
    @property
    def name(self):
        return self.attributes.get("name")

    @property
    def headsign(self):
        return self.attributes.get("headsign")
