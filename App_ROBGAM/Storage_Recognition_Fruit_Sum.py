import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import numpy as np
import face_recognition
from firebase_admin import db


class SimpleFaceRecognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_resizing = 0.25
        self.initialized_fruit_data = False

    def load_encoding_images(self, bucket_name):
        """
        Load encoding images from Firebase Storage. Each subdirectory represents a person
        and contains images of that person.
        :param bucket_name: The name of the Firebase Storage bucket.
        """
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://smartstore-1b843-default-rtdb.firebaseio.com/",
            'storageBucket': bucket_name
        })
        bucket = storage.bucket()
        
        blobs = bucket.list_blobs()
        for blob in blobs:
            # Assuming the blob name is in the format 'users/{id}/filename.ext'
            blob_name_parts = blob.name.split('/')
            if len(blob_name_parts) >= 2:
                person_name = blob_name_parts[1]  # ID of the person
                img_data = blob.download_as_bytes()

                # Check if the image data is empty or corrupted
                if img_data is None or len(img_data) == 0:
                    print(f"Empty or corrupted image data for {blob.name}")
                    continue

                img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
                if img is None:
                    print(f"Failed to decode image for {blob.name}")
                    continue

                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                try:
                    img_encoding = face_recognition.face_encodings(rgb_img)[0]
                    self.known_face_encodings.append(img_encoding)
                    self.known_face_names.append(person_name)
                except IndexError:
                    print(f"No face found in the image {blob.name}")

        print("Encoding images loaded")


    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        detected_name = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            detected_name.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), detected_name


    def update_fruit_count(self, detected_names, e_fruit):
        fruit_price_list = {
            "apple": 5,
            "avocado": 8,
            "guava": 5,
            "mango": 6,
            "orange": 5,
            
            "peach": 8,
            "pear": 5,
            "pitahaya": 8,
            "pomegranate": 6,
            "tomato": 4,
        }

        if self.initialized_fruit_data == False:
            # Solo reiniciar los valores de frutas a 0 en Firebase si no se ha hecho antes
            ref = db.reference('ROBGAM')  # Apunta al nodo raíz 'ROBGAM'

            fruit_data = {
                "apple": 0,
                "avocado": 0,
                "guava": 0,
                "mango": 0,
                "orange": 0,
                "peach": 0,
                "pear": 0,
                "pitahaya": 0,
                "pomegranate": 0,
                "tomato": 0,
                "Total": 0.00
            }

            for detected_name in detected_names:
                if detected_name:
                    detected_name_ref = ref.child(detected_name).child('Items')
                    for fruit, count in fruit_data.items():
                        fruit_ref = detected_name_ref.child(fruit)
                        fruit_ref.set(0)
                        self.initialized_fruit_data = True  # Establecer la bandera a True para indicar que los datos se han inicializado

        # Actualizar la cantidad de frutas si se detecta un nombre y se ingresa una fruta por la terminal
        ref = db.reference('ROBGAM')  # Apunta al nodo raíz 'ROBGAM'
        for detected_name in detected_names:
            if detected_name:
                if e_fruit:
                    detected_name_ref = ref.child(detected_name).child('Items')
                    fruit_ref = detected_name_ref.child(e_fruit)
                    fruit_ref.transaction(lambda current_value: (current_value or 0) + 1)
                    fruit_price = fruit_price_list.get(e_fruit)
                    total_ref = detected_name_ref.child("Total")
                    total_ref.transaction(lambda current_value: (current_value or 0) + fruit_price)
                    print("Cantidad de frutas actualizada")

#####################
    
# Crear una instancia de SimpleFaceRecognition
sfr = SimpleFaceRecognition()

# Cargar las imágenes de codificación
sfr.load_encoding_images("smartstore-1b843.appspot.com")

# Cargar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, detected_name = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, detected_name):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    if detected_name:
        e_fruit = input("Enter fruit name: ")
        if e_fruit in {"apple", "avocado", "guava", "mango", "orange", "peach", "pear", "pomegranate", "pitahaya", "tomato", "Total"}:
            sfr.update_fruit_count(detected_name, e_fruit)
        else:
            print("No fruit")
    # Actualizar la cantidad de manzanas si se detecta un nombre
    #sfr.update_fruit_count(detected_name, e_fruit)

    # Mostrar el fotograma resultante
    cv2.imshow("Frame", frame)

    # Romper el bucle cuando el usuario presione 'ESC'
    key = cv2.waitKey(1)
    if key == 27:
        break

# Liberar la captura y destruir todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()
