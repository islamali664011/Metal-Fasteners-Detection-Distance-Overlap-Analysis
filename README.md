# Metal-Fasteners-Detection-Distance-Overlap-Analysis
A computer vision system for detecting metal clamps in industrial images, computing spatial distances between them, and analyzing overlapping relationships for quality inspection and structural assessment.


  🔩 Industrial Metal Clamp Detection & Spatial Analysis System
  
📌 Overview

This project is an industrial computer vision system designed for automatic detection of metal clamps in images and video streams. It goes beyond simple object detection by performing geometric spatial analysis, including:

- Accurate clamp detection using YOLO
- Calibration from pixels to real-world units (inches)
- Measurement of spacing between clamps
- Detection of overlapping or abnormal clamp arrangements
- Full pipeline support for both images and videos

The system is suitable for industrial inspection, quality control, and structural verification tasks.


🚀 Key Features

🔍 Object Detection

- YOLO-based detection using a custom-trained model (yolo11m)
- High-accuracy industrial dataset trained via Roboflow

  
📏 Spatial Measurement

- Circle fitting to estimate structure geometry
- Pixel-to-inch calibration using real-world reference diameter
- Arc-length-based spacing computation between clamps
  
⚠️ Anomaly Detection

- Detects uneven spacing using statistical analysis (IQR)
- Identifies overlapping or double clamps
- Flags structural inconsistencies

  
🎥 Video Analysis
- Frame-by-frame processing (1 frame per second)
- Generates annotated analysis video
- Saves per-frame inspection images

  
🧠 Model Training Details

The model was trained using Ultralytics YOLO11m on a custom industrial dataset.


📦 Dataset

Source: Roboflow
Format: YOLOv11
Workspace: cracks-oa7kv
Project: industrial-project-front-view


⚙️ Training Configuration
Epochs: 150
Image size: 1280
Batch size: 8

Optimizations:
Cosine LR scheduling
Mixed precision (AMP)
Mosaic augmentation
HSV augmentation (brightness, saturation, hue)
Geometric transforms (rotation, scaling, shear)


📊 Performance Results

The final trained model achieved state-of-the-art accuracy after multiple failed attempts and improvements over earlier models.
Metric	Value
Precision	0.9978
Recall	1.0000
mAP@50	0.9950
mAP@50-95	0.8098
⚠️ This is the best-performing model after several iterations.
Earlier versions performed poorly, and even additional preprocessing (e.g., brightness augmentation via Roboflow) did not improve results significantly.
The final model represents the most stable and accurate configuration achieved in this project.


🧪 Pipeline Workflow

1️⃣ Detection
Detect clamps using trained YOLO model

2️⃣ Geometry Reconstruction
Extract bounding box centers
Fit circular structure using least squares

3️⃣ Calibration
Convert pixel distances → inches using known diameter reference

4️⃣ Spacing Analysis
Compute arc-length distances between consecutive clamps
Evaluate uniformity using statistical thresholds

5️⃣ Overlap Detection
Identify abnormal clustering (double clamps)
Merge detections dynamically based on size threshold


🎥 Video Processing Mode
Processes video frame-by-frame
Extracts 1 frame per second

Generates:
Annotated frames
Final analysis video
Outputs saved automatically


📁 Project Structure
├── model/
│   └── best-2.pt
├── dataset/ (Roboflow YOLOv11)
├── notebooks/
│   └── training.ipynb
├── output/
│   ├── analysis_images/
│   └── output_video.mp4
└── README.md


🛠️ Technologies Used
Python
Ultralytics YOLO
OpenCV
NumPy
Matplotlib
Roboflow


📌 Real-World Applications
Industrial quality inspection
Manufacturing defect detection
Mechanical assembly validation
Structural alignment analysis
Automated visual inspection systems

🏁 Conclusion
This system demonstrates a full industrial-grade pipeline combining deep learning-based object detection with geometric reasoning and real-world measurement, enabling accurate inspection of metal clamp structures in both images and videos.

📎 Notes
Model trained on custom dataset
Pixel-to-inch calibration depends on known physical reference
Designed for controlled industrial imaging environments
