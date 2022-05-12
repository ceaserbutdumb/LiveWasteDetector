from cProfile import run
import cv2

def detect(vid):
  """
  Detect if there is trash in the video
  """

  # test for image
  if vid:
    img = get_image(vid)
    return predict(img)


  return {"class": "not recognised", "probibility": 0}

def get_image(vid):
  """
  Get an image from the video and return as a cv image
  """

  # to get video capture from a cctv run
  # cv2.VideoCapture(url)

  img = cv2.imread(vid, cv2.IMREAD_COLOR)

  return img


def predict(img):
  """
  Run the model
  """

  return {"class": "trash", "probibility": 0.7}
