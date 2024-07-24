import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from .dict import return_disease, show, get_dict
import json

# Load the model architecture from JSON file
json_file = open(
    "/Users/arjun/Documents/KrishiSahay/python-whatsapp-bot/app/utils/model/new1model_architecture.json",
    "r",
)
loaded_model_json = json_file.read()
json_file.close()

# with open('model_architecture.json') as f:
#     # Load the JSON data
#     loaded_model_json = json.load(f)

model = model_from_json(loaded_model_json)

# Load the trained weights
model.load_weights(
    "/Users/arjun/Documents/KrishiSahay/python-whatsapp-bot/app/utils/model/new1model_weights.h5"
)


# Function to predict the class of an image
def predict_image_class(image_path):
    img = image.load_img(image_path, target_size=(160, 160))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image (if applicable)

    predictions = model.predict(img_array)

    class_idx = np.argmax(predictions[0])
    # Modify this logic based on how your classes are determined
    class_label = {
        "Downey Mildew": 0,
        #       "Healthy cucumberleaf": 1,
        "Pepper__bell___Bacterial_spot": 1,
        "Pepper__bell___healthy": 2,
        "Tomato__Tomato_YellowLeaf__Curl_Virus": 3,
        # "Tomato__Tomato_mosaic_virus": 5,
        "Tomato_healthy": 4,
    }
    disease_type = list(class_label.keys())[list(class_label.values()).index(class_idx)]

    # return disease_type

    if (
        disease_type == "Tomato_healthy"
        or disease_type == "Pepper__bell___healthy"
        or disease_type == "Healthy_cucumberleaf"
    ):
        print("Given plant is a healthy plant")
    else:
        output_dict = get_dict(disease_type)
        return output_dict


# Test the model on some images
# test_images = 'yellow.jpeg'

# predict_image_class("yellow.jpeg")

# if output == 'Tomato_healthy' or output == 'Pepper__bell___healthy' or output =='Healthy_cucumberleaf':
#     print("Given plant is a healthy plant")
# else:
#     output_dict = get_dict(output)
#     print(output_dict)
# return_disease(output_dict)
# print(output_dict)
