from flask import Flask, request
app=Flask(__name__)

import time
import uuid

@app.route("/process", methods=["POST"])
def process():
    run_id = uuid.uuid4()
    app.logger.info(request.data)
    request_json = request.get_json(silent=True)
    if request_json and "sleep_duration" in request_json:
        sleep_duration = request_json["sleep_duration"] * 60
    else:
        sleep_duration = 5 * 60
    app.logger.info(f"#{run_id} - timeout test will wait {sleep_duration} seconds")
    time.sleep(sleep_duration)
    app.logger.info(f"#{run_id} - timeout test has waited {sleep_duration} seconds")
    return f"Timeout test {run_id} complete: {sleep_duration} seconds"
