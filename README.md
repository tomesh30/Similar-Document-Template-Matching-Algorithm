# Similar Document Template Matching Algorithm 

This project is a **Python-based image processing script** that detects the presence of a template in a document using OpenCV's `matchTemplate()` function.

It was designed to automate the detection of repeated stamps/seals, logos, or similar patterns across scanned documents.

---

##  Technologies Used

- Python
- OpenCV
- NumPy

 **Reference:**  
[OpenCV Template Matching Documentation](https://docs.opencv.org/2.4/modules/imgproc/doc/object_detection.html)

---

##  Objective

The goal is to locate a specific template (like a seal, logo, or signature) inside a larger scanned document and draw a bounding box around the matched region with high confidence.

---

##  Project Structure

├── template_matching.py # Main Python script
├── sample/ # Sample input images
│ ├── sample_input.png
│ └── sample_template.jpg
├── output/ # Output image after bounding box drawn
│ └── result.png
├── README.md # Project description


---

## 🚀 Features

- Reads both target image and template image
- Converts to grayscale for accurate matching
- Uses OpenCV's `cv2.matchTemplate()` for locating template
- Returns bounding box coordinates if matched
- Displays and saves the result with bounding box + confidence score
- Threshold based detection to filter weak matches
- Handles edge cases like file not found or poor match confidence

---

## 🧪 Example Usage

Inside `template_matching.py`, you can set your file paths:

python
image_path = "sample/sample_input.png"
template_path = "sample/sample_template.jpg"
output_path = "output/result.png"

 Sample Output
(Upload and link your result image in the output folder)

- Detected match with red bounding box

- Confidence score shown on the image

- If confidence < threshold (0.8), it will not consider it a valid match

Notes
- Make sure you’re using good-quality, high-resolution templates.

- The confidence threshold (default: 0.8) can be adjusted based on use-case.

- To avoid large repo size, node_modules or large folders are excluded.

