
        blurred_img = cv2.GaussianBlur(img, (15,15),0)

        edges_img = cv2.Canny(gray_img, 100, 200)
