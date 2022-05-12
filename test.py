import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

def predict(img_path):
     labels={0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

     img = image.load_img(img_path, target_size=(300, 300))
     img = image.img_to_array(img, dtype=np.uint8)
     img=np.array(img)/255.0
     
     model = tf.keras.models.load_model(r"C:\Users\Prangal pandey\Downloads\trained_model.h5")
     p=model.predict(img[np.newaxis, ...])
     pro=np.max(p[0], axis=-1)
     predicted_class = labels[np.argmax(p[0], axis=-1)]
    #  os.remove(img_path)
     return(str(predicted_class)+"\nProbability:"+str(pro*100)+"%")

# def camera():


print(predict(r"C:\Users\Prangal pandey\Downloads\WhatsApp Image 2022-05-05 at 10.47.03 AM.jpeg"))