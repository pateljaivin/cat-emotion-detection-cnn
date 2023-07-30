import os
import cv2

def crop_image(original_input_image_path):
    try:
        img = cv2.imread(original_input_image_path)
        input_image_path = original_input_image_path[:-4]
        
        # create a new directory to store cropped images
        output_dir = 'cropped_images'
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        
        # create output image path in the new directory
        output_image_path = os.path.join(output_dir, os.path.basename(input_image_path)) + "_cropped.jpg"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier('cat_hascade.xml')

        # Detect faces
        scaleFactor = 1.1
        minNeighbors = 4
        minSize = (int(gray.shape[0]*0.05),
                   int(gray.shape[1]*0.05)) 
        maxSize = (int(gray.shape[0]*2.2), int(gray.shape[1]*2.2))
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor, minNeighbors, 0, minSize, maxSize)
        print(len(faces))
        # Draw rectangle around the faces and crop the faces
        for (x, y, w, h) in faces:
            x = int(x - 0.30*w)  # to adjust left region of face
            y = int(y - 0.35*h)  # to adjust top region of face
            w = int(1.5*w)  # to adjust top region of face
            h = int(1.5*h)  # to adjust bottom region of face
            
            # Ensure that the face detection rectangle is within the bounds of the image
            if x < 0:
              x = 0
            if y < 0:
              y = 0
            if x + w > img.shape[1]:
                 w = img.shape[1] - x
            if y + h > img.shape[0]:
                 h = img.shape[0] - y

            cropped_face = img[y:y + h, x:x + w]
            cropped_face = cv2.resize(cropped_face, (256, 256), interpolation=cv2.INTER_AREA)
            cv2.imwrite(output_image_path, cropped_face,[cv2.IMWRITE_JPEG_QUALITY, 100])
            # faces = cv2.resize(faces, (256, 256))
            # cv2.imwrite(output_image_path, faces)
        return output_image_path 
    except Exception as e:
        print(e)
# crop_image("cat-pet-animal-domestic-104827.jpeg")