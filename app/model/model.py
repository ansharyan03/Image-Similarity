import numpy as np

from keras.applications import Xception
from keras.applications.xception import preprocess_input

from keras.preprocessing import image
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

from io import BytesIO

def preprocess_image(img_path, target_size=(299, 299), methods={}):
    img = image.load_img(img_path, target_size=target_size)
    
    #
    if "gray" in methods:
        img = img.convert('L')
    if "rotate" in methods:
        img = img.rotate(methods["rotate"])
    #
    
    img_array = image.img_to_array(img)
    print(img_array.shape)
    # Expand dimensions to match the input shape (batch size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    # Preprocess the image for Xception
    return preprocess_input(img_array)

class SimilarityModel:
    def __init__(self):
        self.model = Xception(weights='imagenet', include_top=False, pooling='avg')
        self.inputs = []
    
    def add_input_file(self, path):
        img = preprocess_image(path)
        self.inputs.append(img)

    def add_input_PIL(self, img):
        img = Image.open(BytesIO(img)).resize((299, 299))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        self.inputs.append(preprocess_input(img_array))

    def add_input_raw(self, img):
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        self.inputs.append(preprocess_input(img_array))

    def get_similarity(self):
        features = []
        for i in range(len(self.inputs)):
            print(f"shape: {self.inputs[i].shape}")
            features.append(self.model.predict(self.inputs[i]))
        return float(cosine_similarity(features[0], features[1])[0][0])

    def extract_features(self, img):
        # Preprocess the image
        features = self.model.predict(img)
        return features