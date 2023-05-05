from flask import Flask, render_template, request, jsonify, make_response
from io import BytesIO
import base64
from PIL import Image, ImageOps
from numpy import asarray
import numpy as np
import pickle
import pandas as pd
import sklearn
from functools import wraps
from time import perf_counter
import warnings

warnings.filterwarnings('ignore') 

def getTime(function):
    """Times any function with a return value"""

    @wraps(function)
    def wrapper(*args, **kwargs):
        startTime = perf_counter()
        result = function(*args, **kwargs)
        endTime = perf_counter()
        totalTime = round(endTime - startTime, 10)
        print(function.__name__, 'took', totalTime, 'seconds')
        return result

    return wrapper


@getTime
def processImage(image):
    image = image.replace("data:image/png;base64,", "")
    image = base64.b64decode(image)
    rawImage = Image.open(BytesIO(image))
    resizedImage = rawImage.resize((28,28))
    invertedImage = ImageOps.invert(resizedImage.convert('RGB'))
    pixels = asarray(invertedImage)
    return pixels

@getTime
def dataframeTransform(pixels):
    result_arr = []
    for i in pixels:
        for j in i:
            result_arr.append(int(np.sum(j)/3))
    
    data = [result_arr]
    df = pd.DataFrame(data)
    return df


@getTime
def predictResult(df):
    loaded_model = pickle.load(open('typeface_model_best.pkl','rb'))
    prediction = loaded_model.predict(df)
    return prediction


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@getTime
def predict():
    if request.is_json:
        req = request.get_json()
        pixels = processImage(req['image'])
        df = dataframeTransform(pixels)
        predictedValue = predictResult(df)
        print(predictedValue[0])
        response = {
            "predictedValue": str(predictedValue[0]),
        }

        response = make_response(jsonify(response), 200)
        return response

    else:
        return "No JSON received", 400

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")