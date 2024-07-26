import requests 
import json 

def emotion_detector(text_to_analyze):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  
    formatted_response = json.loads(response.text)
    if response.status_code == 200: 
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        score_dict = {'anger': anger_score,'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness':sadness_score}
        max_score = {'max':["",0]}
        for i in score_dict:
            if score_dict[i] >= max_score['max'][1]:
                max_score['max'][1] = score_dict[i]
                max_score.update({'max': [i,score_dict[i]]})    
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        max_score = {'max':[None,None]}
    return {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
        'sadness': sadness_score, 'dominant_emotion': max_score['max'][0]
        }

