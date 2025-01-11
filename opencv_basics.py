import cv2
import numpy as np

# Function 1: Basic Image Operations
def basic_image_operations():
    print("Reading image...")
    img = cv2.imread('image.jpg')
    
    if img is None:
        print("Error: Could not read the image. Using a blank image instead.")
        img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    print(f"Image Dimensions: {img.shape}")
    print(f"Image Data Type: {img.dtype}")

    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian blur
    blurred = cv2.GaussianBlur(img, (7, 7), 0)

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Resizing the image
    resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # Displaying the images
    cv2.imshow("Original", img)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Blurred", blurred)
    cv2.imshow("Edges", edges)
    cv2.imshow("Resized", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function 2: Drawing Shapes
def drawing_shapes():
    # Creating a blank canvas
    canvas = np.zeros((400, 600, 3), dtype=np.uint8)

    # Drawing a rectangle
    cv2.rectangle(canvas, (100, 100), (300, 200), (0, 255, 0), 2)

    # Drawing a circle
    cv2.circle(canvas, (400, 200), 50, (0, 0, 255), -1)

    # Drawing a line
    cv2.line(canvas, (0, 300), (600, 300), (255, 0, 0), 3)

    # Adding text
    cv2.putText(canvas, 'OpenCV Basics', (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Displaying the canvas
    cv2.imshow("Drawing Demo", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function 3: Webcam Demo
def webcam_demo():
    # Using Video4Linux backend for compatibility on Linux
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")
            break

        # Converting to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Applying edge detection
        edges_frame = cv2.Canny(frame, 100, 200)

        # Displaying the webcam feed with edge detection
        cv2.imshow("Webcam - Original", frame)
        cv2.imshow("Webcam - Edges", edges_frame)

        # Breaking the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main Function
def main():
    while True:
        print("\nOpenCV Basic Demo")
        print("1. Basic Image Operations")
        print("2. Drawing Shapes")
        print("3. Webcam Demo")
        print("4. Exit")

        choice = input("Enter Your Choice (1-4): ")

        if choice == '1':
            basic_image_operations()
        elif choice == '2':
            drawing_shapes()
        elif choice == '3':
            webcam_demo()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point
if __name__ == '__main__':
    main()
