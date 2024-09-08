# gestureMouse 🖱️👋

**gestureMouse** is a computer interaction tool that allows users to control their cursor using hand gestures detected via a webcam. It uses OpenCV and MediaPipe for hand tracking and PyAutoGUI for cursor movement and click detection, providing an intuitive and contact-free user experience. 🖥️👐

## 🚀 Features
- 🖱️ **Cursor Control with Hand Gestures**: Move the cursor by simply pointing with your hand.
- 👆 **Left Click Detection**: Simulates a left click when the index finger and thumb are close together.
- 👉 **Right Click Detection**: Simulates a right click when the thumb and middle finger come together.
- 📸 **Webcam-based Detection**: Real-time hand tracking using your webcam.
- ❌ **Exit Command**: Press the "Esc" key to stop the program.

## 📋 Requirements
- Python 3.x 🐍
- OpenCV library 📦
- MediaPipe library 📦
- PyAutoGUI library 📦

## 🔧 Setup:
1. Clone the repository and navigate to the folder:
   - ```git clone https://github.com/sabilashang/gestureMouse.git```
   - ```cd gestureMouse```
2. Create and Activate a Virtual Environment:
   - ```python -m venv .venv```
   - ```venv\Scripts\activate``` (Windows)
   - ```source .venv/bin/activate``` (macOS/Linux)
3. Install Required Packages:
   - ```pip install -r requirements.txt```

## 🖥️ Usage:
1. **Run the Script**: ```python gestureMouse.py```
2. **Use the following actions**:
   - **Move Cursor**: Move your hand in front of the webcam, and the cursor will follow the movement of your index finger.
   - **Left Click**: Bring your thumb and index finger close together to simulate a left click.
   - **Right Click**: Bring your thumb and middle finger close together to simulate a right click.
   - **Exit**: Press the "Esc" key to terminate the program.

> **Note**: The accuracy of cursor control and click detection depends on lighting conditions and the quality of the webcam.

## 📝 Example Usage
   - Move your index finger to control the cursor. To left-click, bring your thumb and index finger together. For a right-click, bring your middle finger and thumb together.

## ⚠️ License:
This project is under No License: This code is for personal use only. Copying, modifying, or using this code for academic, commercial, or other purposes is not permitted. Feel free to reach out if you require permission to reuse.

## 📫 Contact:
Feel free to reach out if you have any questions!
**Instagram**: [@sabilashan_g](https://www.instagram.com/sabilashan_g/)
