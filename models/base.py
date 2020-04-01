class MBTADataModel:
    def __init__(self, props):
        self.props = props
        self.DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

    @property
    def id(self):
        return self.props.get("id")

    @property
    def attributes(self):
        return self.props.get("attributes")

    @property
    def relationships(self):
        return self.props.get("relationships")
