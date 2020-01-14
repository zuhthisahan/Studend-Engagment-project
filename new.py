import numpy as np
import cv2
import plotly.graph_objects as go

MHI_DURATION = 10
DEFAULT_THRESHOLD = 30

video_src = '6.webm'
energy = []

cam = cv2.VideoCapture(video_src)
ret, frame = cam.read()
h, w = frame.shape[:2]
prev_frame = frame.copy()
motion_history = np.zeros((h, w), np.float32)
timestamp = 0

while True:

    # global energy
    ret, frame = cam.read()
    if not ret:
        break

    frame_diff = cv2.absdiff(frame, prev_frame)
    gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    ret, fgmask = cv2.threshold(gray_diff, DEFAULT_THRESHOLD, 1, cv2.THRESH_BINARY)
    timestamp += 1

    # update motion history
    cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, MHI_DURATION)

    # normalize motion history
    mh = np.uint8(np.clip((motion_history - (timestamp - MHI_DURATION)) / MHI_DURATION, 0, 1) * 255)
    # cv2.imshow('motempl', mh)
    prev_frame = frame.copy()

    # name = "frame%d.jpg" % timestamp
    # cv2.imwrite(name, mh)

    cv2.waitKey(27)

    mag = np.linalg.norm(mh)

    area = cv2.countNonZero(mh)

    calculated_energy = (mag / area)
    energy.append(calculated_energy)

    print(mag)

X = []
X.extend(range(4550))

print(X)
fig = go.Figure(data=go.Scatter(x=X, y=energy))
fig.show()
