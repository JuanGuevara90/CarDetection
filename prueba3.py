import cv2
cars_cascade = cv2.CascadeClassifier('cars.xml')

def detect_cars(gray,frame):

    cars = cars_cascade.detectMultiScale(gray, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 0, 255), thickness=2)
    cv2.imshow('frame', frame)

def Simulator():
    CarVideo = cv2.VideoCapture(0)
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        controlkey = cv2.waitKey(1)
        if ret:        
            cars_frame = detect_cars(gray,frame)
        else:
            break
        if controlkey == ord('q'):
            break

    CarVideo.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    Simulator()