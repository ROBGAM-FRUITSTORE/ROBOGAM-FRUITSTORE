import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the training model
modelo = load_model('MODELO/MODELO.h5')

# Names of the classes
diccionario_clases = {0:'AVOCADO',1: 'APPLE',2: 'PEACH',3: 'POMEGRANATE',4: 'GUAVA',5: 'MANGO',6:'ORANGE',7:'PEAR',8:'PITAHAYA',9:'TOMATO'}  # Actualiza esto según tus clases

# Preprocessing process
def predecir_fruta(frame):
    # Resize the image according to the model
    img = cv2.resize(frame, (100, 100))
    # Normalization
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  

    # Prediction
    prediccion = modelo.predict(img)
    clase_predicha = np.argmax(prediccion)

    # Result of the prediction
    return diccionario_clases[clase_predicha]

# REcording screen
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Make prediction based on what the camera is watching
    fruta_predicha = predecir_fruta(frame)

    # Show the prediction in the screen 
    cv2.putText(frame, fruta_predicha, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Predicción de Fruta', frame)

    # Broke code
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all the windows
cap.release()
cv2.destroyAllWindows()




