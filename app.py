from datetime import datetime

from flask import Flask, render_template, jsonify

from errors.api_error import ApiError
from models.stop import Stop
from services.cr import CommuterRailService

app = Flask(__name__)
cr_service = CommuterRailService()


@app.route("/<stop_id>", methods=["GET"])
def board(stop_id):
    if stop_id not in Stop.VALID_STOPS:
        raise ApiError("Invalid stop", 400)

    routes_by_id, stop = cr_service.fetch_routes_and_stop(stop_id)
    predictions, trips_by_id = cr_service.fetch_predictions_and_trips(
        routes_by_id.keys(),
        stop_id
    )
    length = len(predictions)
    now = datetime.now()

    return render_template(
        "board.html",
        date=now.strftime("%A %m-%d-%Y"),
        time=now.strftime("%H:%M %p"),
        stop=stop,
        length=length,
        predictions=predictions,
        routes_by_id=routes_by_id,
        trips_by_id=trips_by_id,
    )


@app.errorhandler(ApiError)
def handle_api_error(error):
    response = jsonify(error.serialize())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run()
