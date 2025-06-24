# CrossCam Mapper

A minimal pipeline for **cross-camera identity mapping** between tracked video feeds.  
This project processes object-tracked data from two video perspectives and produces an association between tracked identities.  

It operates on pre-generated object detections from YOLOv11 models applied to provided `broadcast` and `tacticam` videos.

---

## Project Structure

| File / Folder                    | Description                                    |
|---------------------------------|------------------------------------------------|
| `broadcast.mp4`                  | Given video (broadcast camera)                 |
| `tacticam.mp4`                   | Given video (tacticam)                         |
| `best.pt`                        | Given YOLOv11 model (⭕⭕**This file is not available in this repository as it is too large**)   |
|                                 |                                                |
| `broadcast.py`                   | Script to run given YOLO on `broadcast.mp4`          |
| `tacticam.py`                    | Script to run given YOLO on `tacticam.mp4`           |
|                                 |                                                |
| `runs/detect/predict/broadcast.mp4`          | Object-detection results for `broadcast.mp4` (Compressed version of original avi file is stored)  |
| `runs/detect/predict2/tacticam.avi`          | Object-detection results for `tacticam.mp4` (Original avi file is stored)   |
|                                 |                                                |
| `run_broadcast.py`               | Script to generate tracking for broadcast      |
| `run_tacticam.py`                | Script to generate tracking for tacticam       |
|                                 |                                                |
| `track_broadcast.csv`            | YOLO tracking output for `broadcast.mp4`       |
| `track_tacticam.csv`             | YOLO tracking output for `tacticam.mp4`        |
|                                 |                                                |
| `mapping.py`                     | Main script: generates cross-camera ID mapping |
| `mapping_output.csv`             | Final output: broadcast ↔️ tacticam player mapping |
|                                 |                                                |
| `requirements.txt`               | Project dependencies                          |
| `README.md`                      | Project documentation                         |


###Final output mapping is stored in player_mapping.csv already. To regenerate mapping, run mapping.py file again.
---

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
