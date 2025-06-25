import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import csv

broadcast_df = pd.read_csv("tracks_broadcast.csv")
tacticam_df = pd.read_csv("tracks_tacticam.csv")

def compute_avg_centers(df):
    df['center_x'] = (df['x1'] + df['x2']) / 2
    df['center_y'] = (df['y1'] + df['y2']) / 2
    avg_positions = df.groupby('track_id')[['center_x', 'center_y']].mean()
    return avg_positions

broadcast_avg = compute_avg_centers(broadcast_df)
tacticam_avg = compute_avg_centers(tacticam_df)

dist_matrix = cdist(broadcast_avg.values, tacticam_avg.values)

mapping = {}
for i, row in enumerate(dist_matrix):
    broadcast_id = broadcast_avg.index[i]
    closest_idx = np.argmin(row)
    tacticam_id = tacticam_avg.index[closest_idx]
    mapping[broadcast_id] = tacticam_id

print("Cross-Camera Player Mapping:")
for b_id, t_id in mapping.items():
    print(f"Broadcast ID {b_id} → Tacticam ID {t_id}")

mapping_df = pd.DataFrame(list(mapping.items()), columns=['broadcast_id', 'tacticam_id'])
mapping_df.to_csv("player_mapping.csv", index=False)
with open('player_mapping.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['broadcast_id', 'tacticam_id'])  

    for broadcast_id, tacticam_id in mapping.items():
        writer.writerow([broadcast_id, tacticam_id])

print("Mapping written to player_mapping.csv")
