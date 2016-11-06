from decouple import config
from watson_developer_cloud import VisualRecognitionV3


def valida_foto(test_url):
    visual_recognition = VisualRecognitionV3(
        '2016-11-06', api_key=config('API_KEY'))

    analise = visual_recognition.classify(images_url=test_url)
    if analise['images'][0]['classifiers'][0]['classes'][0]['class'] == 'person':
        face = visual_recognition.detect_faces(images_url=test_url)
        genero = face['images'][0]['faces'][0]['gender']['gender']
        if genero == 'FEMALE':
            r = 'Cadastro válido.'
        else:
            r = 'Cadastro sujeito a aprovação.'
    else:
        r = 'Por favor, envie uma foto válida.'

    return r
