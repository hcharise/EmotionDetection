from deepface import DeepFace
from parse_emotion import *

def make_predictions(img, file):
    try:
        face_analysis = DeepFace.analyze(img)
        file.write(img)
        file.write(", " + face_analysis[0]['dominant_gender'])
        file.write(", " + face_analysis[0]['dominant_emotion'])
        file.write(", " + parse_emotion(img))
        file.write("\n")
    except:
        file.write(img)
        file.write(", COULD NOT DETECT FACE")
        file.write("\n")