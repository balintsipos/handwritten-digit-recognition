# Handwritten Digit Recognition Web App

LIVE DEMO: [CLICK HERE](https://balintsipos.pythonanywhere.com/)

## Description

MNIST is a common dataset in the machine learning world to test different solutions, and as my first time using images with machine learning, I chose an MNIST-like dataset to see how well I can perform and deploy a proper working machine learning application.

The application consists of an HTML/CSS frontend which uses vanilla JavaScript to communicate with a Flask-based Python backend serving a REST API endpoint.

The model tries to predict the digit you draw within the canvas provided on the left. For the best results, try to center your drawing as much as possible, and avoid too large, or too small drawings. My model uses the TMNIST dataset from Kaggle, which instead uses typefaces instead of handwritten digits as opposed to its traditional counterpart. These datasets however aren't made for real-world use, and perfect accuracy outside of their training set is difficult to achieve. 

## Technologies used

- Python 3.10
- Flask
- sci-kit learn (SKLearn)
- Jupyter Notebooks
- JavaScript
- HTML
- CSS