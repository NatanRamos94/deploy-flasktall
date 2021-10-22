from flask import Flask, request
import pickle
import numpy as np

app=Flask(__name__)
@app.route("/")
def home():
    return 'Deploy ML'
