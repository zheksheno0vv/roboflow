import requests
import io
from fastapi import HTTPException
from config import config

async  def get_prediction(image_bytes:bytes):
    try:
        print('Roboflow кошулду')
        url = config.ROBOFLOW_URL
        files = {
            'file':('image.jpg',io.BytesIO(image_bytes),'image/jbg')
        }

        responses = requests.post(url, files=files)

        print(responses.text)

        if responses.status_code !=200:
            raise HTTPException(status_code=500,detail='Ошыбка')

        return {'time answer':responses.json()['time'],
                'class':responses.json()['predictions'][0]['class'],
                'confidence':responses.json()['predictions'][0]['confidence']*100}



    except Exception as e:
        raise  HTTPException(status_code=500,detail=str(e))
