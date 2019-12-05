import urllib.request

import cv2
import numpy as np
from pydarknet import Detector, Image


def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model once and for all and reload weights
    net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"),
                   bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                   bytes("cfg/coco.data", encoding="utf-8"))

    # img = cv2.imread("cars-on-busy-street-3456x2304_73674.jpg")

    def model_api(input_data):
        # url = 'https://cdn.motor1.com/images/mgl/QlveY/s1/2019-audi-a7.jpg'
        url = input_data.get('image_url')
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)

        img2 = Image(img)

        #r = net.classify(img2)
        #print(r)
        results = net.detect(img2)
        is_car = False
        car_score = 0
        car_bbox = []
        for cat, score, bbox in results:
            if cat.decode() == 'car':
                is_car = True
                car_score = score
                car_bbox = bbox
                break
        return {
            'includes_car': is_car,
            'score': car_score,
            'bbox': car_bbox
        }

    return model_api
