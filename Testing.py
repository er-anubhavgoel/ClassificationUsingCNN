import cv2
import tensorflow as tf

CATEGORIES = ["Metals","Plastics"]

def prepare(filepath):
    IMG_SIZE = 100
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  #Grayscale is used, so that R=G=B and reduce color feature
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE)) #Every image is converted to 100x100 standard dimension
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)     #(-1) is for self-evaluation (feature extraction) of image passed

model = tf.keras.models.load_model("MPmodel.h5")

prediction = model.predict([prepare('saved_img-final.jpg')])
print(CATEGORIES[int(prediction[0][0])])
