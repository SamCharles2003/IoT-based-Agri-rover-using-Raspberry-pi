import cv2
from flask import Flask, request
import numpy as np
import cvzone.ClassificationModule
from cvzone import ClassificationModule

myClassifier = cvzone.ClassificationModule.Classifier(r"C:\Users\sam charles\Documents\Plant Disease Detection\keras_model.h5",r"C:\Users\sam charles\Documents\Plant Disease Detection\labels.txt"
                                                                                                                               r"")

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def image():
    try:
        uploaded_file = request.files['file']
        nparr = np.frombuffer(uploaded_file.read(), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        prediction, index = myClassifier.getPrediction(image, scale=1)

        return str(index), 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)
