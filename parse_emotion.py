
def parse_emotion(image_path):
    # print out the true emotion and check if correct or not
    if image_path.find("angry") != -1:
        emotion = "angry"
    elif image_path.find("disgust") != -1:
        emotion = "disgust"
    elif image_path.find("fear") != -1:
        emotion = "fear"
    elif image_path.find("neutral") != -1:
        emotion = "neutral"
    elif image_path.find("sad") != -1:
        emotion = "sad"
    elif image_path.find("surprise") != -1:
        emotion = "surprise"
    elif image_path.find("happy") != -1:
        emotion = "happy"

    return emotion