from flask import Flask, render_template, url_for, request, jsonify, make_response

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    
    if request.is_json:
        req = request.get_json()

        return "JSON received", 200

    else:
        return "No JSON received", 400


if __name__ == "__main__":
    app.run(debug = True)