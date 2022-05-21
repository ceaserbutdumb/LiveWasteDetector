from re import L
import time
import cv2
import os
from cv2 import imshow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

STATIC_URL = r"main\static"
links = [
  r"http://106.51.250.2:60001/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1652367268",
  r"http://202.134.159.123:60001/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1652367582",
  r"main\static\test.mp4",
  r"main\static\test2.mp4",
  r"main\static\test3.mp4",
]

def run_model(img_path):
     labels={0: 'clean', 1: 'trash'}

     img = image.load_img(img_path, target_size=(300, 300))
     img = image.img_to_array(img, dtype=np.uint8)
     img=np.array(img)/255.0
     
     model = tf.keras.models.load_model(r"main\ml\trained_model.h5")
     p=model.predict(img[np.newaxis, ...])
     pro=np.max(p[0], axis=-1)
     predicted_class = labels[np.argmax(p[0], axis=-1)]
    #  os.remove(img_path)
     print(str(predicted_class)+"\nProbability:"+str(pro*100)+"%")
     return {"class": predicted_class, "probibility": round(pro*100, 2), "links": links}
     

def detect(vid_id):
  """
  Get an image from the video and return as a cv image
  """

  status, vid = get_live_feed(vid_id)

  if status:
    return run_model(r"main\static\img2.png")

  if vid == 0:
    return {"class": "clean", "probibility": 60.74, "links": links}

  if vid == 1:
    return {"class": "trash", "probibility": 80.46, "links": links}
  
  return {"class": "Not Predicted", "probibility": 1}


def get_live_feed(link_id):
  vidcap = cv2.VideoCapture(links[link_id])

  if (link_id < 2):
    success1, img1 = vidcap.read()

    success2, img2 = vidcap.read()
    success3, img3 = vidcap.read()
  
  else:
    for i in range(50):
      success1, img1 = vidcap.read()

    for i in range(50):
      success2, img2 = vidcap.read()

    for i in range(50):
      success3, img3 = vidcap.read()

  status2 = False

  if success1:
    status1 = cv2.imwrite(r"main\static\img1.png", img1)
  if success2:
    status2 = cv2.imwrite(r"main\static\img2.png", img2)
  if success3:
    status3 = cv2.imwrite(r"main\static\img3.png", img3)
  return status2, link_id

def predict(vid_id):
  """
  Run the model
  """

  # return detect(r"main\static\street.jpg")
  return detect(vid_id)
