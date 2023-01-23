#!/usr/bin/env python
# encoding: utf-8
import base64

import cv2 as cv
from flask import Flask, jsonify, request, render_template
from flask_restful import Api

from person_detection_service import PersonDetectionService

app = Flask(__name__)
api = Api(app)

pd_service = PersonDetectionService()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/personDetection', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return 'Image required', 400
    image = request.files['image']
    if not is_photo(image.filename):
        return 'File must be a type of image', 400
    processed_image,number_of_people= pd_service.processImage(image.read())
    _, img_encoded = cv.imencode('.jpg',processed_image)
    img64 = base64.b64encode(img_encoded.tostring()).decode()
    return jsonify({"status": "ok", "processed_image": img64,"number_of_people":number_of_people})


def is_photo(filename: str) -> bool:
    filename_split = filename.split('.')
    allowed_extensions = ['jpg', 'jpeg', 'png']
    if len(filename_split) != 2:
        return False
    return filename_split[1] in allowed_extensions


if __name__ == "__main__":
    app.run(debug=True)
