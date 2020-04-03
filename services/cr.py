import requests

import config
from models.prediction import Prediction
from models.route import Route
from models.stop import Stop
from models.trip import Trip


class CommuterRailService:
    def __init__(self):
        pass

    def fetch_routes_and_stop(self, stop_id):
        routes, stop = self.fetch_routes(stop=stop_id)

        return {route.id: route for route in routes}, stop

    @staticmethod
    def fetch(path, params):
        url = "{}/{}".format(config.Core.MBTA_API, path)
        response = requests.get(url=url, params=params)
        data = response.json()
        return data.get("data"), data.get("included")

    def fetch_routes(self, stop):
        params = {
            "filter[stop]": stop,
            "filter[type]": 2,
            "include": "stop",
        }
        routes, included = self.fetch(path="routes", params=params)
        return [Route(r) for r in routes], Stop(included[0])

    def fetch_predictions_and_trips(self, route_ids):
        params = {
            "filter[stop]": config.Core.MBCR_GATEWAY,
            "filter[direction_id]": 0,
            "filter[route]": ",".join(route_ids),
            "include": "trip",
        }

        predictions, included = self.fetch(path="predictions", params=params)

        if predictions:
            trips_by_id = {}
            for t in included:
                trip = Trip(t)
                trips_by_id[trip.id] = trip
            return [Prediction(p) for p in predictions], trips_by_id
        else:
            return [], {}
