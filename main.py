from deepface import DeepFace
import glob

# Open file for results
predictions = open("predictions.txt", "w")

# Open folder containing images
path = glob.glob("Images2/*.jpg")

# Iterate through images, detecting face and predicting gender and dominant emotion
for img in path:

    try:
        face_analysis = DeepFace.analyze(img)
        predictions.write(img)
        predictions.write(", " + face_analysis[0]['dominant_gender'])
        predictions.write(", " + face_analysis[0]['dominant_emotion'])
        predictions.write("\n")
    except:
        predictions.write(img)
        predictions.write(", COULD NOT DETECT FACE")
        predictions.write("\n")

# Close file for just writing
predictions.close()