import cv2
import tensorflow as tf
import numpy as np
model = tf.keras. models.load_model("keras_model.h5")
video = cv2.videoCapture(0)
while True:
    check, frame = video.read()
    image = cv2.resize(frame, (224, 224))
    numpyimg = np.array(image, dtype = np.float32)
    numpyimg = np.expand_dims(numpyimg, axis = 0)
    normalize = numpyimg/255.0
    prediction = model.predict(normalize)
    cv2.imshow("output", frame)
    abc = cv2.waitkey(3)
    if abc == 8:
        break
video.release()