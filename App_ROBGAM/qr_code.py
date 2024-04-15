############ CREATE QR CODE #############


import qrcode
from PIL import Image

img = qrcode.make("leave_robgam")
img.save("qr_leave_cart.png")


############ DECODE QR CODE ##############
import cv2
from pyzbar.pyzbar import decode

def verificar_acceso(decoded_info):
    print(decoded_info)
    '''if decoded_info == "Access_robgam":
        print("Acceso permitido!", decoded_info)
    else:
        print("Acceso denegado")'''

def leer_qr_desde_camara():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar el video.")
            break

        decoded_objects = decode(frame)
        if decoded_objects:
            for obj in decoded_objects:
                if obj.type == 'QRCODE':
                    decoded_info = obj.data.decode('utf-8')
                    verificar_acceso(decoded_info)

        cv2.imshow('frame', frame)
        
        # Esperar la tecla 'Esc' para salir del bucle
        key = cv2.waitKey(1)
        if key == 27:  # 27 corresponde a la tecla 'Esc'
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    leer_qr_desde_camara()