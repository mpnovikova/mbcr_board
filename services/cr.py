import requests

import config
from models.prediction import Prediction
from models.route import Route
from models.trip import Trip


class CommuterRailService:
    def __init__(self):
        self.routes = self.fetch_routes()
        self.route_ids = [r.id for r in self.routes]

    def routes_by_id(self):
        if not self.routes:
            self.routes = self.fetch_routes()

        return {route.id: route for route in self.routes}

    @staticmethod
    def fetch(path, params):
        url = "{}/{}".format(config.Core.MBTA_API, path)
        response = requests.get(url=url, params=params)
        data = response.json()
        return data.get("data"), data.get("included")

    def fetch_routes(self):
        params = {
            "filter[stop]": config.Core.MBCR_GATEWAY,
            "filter[type]": 2,
            "include": "stop"
        }
        routes, included = self.fetch(path="routes", params=params)
        return [Route(r) for r in routes]

    def fetch_predictions_and_trips(self):
        params = {
            "filter[stop]": config.Core.MBCR_GATEWAY,
            "filter[direction_id]": 0,
            "filter[route]": ",".join(self.route_ids),
            "include": "trip"
        }

        predictions, included = self.fetch(path="predictions", params=params)

        if predictions:
            trips_by_id = {}
            for t in included:
                trip = Trip(t)
                trips_by_id[trip.id] = trip
            return [Prediction(p) for p in predictions], trips_by_id
        else:
            return []
