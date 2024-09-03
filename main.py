from deepface import DeepFace
from parse_emotion import *
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
        predictions.write(", " + parse_emotion(img))
        predictions.write("\n")
    except:
        predictions.write(img)
        predictions.write(", COULD NOT DETECT FACE")
        predictions.write("\n")

# Close file for just writing
predictions.close()

##############################
#  performance calculations  #
##############################
false = 0
true = 0
undetectable = 0

# Reopen file for reading and writing
predictions = open("predictions.txt", "r")
results = open("results.txt", "w")

# Print headers
results.write("RESULTS\n\n")
results.write("Image Name, Pred Gender, Pred Emotion, Real Emotion, True/False/Unpredictable\n")

for line in predictions:

    results.write(line.strip())

    # Split each line by comma
    info = line.split(",")

    # Check for undetectables
    if info[1] == ' COULD NOT DETECT FACE\n':
        undetectable = undetectable + 1
        results.write(", Undetectable = %d\n" % undetectable)
        continue

    # Parse emotion data if face was detectable
    pred_emotion = info[2].strip()
    real_emotion = info[3].strip()

    # Check if emotion prediction is correct or not
    if (pred_emotion == real_emotion):
        true = true + 1
        results.write(", True = %d\n" % true)
    else:
        false = false + 1
        results.write(", False = %d\n" % false)

print("\n** TOTAL TRUE = " + str(true / (true + false + undetectable)) + " **")
print("** TOTAL FALSE = " + str(false / (true + false + undetectable)) + " **")
print("** TOTAL UNDETECTABLE = " + str(undetectable / (true + false + undetectable)) + " **")

