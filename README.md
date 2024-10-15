# Python-Screen-Recorder

This project builds a simple screen recorder using Python. The program continuously captures the screen at regular intervals and compiles the images into a video file, which is saved in `.avi` format.

## Features:
- Records your screen at a resolution of **1920x1080** (customizable based on screen size).
- Saves the screen recording as a **.avi** video file.
- The frame rate is set to **20 frames per second** by default.
- Automatically stops recording after **10 seconds** (this can be customized).
- Allows you to stop recording early by pressing the **`q`** key.

## Requirements:
- **Python 3.x**
- Python libraries:
  - **pyautogui**
  - **opencv-python**
  - **numpy**

You can install the required libraries using the following command:
```bash
pip install pyautogui opencv-python numpy
