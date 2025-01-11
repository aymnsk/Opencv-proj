import cv2

# Use V4L2 backend to ensure compatibility on Linux
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't read frame")
        break

    # Apply filters
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        # Grayscale filter
    blur_frame = cv2.GaussianBlur(frame, (15, 15), 0)           # Blur filter
    edges_frame = cv2.Canny(frame, 100, 200)                    # Edge detection

    # Display the original and filtered frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Grayscale Frame', gray_frame)
    cv2.imshow('Blurred Frame', blur_frame)
    cv2.imshow('Edges Frame', edges_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
