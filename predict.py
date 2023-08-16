
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os



#model = os.chdir("EfficientNetB0_TL_Model.h5")
loaded_model = load_model('model_snapshot_5.h5')    # load the previouly saved model

def predict_result(full_path):
    img = image.load_img(full_path, target_size = (135, 135, 3))
    img = np.expand_dims(img, axis=0)
    img = img.astype('float')/255

    result = loaded_model.predict(img)
    result = result.item()

    if result > 0.5:
        return round(result*100, 2), 'Parasitized'
    else:
        return round((1-result)*100, 2), 'Unparasitized'
