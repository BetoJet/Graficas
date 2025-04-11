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
