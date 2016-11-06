from decouple import config
from watson_developer_cloud import VisualRecognitionV3

test_url = 'http://tudosobrecachorros.com.br/wp-content/uploads/cachorro-independente.jpg'

visual_recognition = VisualRecognitionV3(
    '2016-11-06', api_key=config('API_KEY'))

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
