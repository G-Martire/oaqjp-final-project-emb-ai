"""Flask web server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

APP = Flask("Emotion Detector")


@APP.route("/emotionAnalyzer")
def emotion_analyzer():
    """Analyze emotion from the query string parameter textToAnalyze."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


@APP.route("/")
def render_index():
    """Render the main HTML interface."""
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)