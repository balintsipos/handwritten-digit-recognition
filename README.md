# Handwritten Digit Recognition Web App

LIVE DEMO: [CLICK HERE]([https://balintsipos.pythonanywhere.com/](https://flask-app.o2uq7k8vco3du.eu-west-3.cs.amazonlightsail.com/))

## Description

MNIST is a common dataset in the machine learning world to test different solutions, and as my first time using images with machine learning, I chose an MNIST-like dataset to see how well I can perform and deploy a proper working machine learning application.

The application consists of an HTML/CSS frontend which uses vanilla JavaScript to communicate with a Flask-based Python backend serving a REST API endpoint.

The model tries to predict the digit you draw within the canvas provided on the left. For the best results, try to center your drawing as much as possible, and avoid too large, or too small drawings. My model uses the TMNIST dataset from Kaggle, which instead uses typefaces instead of handwritten digits as opposed to its traditional counterpart. These datasets however aren't made for real-world use, and perfect accuracy outside of their training set is difficult to achieve. 

![an image of the working application](https://github.com/balintsipos/handwritten-digit-recognition/blob/main/screenshot.png)

## Technologies used

- Python 3.10
- Flask 2.2
- sci-kit learn (SKLearn)
- Jupyter Notebooks
- JavaScript
- HTML
- CSS
- Docker
- AWS Lightsail

## Installation and Usage

To install this application and host it yourself:

- Clone the repository to have it on your own machine
- Set up and activate a Python virtual environment
- Once active, install the libraries listed under requirements.txt (you can use $ pip install -r requirements.txt)
- If you want to host the server yourself, set run(debug=False) to run(debug=True) on the bottom of app.py
- You can now reach the working website at localhost:5000. Hurray!

## Machine Learning

For a full walkthrough of how the machine learning part of the project was done and how the final model was trained, check out [the Jupyter notebook](https://github.com/balintsipos/handwritten-digit-recognition/blob/main/screenshot.png)

You might spot another .pkl file in the repository. This was my first experiment with the original MNIST dataset. If you want to try this out too and epxeriment how the two model compares to each other, feel free to swap out the corresponding part of app.py (line 38).

## Credits

Guides and resources I used during making this project:

- Kaggle tutorial for working with the original MNIST dataset by OPENMAP4U. A nice step-by-step tutorial to working with image recognition in SKLearn, well fit for newcomers. [Source](https://www.kaggle.com/code/gainknowledge/mnist-scikit-learn-tutorial/notebook)
- Learning Flask series by Julian Nash on YouTube. Easy-to-follow introduction to Flask. [Source](https://www.youtube.com/watch?v=BUmUV8YOzgM&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L)
- Learn Flask for Python by Jake Rieger from freeCodeCamp.org. Another essential but quick Flask resource to get familiar with its base functionality and toolset. [Source](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
- The official Flask documentation. [Source](https://flask.palletsprojects.com/en/2.2.x/)
- This codepen which inspired the drawing implementation in JavaScript. [Source](https://codepen.io/w2sw2sw2s/pen/VLKEdq)
- MDN Web Docs for helping me get a better grasp of fetch() in JavaScript [Source](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

## Architecture

The application is simple but I find it useful to talk about how the application works in the background.

The app follows the following process:
- User draws on an interactive canvas. This is implemented in vanilla JavaScript following a similar logic to the one linked above. This can be cleared with the clear button which fills the entire rectangle with white. I found that drawing with grey yielded the best results for image recognition, as it was the most similar to the original training set after inverting it.
- Once the user presses predict, the JavaScript script grabs the content of the canvas, and sends a POST request to our Flask backend with the image encoded as its data in a JSON format.
- The Flask server receives this request, unwraps the JSON message, and preprocesses the image, which means: a. converting to 28x28 pixel format, b. transforming into a pandas dataframe, c. averaging the sum of each pixel to get a black and white result, d. inverting colors to match the training set. Then the application loads the model that has been trained previously (see model_training.ipynb), passes the processed image as a dataframe for it to predict.
- The predicted value gets wrapped into a JSON file again and it gets sent back to the client, where the .then() part of our JavaScript script unwraps it and changes the textContent of the html element present inside the right box and presents what our model thinks the user drew inside the canvas.

## Considerations

I chose Flask because it's easy to use and very lightweight, a good candidate for something that will most likely be hosted on a free service later on. The machine learning part is being done in Python as well, so not having to deal with a 3rd language and add another dependency makes Flask an obvious choice.

For SKLearn, while not being the best choice, I was already familiar with it, it made the whole process of training the model painless and quick, especially on a virtual machine, which lacks proper GPU support. Results would be much better if the model was trained in TensorFlow or PyTorch. The goal of this project was to deploy a working machine learning solution and not to have a perfect implementation of digit recognition.

## Future Work/Ideas

This solution could still be improved in a lot of ways:

- Obviously the model could use some fine-tuning as it currently overfits to training data.
- The question of should the image preprocessing be done on the client's side in JavaScript or on the server. Not having to do image processing on the client-side of things takes a good amount of workload of the client's machines, but could be a serious concern if multiple people were trying to access the application and this could speed up the process.
- Better canvas drawing implementation. The current implementation doesn't resemble how the original training set looked like and would require a grey shading around each drawn line to be as close as possible to the original training data.
