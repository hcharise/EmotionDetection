from deepface import DeepFace
from parse_emotion import *

# Function to attempt deepface analysis and print results if successful, error message if not
def make_predictions(img, file):
    try:
        # Detect face and recognize emotion/gender
        face_analysis = DeepFace.analyze(img)

        # Write results
        file.write(img)
        file.write("," + face_analysis[0]['dominant_gender'])
        file.write("," + face_analysis[0]['dominant_emotion'])
        file.write("," + parse_emotion(img))
        file.write("\n")

    except:
        # If unable to detect face, write error message
        file.write(img)
        file.write(",ERROR")
        file.write(",ERROR")
        file.write("," + parse_emotion(img))
        file.write("\n")