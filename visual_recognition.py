import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='')

with open(join(dirname(__file__), 'barack.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))
