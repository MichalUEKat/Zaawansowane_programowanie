import numpy
import tensorflow_hub as tfh
import tensorflow as tf
import cv2


class PersonDetectionService:
    def __init__(self):
        self.detector = tfh.load("https://tfhub.dev/tensorflow/retinanet/resnet101_v1_fpn_640x640/1")

    def processImage(self, image_as_str: str):
        file_bytes = numpy.fromstring(image_as_str, numpy.uint8)
        img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        dim = (640, 640)
        img_resized = cv2.resize(img_rgb, dim)
        img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        image_to_tensor = tf.convert_to_tensor(img_resized)
        img = tf.reshape(image_to_tensor, [1, 640, 640, 3])
        detector_output = self.detector(img)
        result = {key: value.numpy() for key, value in detector_output.items()}
        boxes = result['detection_boxes'][0]
        scores = result['detection_scores'][0]
        labels = result['detection_classes'][0]

        people_indexes = [index for index, label in enumerate(labels) if label == 1.0 and scores[index] > 0.3]
        boxes = boxes[people_indexes]

        img_height, img_width, _ = img_cv.shape
        for box in boxes:
            ymin, xmin, ymax, xmax = box
            xmin, ymin, xmax, ymax = int(xmin * img_width), int(ymin * img_height), int(xmax * img_width), int(
                ymax * img_height)
            cv2.rectangle(img_cv, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)

        return img_cv, len(boxes)
