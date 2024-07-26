'''
Module of server for Emotion Detector
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Function to send the text to Emotion Detector 
    '''
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, "
        f"the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    '''
    Function to render the index page 
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
