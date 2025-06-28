import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import pandas as pd

def run_tracking(video, model, output_csv):

    model = YOLO(model)

    tracker = DeepSort(max_age=30)

    cap = cv2.VideoCapture(video)
    frame_num = 0

    detections = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_num += 1

        results = model.predict(source=frame, save=False, verbose=False)
        result = results[0]

        if result.boxes is not None:
            boxes_xyxy = result.boxes.xyxy.cpu().numpy()
            scores = result.boxes.conf.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy()

            detections_for_sort = []
            for box, score, cls in zip(boxes_xyxy, scores, classes):
                if cls == 0:  
                    x1, y1, x2, y2 = box
                    detections_for_sort.append(([x1, y1, x2-x1, y2-y1], score, 'player'))

            tracks = tracker.update_tracks(detections_for_sort, frame=frame)

            for track in tracks:
                if not track.is_confirmed():
                    continue
                track_id = track.track_id
                ltrb = track.to_ltrb()
                detections.append([frame_num, track_id, *ltrb])



    cap.release()
    cv2.destroyAllWindows()


    df = pd.DataFrame(detections, columns=['frame', 'track_id', 'x1', 'y1', 'x2', 'y2'])
    df.to_csv(output_csv, index=False)

    print(f"Tracking results saved to {output_csv}")
