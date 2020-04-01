from flask import Flask, render_template

from services.cr import CommuterRailService

app = Flask(__name__)
cr_service = CommuterRailService()


@app.route('/')
def board():
    routes_by_id = cr_service.routes_by_id()
    predictions, trips_by_id = cr_service.fetch_predictions_and_trips()
    for p in predictions:
        print(p.props)
    length = len(predictions)
    return render_template("north.html",
                           length=length,
                           predictions=predictions,
                           routes_by_id=routes_by_id,
                           trips_by_id=trips_by_id
                           )


if __name__ == '__main__':
    app.run()
