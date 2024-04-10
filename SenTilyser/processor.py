import pickle
import nltk
import re
import numpy as np
import tensorflow as tf
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from keras.models import load_model
import speech_recognition as sr 
import Py_Thanglish as p

try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")


class Processor():
    def __init__(self):
        self.ps = PorterStemmer()
        self.recognizer = sr.Recognizer()

        with open("vectorizer.pkl","rb") as f:
            self.Tfidf = pickle.load(f)

        with open("encoder.pkl","rb") as f:
            self.OneHotEncoder = pickle.load(f)

        self.corpus = []

        self.X = None


    def audio_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source)

            print("Converting audio to text...")

            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio, language="ta-IN")  # "ta-IN" for Tamil
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition; {0}".format(e))


    def pre_process(self, audio):

        self.corpus = []

        for i in range(len(audio)):

            ta_data = self.audio_to_text(audio[i])

            with open("tamilData.txt","w", encoding="utf-8") as f:
                f.write(ta_data)

            data = p.tamil_to_thanglish(ta_data)

            review = re.sub("[^a-zA-Z]"," ",data)

            review = review.lower().split()

            review = [self.ps.stem(r) for r in review if r not in stopwords.words("english")]

            review = " ".join(review)

            self.corpus.append(review)

        self.X = self.Tfidf.transform(self.corpus).toarray()

        return self.X
    

    def post_process(self, res):

        max_values = np.max(res, axis=1)

        # Create an array to store the row indices of the maximum values
        max_indices = np.argmax(res, axis=1)

        # Create an array of zeros with the same shape as the nested array
        keras_y_pred = np.zeros_like(res)

        # Set the maximum values to their indices and all other values to zero
        keras_y_pred[np.arange(len(res)), max_indices] = 1
        keras_y_pred = keras_y_pred.astype(int)

        return self.OneHotEncoder.inverse_transform(keras_y_pred).ravel()


        




class Model():
    def __init__(self):
        self.model = load_model("cnn-model1")

    
    def load_model(self):
        return self.model



    def predict(self,X):

        res = self.model.predict(X)

        return res




if __name__ == "__main__":
    message = r"C:\Users\willi\Downloads\Tamil Dialogue.wav"
    #yenakku naan poataa nee yaentaa ippati panra ippati yellaam pannaathataa

    processor = Processor()
    X = processor.pre_process([message,message])

    model = Model()


    res = model.predict(X)
    print(res)

    print(processor.post_process(res))