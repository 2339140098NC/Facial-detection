Face Detection in Video using OpenCV
====================================

This project uses OpenCV's Haar Cascade classifier to detect faces in each frame of a video file and display the results in real time.

Project Structure
-----------------
```
face-detection-video/
├── 06facial_detection.py      # Main Python script
├── README.txt                 # This file
└── haarcascades/              # Directory for Haar Cascade XML files (optional)
    └── haarcascade_frontalface_alt2.xml
```
Features
--------
- Face detection using Haar Cascade classifier
- Processes a video file frame-by-frame
- Displays video with rectangles drawn around detected faces
- Option to quit by pressing 'q'

Requirements
------------
- Python 3.x
- OpenCV (cv2)

You can install OpenCV using:

    pip install opencv-python

Usage
-----
1. Make sure you have the Haar Cascade XML file.
   You can download it from https://github.com/opencv/opencv/tree/master/data/haarcascades
   or use the path where OpenCV provides it.

2. Place your video file in an accessible location.

3. Run the script:

    python face_detection.py

4. Update the code to point to your video file:

    cap = cv.VideoCapture('path_to_your_video.mp4')

5. Press 'q' while the video is playing to exit.

Example
-------
![project1](https://github.com/user-attachments/assets/a2c36f3b-c452-4ec5-88e3-609389a603e8)


Notes
-----
- Detection works best with good lighting and clear frontal faces.
- The current code loads the cascade file on every frame — for efficiency, you can load it once outside the detection loop.

License
-------
This project is licensed under the MIT License.
