from models.base import MBTADataModel


class Stop(MBTADataModel):
    @property
    def name(self):
        return self.attributes.get("name")

    @property
    def address(self):
        return self.attributes.get("address")

    def serialize(self):
        return "ID: {}, NAME: {}".format(self.id, self.name)
