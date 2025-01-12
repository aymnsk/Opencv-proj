import cv2
import numpy as np

#yolo model load karna
# net = cv2.dnn.readNet('yolov4-tiny.weights','yolov4-tiny.cfg')
net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

#load ko class diye
with open('coco.names', 'r') as f:
    classes = f.read().strip().split('\n')

#network ko set karna hai
layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()] #linux kay liye h



#video ko capture kay liye
cap = cv2.VideoCapture(0,cv2.CAP_V4L2)

while True:
    ret ,frame = cap.read()
    if not ret:
        break
    height, width, channels = frame.shape

    #yolo model ka frame taiyar karege
    blob =cv2.dnn.blobFromImage(frame,0.00392,(416,416),swapRB=True ,crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    #detection ka proccessing dikhayega

    # for output in outputs:
    #     for detection in outputs:
    #         scores = detection[5:]
    #         class_id = np.argmax(scores)
    #         confidence = scores[class_id]  #debuggg
    for output in outputs:
        for detection in output:
        # Get the confidence score of the detection
            confidence = detection[4]
        if confidence > 0.5:  # Filter weak detections
            scores = detection[5:]
            class_id = np.argmax(scores)

            if confidence > 0.5:
                center_x = int(detection[0]* width)
                center_y = int(detection[1]* height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w /2)
                y = int(center_y - h/2)

                #box banana hai
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,f"{classes[class_id]}:{int(confidence*100)}%",(x,y - 10),cv2.Font_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)       

    cv2.imshow('ObjectDetection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
