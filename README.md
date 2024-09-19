# Color Detection with OpenCV and PIL

## 📝 Overview
This **Color Detection** project uses **OpenCV** and **PIL** to identify and track specific colors (yellow, red, blue, and green) in real-time using a webcam feed. The system converts the webcam feed to HSV color space and detects colors based on predefined ranges. When a color is detected, the project highlights the object on the screen and labels it.

## ✨ Features
- 🎥 **Real-time Color Detection**: Detect and highlight objects based on their color in the webcam feed.
- 📊 **Multiple Colors**: The system is configured to detect four colors: **Yellow**, **Red**, **Blue**, and **Green**.
- 🔍 **Dynamic Bounding Box**: A bounding box is drawn around the detected color, and the object is labeled accordingly.
- 🎨 **Adjustable Color Ranges**: The HSV limits for each color can be customized for fine-tuning color detection.

## 📋 Requirements
- 🐍 **Python 3.x**
- 👁️ **OpenCV 4.8.0.74**
- 🖼️ **Pillow (PIL) 9.3.0**
- ➗ **Numpy 1.23.5**

## 🎨 Detected Colors
The program is configured to detect the following colors:

- **Yellow**: Objects colored yellow will be highlighted with a bounding box and labeled "Yellow".
- **Red**: Objects colored red will be detected, outlined, and labeled "Red".
- **Blue**: Blue objects will be tracked with a bounding box and labeled "Blue".
- **Green**: Green objects will be detected, highlighted, and labeled "Green".

## 🔧 Code Breakdown

### Main Script
The script opens a webcam feed using **OpenCV** and continuously processes frames to detect colors:

- **HSV Conversion**: Each frame from the webcam is converted to **HSV color space** for better color detection.
- **Color Masks**: Based on predefined HSV ranges, a mask is created for each color (Yellow, Red, Blue, Green).
- **Bounding Boxes**: When a color is detected in the frame, a bounding box is drawn around the object using the mask.

### `get_limits(color)` Function
This utility function takes an RGB color and returns the HSV lower and upper bounds for detecting that color:

- Converts the given color to **HSV**.
- Defines the **lower** and **upper** bounds with some tolerance to detect colors in a range.

