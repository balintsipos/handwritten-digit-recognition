from flask import Flask, render_template, url_for, request, jsonify, make_response
from io import BytesIO
import base64
from PIL import Image, ImageOps
from numpy import asarray
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    if request.is_json:
        req = request.get_json()

        drawnImage = (req['image'])
        drawnImage = drawnImage.replace("data:image/png;base64,", "")
        drawnImage = base64.b64decode(drawnImage)
        rawImage = Image.open(BytesIO(drawnImage))
        resizedImage = rawImage.resize((28,28))
        invertedImage = ImageOps.invert(resizedImage.convert('RGB'))

        pixels = asarray(invertedImage)
        result_arr = []
        for i in pixels:
            for j in i:
                result_arr.append(int(np.sum(j)/3))
        
        data = [result_arr]
        df = pd.DataFrame(data)
        loaded_model = pickle.load(open('typeface_model_best.pkl','rb'))
        predictedValue = loaded_model.predict(df)
        print(predictedValue[0])
        response = {
            "predictedValue": str(predictedValue[0]),
        }

        response = make_response(jsonify(response), 200)
        return response

    else:
        return "No JSON received", 400


if __name__ == "__main__":
    app.run(debug = True)