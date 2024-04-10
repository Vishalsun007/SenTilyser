# SenTilyser - Tamil Sentiment Analyser

SenTilyser is a deep learning project aimed at sentiment analysis in Tamil audio files. It utilizes Convolutional Neural Networks (CNNs) to identify and analyze emotions expressed in spoken Tamil language. The project provides a comprehensive solution for sentiment analysis, with a user-friendly Django web application interface.

## Features
- Deep learning model for sentiment analysis in Tamil audio files.
- Web application interface for uploading audio files.
- Integration with Google Speech Recognition for audio-to-text conversion.
- Preprocessing of text data, including stemming and vectorization.
- Evaluation of model performance through experiments and metrics.
- Future work includes direct audio analysis, alternative deep learning architectures, multilingual support, real-time analysis, user interface enhancements, and ethical considerations.

## Requirements
- Python 3.x
- Django
- TensorFlow
- SpeechRecognition
- NLTK

## Installation
1. Clone the repository:

```bash
git clone https://github.com/william-renaldy/SenTilyser.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the Django server:

```bash
python manage.py runserver
```

5. Access the web application at http://localhost:8000/

## Usage
1. Upload a Tamil audio file using the provided interface.
2. Wait for the audio file to be processed.
3. View the sentiment analysis results.
