# Emotion Detector - Watson NLP Web Application

Final Project for the IBM AI Engineering / Python & Flask Web Development course.

## Project Overview

This application is an AI-powered web service built with Python and Flask that analyzes text inputs to detect human emotions using the IBM Watson NLP library. It identifies the scores for **anger**, **disgust**, **fear**, **joy**, and **sadness**, and determines the **dominant emotion** in the provided statement.

## Features

- **Emotion Analysis**: Integrates Watson NLP Emotion Predict API to extract granular emotion scores.
- **Packaged Architecture**: Structured as a reusable Python package (`EmotionDetection`).
- **Unit Testing**: Includes automated unit tests (`test_emotion_detection.py`) verifying accuracy across multiple emotional states.
- **Web Interface**: Deployed locally via Flask (`server.py`) with interactive user input.
- **Error Handling**: Gracefully handles blank inputs and HTTP 400 status responses from the API.
- **Static Code Analysis**: Validated with `pylint` achieving a 10/10 score.

## Project Structure

```text
emotion-detection-ibm/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
