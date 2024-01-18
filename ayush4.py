import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from imutils import face_utils

def eye_aspect_ratio(eye):
    # Compute the euclidean distances between the two sets of vertical eye landmarks
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])

    # Compute the euclidean distance between the horizontal eye landmark
    C = distance.euclidean(eye[0], eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

# Constants for eye blink detection
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

# Initialize the dlib face detector and create facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("path/to/shape_predictor_68_face_landmarks.dat")

# Start video capture from the default camera
video_capture = cv2.VideoCapture(0)

# Initialize counters for blinking
blink_counter = 0
total_blinks = 0

while True:
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray, 0)

    for face in faces:
        # Get the facial landmarks
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # Extract the eye coordinates
        left_eye = shape[42:48]
        right_eye = shape[36:42]

        # Calculate the eye aspect ratio for each eye
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the eye aspect ratio for both eyes
        ear = (left_ear + right_ear) / 2.0

        # Check for eye blink
        if ear < EYE_AR_THRESH:
            blink_counter += 1
        else:
            if blink_counter >= EYE_AR_CONSEC_FRAMES:
                total_blinks += 1
            blink_counter = 0

        # Draw the eye landmarks on the frame for visualization
        for (x, y) in left_eye:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
        for (x, y) in right_eye:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Check if the number of blinks is sufficient for verification
if total_blinks >= 3:
    print("Human verified.")
else:
    print("Verification failed.")
