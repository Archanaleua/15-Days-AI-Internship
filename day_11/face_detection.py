import cv2

# Load the face detection model (built into OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

print("✅ Webcam opened! Press 'S' to save image, Press 'Q' to quit")

import os
count = len([f for f in os.listdir('.') if f.startswith('face_')])

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Cannot open webcam!")
        break
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected!", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Show face count
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Show the frame
    cv2.imshow("Face Detection - Day 11", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    # Press S to save
    if key == ord('s'):
        count += 1
        filename = f"face_{count}.png"
        cv2.imwrite(filename, frame)
        print(f"✅ Image saved: {filename}")
    
    # Press Q to quit
    if key == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()
print("✅ Done!")