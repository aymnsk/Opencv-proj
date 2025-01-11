import cv2
import numpy as np

def basic_image_operations():
    print("reading image.....")
    img = cv2.imread('image.jpg')
    if img is None:
        print("Error: Could not read the image. Using a blank image instead.")
        img = np.zeros((300,300,3),dtype=np.uint8)
    print(f"image dimensions: {img.shape}")
    print(f"image data type: {img.dtype}")

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(img,(7,7),0)

    edges = cv2.Canny(gray,100,200)

    resized = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

    cv2.imshow("original",img)
    cv2.imshow("gray",gray)
    cv2.imshow("blur",blurred)
    cv2.imshow("edge",edges)
    cv2.imshow("resize",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawing_shapes():
    canvas = np.zeros((400,600,3),dtype=np.uint8)

    cv2.rectangle(canvas,(100,100), (300,200),(0,255,0),(2))

    cv2.circle(canvas,(400,200),50,(0,0,255),-1)

    cv2.line(canvas,(0.300),(600,300),(255,0,0),3)

    cv2.putText(canvas,'OpenCV Basics',(150,350),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('DrawingDemo',canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def webcam_demo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        edges_frame = cv2.Canny(frame, 100, 200)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()
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

if __name__ == '__main__':
    main()