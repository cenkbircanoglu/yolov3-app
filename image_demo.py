import urllib.request

import cv2
import numpy as np
from pydarknet import Detector, Image

if __name__ == "__main__":

    net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"),
                   bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                   bytes("cfg/coco.data", encoding="utf-8"))

    # img = cv2.imread("cars-on-busy-street-3456x2304_73674.jpg")
    url = 'https://cdn.motor1.com/images/mgl/QlveY/s1/2019-audi-a7.jpg'
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    img2 = Image(img)

    # r = net.classify(img2)
    results = net.detect(img2)
    for cat, score, _ in results:
        print(str(cat), score)
