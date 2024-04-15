import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inicializa la aplicación de Firebase con tus credenciales
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://smartstore-1b843-default-rtdb.firebaseio.com/"
})

# Referencia a la base de datos de Firebase
ref = db.reference('ROBGAM')  # Apunta al nodo raíz 'ROBGAM'

# Función para enviar los datos a Firebase para un usuario específico
def send_data_to_firebase(user_id, fruit_data):
    ref.child(user_id).child("Items").set(fruit_data)

# ID de usuario (debe ser proporcionado)
user_id = "ym4K3HWSEqcOw9bidnB5NHzI2MJ3"

# Datos de frutas que deseas enviar a Firebase
fruit_data = {
    "apple": 0,
    "pear": 0,
    "mango": 0,
    "orange": 0,
    "peach": 0,
    "pitahaya": 0,
    "guava": 0,
    "tomato": 0,
    "avocado": 0,
    "pomegranate": 0,
    "Total": 0.00
}

# Llama a la función para enviar datos a Firebase
send_data_to_firebase(user_id, fruit_data)

