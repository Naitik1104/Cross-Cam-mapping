# CrossCam Mapper

A minimal pipeline for **cross-camera identity mapping** between tracked video feeds.  
This project processes object-tracked data from two video perspectives and produces an association between tracked identities.  

It operates on pre-generated object detections from YOLOv11 models applied to provided `broadcast` and `tacticam` videos.

---

## Project Structure


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

Final mapping is written to `mapping_output.csv`:

```csv
broadcast_id,tacticam_id
2,4
4,4
24,4
