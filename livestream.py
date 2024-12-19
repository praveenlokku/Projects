import cv2

capture = cv2.VideoCapture("https://10.12.106.113:8080/video")

while(True):
    _, frame =capture.read()
    cv2.imshow("livestream", frame)

    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()