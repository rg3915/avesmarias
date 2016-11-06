import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

# test_url = 'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'
# test_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Thomas_J_Watson_Sr.jpg/800px-Thomas_J_Watson_Sr.jpg'
test_url = 'http://tudosobrecachorros.com.br/wp-content/uploads/cachorro-independente.jpg'

visual_recognition = VisualRecognitionV3('2016-11-06', api_key='aadd9bb59c10ec90e0e6ee622a855e70431a0054')

analise = visual_recognition.classify(images_url=test_url)
if analise['images'][0]['classifiers'][0]['classes'][0]['class'] == 'person':
    face = visual_recognition.detect_faces(images_url=test_url)
    genero = face['images'][0]['faces'][0]['gender']['gender']
    if genero == 'FEMALE':
        print('Cadastro válido.')
    else:
        print('Cadastro sujeito a aprovação.')
else:
    print('Por favor, envie uma foto válida.')
