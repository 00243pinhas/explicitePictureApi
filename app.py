import os

from flask import Flask
import tensorflow as tf
from flask import request, jsonify

model = tf.keras.models.load_model("my_model.h5")

@app.route("/predict", methods=["POST"])


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"
    