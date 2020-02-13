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

    def model_api(url):
        car_exists = False
        try:
            if 'file://' in url:
                with open(url, 'rb') as f:
                    image = np.asarray(bytearray(f.read()), dtype="uint8")
            elif 's3://' in url:
                import boto3
                s3 = boto3.client('s3')
                bucket = url.split('/')[2]
                key = '/'.join(url.split('/')[3:])
                obj = s3.get_object(Bucket=bucket, Key=key)
                image = np.asarray(bytearray(obj['Body'].read()),
                                   dtype="uint8")
            else:
                resp = urllib.request.urlopen(url)
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
            img = cv2.imdecode(image, cv2.IMREAD_COLOR)

            img2 = Image(img)

            # r = net.classify(img2)
            results = net.detect(img2)
            response = []
            for cat, score, bbox in results:
                response.append({
                    'category': cat.decode(),
                    'proba': score,
                    'bbox': bbox
                })
            print(response)
            return response
        except Exception as e:
            return 'unknown'

    return model_api
