#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request, Response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})


@app.route('/api/personDetection', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return 'Image required', 400
    image = request.files['image']
    if not is_photo(image.filename):
        return 'File must be a type of image', 400
    print(is_photo(image.filename))
    print(type(image))
    print(image.filename)
    print(image.stream.read())
    return jsonify({"status": "ok"})


def is_photo(filename: str) -> bool:
    filename_split = filename.split('.')
    allowed_extensions = ['jpg', 'jpeg', 'png']
    if len(filename_split) != 2:
        return False
    return filename_split[1] in allowed_extensions


if __name__ == "__main__":
    app.run(debug=True)
