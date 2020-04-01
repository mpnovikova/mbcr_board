from datetime import datetime

from models.base import MBTADataModel
import re


class Prediction(MBTADataModel):
    @property
    def departure_time(self):
        if self.attributes.get("departure_time"):
            departure_time = datetime.strptime(self.attributes.get("departure_time"), self.DATE_FORMAT)
            return departure_time.strftime("%I:%M %p")
        else:
            return None

    @property
    def status(self):
        return self.attributes.get("status")

    @property
    def route_id(self):
        return self.relationships.get("route").get("data").get("id")

    @property
    def trip_id(self):
        return self.relationships.get("trip").get("data").get("id")

    @property
    def track_id(self):
        stop = self.relationships.get("stop").get("data").get("id")
        track = re.search("\\d+", stop)
        return track.group(0)
