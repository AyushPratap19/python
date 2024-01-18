from flask import Flask, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)

def detect_faces(image_data):
    try:
        # Convert base64 encoded image to NumPy array
        img_data = base64.b64decode(image_data)
        np_arr = np.frombuffer(img_data, dtype=np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Load OpenCV's pre-trained face detector (Haar Cascade)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Convert the image to grayscale for face detection
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw bounding boxes around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Convert the modified image back to base64
        _, buffer = cv2.imencode(".jpg", img)
        img_data = base64.b64encode(buffer).decode("utf-8")

        return img_data
    except Exception as e:
        print("Error:", e)
        return None

@app.route('/detect_faces', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        image_data = data['image']
        result = detect_faces(image_data)
        if result:
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Face detection failed."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
