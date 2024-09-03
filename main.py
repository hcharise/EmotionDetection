#################################################################
#
#  Emotion Detection
#  by Hannah Ashton
#  Syracuse University
#  CIS 663 Biometrics
#  Professor Gregory Wagner
#  July 2024 Term
#
#  This program was designed and utilized for research
#  published in the paper "An Analysis of Gender Biases in
#  Emotion Recognition Software Performance." The program
#  iterates through a folder of images and utilizes DeepFace to
#  detect the gender and emotion of the face in each image. The
#  program then writes these predictions, as well as the actual
#  emotion from the image (as indicated by the file name) into a
#  results.txt file for further processing.
#
#################################################################


import glob
from make_predictions import *

#################################################################
# PREDICTIONS
#################################################################

# Open file for storing predictions
predictions = open("predictions.txt", "w")

# Open folder containing images
path = glob.glob("Images/*.jpg")

# Iterate through images, detecting face and predicting gender and dominant emotion
for img in path:
    make_predictions(img, predictions)

# Close predictions file
predictions.close()

#################################################################
# RESULTS
#################################################################

false = 0
true = 0
undetectable = 0

# Reopen files for reading predictions and writing results
predictions = open("predictions.txt", "r")
results = open("results.txt", "w")

# Print header into results file
results.write("RESULTS\n\n")
results.write("Image Name, Pred Gender, Pred Emotion, Real Emotion, True/False/Unpredictable\n")

# Iterate through predictions file, copying data and true/false to results file
for line in predictions:

    # Copy line from predictions, minus '\n'
    results.write(line.strip())

    # Split predictions line by comma
    info = line.split(",")

    # Check for undetectable images, end loop iteration
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

# Close both files
predictions.close()
results.close()
