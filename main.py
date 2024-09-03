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

##############################
#  performance calculations  #
##############################
false = 0
true = 0
undetectable = 0

# Reopen file for reading and writing
predictions = open("predictions.txt", "r")
results = open("results.txt", "w")

for line in predictions:

    results.write(line.strip())

    #Split each line into file name and gender
    info = line.split(",")

    # Check for undetectables
    if info[1] == ' COULD NOT DETECT FACE\n':
        undetectable = undetectable + 1
        results.write(", Undetectable = %d\n" % undetectable)
        continue

    image_path = info[0]
    image_gender = info[1]
    image_emotion = info[2].strip()

    #print out the true emotion

    if image_emotion == "angry" and image_path.find("angry") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "disgust" and image_path.find("disgust") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "fear" and image_path.find("fear") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "neutral" and image_path.find("neutral") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "sad" and image_path.find("sad") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "surprise" and image_path.find("surprise") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    elif image_emotion == "happy" and image_path.find("happy") == -1:
        false = false + 1
        results.write(", False = %d\n" % false)
        continue
    else:
        true = true + 1
        results.write(", True = %d\n" % true)

print("\n** TOTAL TRUE = " + str(true / (true + false + undetectable)) + " **")
print("** TOTAL FALSE = " + str(false / (true + false + undetectable)) + " **")
print("** TOTAL UNDETECTABLE = " + str(undetectable / (true + false + undetectable)) + " **")

