import cv2
import matplotlib.pyplot as plt
import os

# Ruta relativa a la imagen
image_path = 'assets/images/JavaScript.png'

# Verificar que el archivo exista
if not os.path.exists(image_path):
    print(f"Error: el archivo no existe en la ruta '{image_path}'")
else:
    # Cargar la imagen
    img = cv2.imread(image_path)

    if img is None:
        print("Error: no se pudo cargar la imagen. Revisa la integridad del archivo.")
    else:
        # Mostrar imagen original
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title("Imagen Original")
        plt.axis('off')
        plt.show()

        # Convertir a escala de grises
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Mostrar imagen en escala de grises
        plt.imshow(gray_img, cmap='gray')
        plt.title("Imagen en Escala de Grises")
        plt.axis('off')
        plt.show()

        # Guardar imagen en escala de grises
        cv2.imwrite('assets/images/JavaScriptGray.png', gray_img)
        print("Imagen en escala de grises guardada como 'JavaScriptGray.png'.")

        blurred_img = cv2.GaussianBlur(img, (15,15),0)

        edges_img = cv2.Canny(gray_img, 100, 200)

        fig,axes = plt.subplots(1,3, figsize=(15,5))
        axes[0].imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        axes[0].set_title("Imagen Orignial")
        axes[0].axis('off')

        axes[1].imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
        axes[1].set_title("Imagen Desenfocada")
        axes[1].axis('off')

        axes[2].imshow(edges_img, cmap='gray')
        axes[2].set_title("Detección de Bordes (Canny)")
        axes[2].axis('off')

        plt.show()

        # Aplicar umbral simple
        _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
        # Aplicar umbral adaptativo
        adaptive_thresh_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        # Mostrar los resultados
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        axes[0].imshow(gray_img, cmap='gray')
        axes[0].set_title("Escala de Grises")
        axes[0].axis('off')
        axes[1].imshow(binary_img, cmap='gray')
        axes[1].set_title("Umbral Simple")
        axes[1].axis('off')
        axes[2].imshow(adaptive_thresh_img, cmap='gray')
        axes[2].set_title("Umbral Adaptativo")
        axes[2].axis('off')
        plt.show()


        # Detectar contornos
        contours, _ = cv2.findContours(edges_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Dibujar los contornos sobre la imagen original
        contour_img = img.copy()
        cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)
        # Mostrar los contornos sobre la imagen original
        plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
        plt.title("Detección de Contornos")
        plt.axis('off')
        plt.show()


        image_face = 'assets/images/WillSmith.png'
        img2 = cv2.imread(image_face)


        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Convertir la imagen a escala de grises
        gray_face_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # Detectar rostros
        faces = face_cascade.detectMultiScale(gray_face_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    
        # Dibujar rectángulos alrededor de los rostros detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)


        # Mostrar la imagen con los rostros detectados
        plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        plt.title("Detección de Rostros")
        plt.axis('off')
        plt.show()