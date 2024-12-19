from flask import Flask, Response, redirect
import cv2

app = Flask(__name__)

# Initialize the camera (0 for the default camera)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET'])
def home():
    # Redirect the root URL to start-stream route
    return redirect('/start-stream')

@app.route('/start-stream', methods=['GET'])
def start_stream():
    # Automatically redirect to the video feed URL
    return redirect('/video_feed')

@app.route('/video_feed')
def video_feed():
    # Serve the live video feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
