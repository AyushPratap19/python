import dlib
import cv2

def detect_face_and_eyes(image_path):
    """Detects faces and eyes in the given image."""
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("/Users/ayushpratapsingh/Desktop/ ayush.py/shape_predictor_68_face_landmarks.dat.bz2")

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Extract eye landmarks
        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

        # Draw rectangles around the eyes
        for i in range(6):
            cv2.line(image, left_eye[i], left_eye[i + 1], (0, 255, 0), 1)
            cv2.line(image, right_eye[i], right_eye[i + 1], (0, 255, 0), 1)
        cv2.line(image, left_eye[0], left_eye[5], (0, 255, 0), 1)
        cv2.line(image, right_eye[0], right_eye[5], (0, 255, 0), 1)

        # Draw rectangle around the face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Face and Eyes Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    detect_face_and_eyes(image_path)
