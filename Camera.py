import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def Cam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        img = cv2.flip(img, 1)
        cv2.imshow(None, img)
        if cv2.waitKey(1) == 27: #Break loop with Esc
            break
    cv2.destroyAllWindows()
    
@app.route("/video_feed")
def video_feed():
    Cam()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)      
