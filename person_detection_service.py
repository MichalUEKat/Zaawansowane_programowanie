import numpy
import tensorflow_hub as tfh
import tensorflow as tf
import cv2

class PersonDetectionService:
    def __init__(self):
        # Apply image detector on a single image.
        self.detector = tfh.load("https://tfhub.dev/tensorflow/retinanet/resnet101_v1_fpn_640x640/1")

    def processImage(self, image_as_str: str):
        file_bytes = numpy.fromstring(image_as_str, numpy.uint8)
        img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        dim= (640, 640)
        img_resized = cv2.resize(img_rgb,dim)
        img_resized = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
        image_to_tensor = tf.convert_to_tensor(img_resized)
        img = tf.reshape(image_to_tensor,[1,640,640,3])
        detector_output= self.detector(img)
        print(detector_output)
