# CrossCam Mapper

A minimal pipeline for **cross-camera identity mapping** between tracked video feeds.  
This project processes object-tracked data from two video perspectives and produces an association between tracked identities.  

It operates on pre-generated object detections from YOLOv11 models applied to provided `broadcast` and `tacticam` videos.

---

## Project Structure
├── broadcast.mp4 # Given video (broadcast cam)
├── tacticam.mp4 # Given video (tacticam)
├── best.pt # Given YOLOv11 model (provided)
├── broadcast.py # Script for running given object detection model on broadcast.mp4
├── tacticam.py # Script for running given object detectio model on tacticam.mp4
├── runs/detect/predict1 # Contains object-detected video for broadcast.mp4
├── runs/detect/predict2 # Contains object-deteted video for tacticam.mp4
├── run_broadcast.py # Script to generate tracking for broadcast.mp4
├── run_tacticam.py # Script to generate tracking for tacticam.mp4
├── track_broadcast.csv # YOLO tracking result on broadcast.mp4
├── track_tacticam.csv # YOLO tracking result on tacticam.mp4
├── mapping.py # Main script: generates identity mapping
├── mapping_output.csv # Final output: cross-camera ID mapping
├── requirements.txt # Dependencies
└── README.md # Project README

---
#Final output mapping is stored in player_mapping.csv already. To regenerate mapping, run mapping.py file again.

## How It Works

1. **Input:** Two video sources with separate views of the same scene — `broadcast.mp4` and `tacticam.mp4`
2. **Object Detection:** YOLOv11 model is used to detect and track objects in each video.
3. **Tracking Output:**  
    - `track_broadcast.csv`  
    - `track_tacticam.csv`  
    Each CSV contains object tracking data per frame.
4. **Mapping:**  
    - `mapping.py` compares movement patterns and positions across views.  
    - Generates a mapping between `broadcast_id` ↔ `tacticam_id`.

---

## Output

Final mapping is written to `player_mapping.csv`:

```csv
broadcast_id,tacticam_id
2,4
4,4
24,4
