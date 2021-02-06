import os
from joblib import load
import flask

PORT = os.getenv('PORT') or 8080

app = flask.Flask(__name__)
model = load('model.joblib')


@app.route('/predict', methods=['GET'])
def predict():
    query = flask.request.args
    visits_last_year = query.get('VisitsLastYear')
    question_text_length = query.get('QuestionTextLength')

    if not (is_int(visits_last_year) and is_int(question_text_length)):
        return flask.abort(400)

    features = [[visits_last_year, question_text_length]]
    model_output = model.predict(features)
    prediction = bool(model_output[0])

    return flask.jsonify({'prediction': prediction})


def is_int(value):
    if value is None:
        return False

    try:
        val = int(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    app.run(port=PORT)
