import pandas as pd

data = {'Event': ['Attack Start', 'Detected', 'Contained', 'Eradicated', 'Recovered'],
        'Time': ['22:00', '22:02', '22:03', '22:04', '22:05']}  # Update with your times
df = pd.DataFrame(data)
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
detection_time = (df['Time'][1] - df['Time'][0]).total_seconds() / 60
total_time = (df['Time'][4] - df['Time'][0]).total_seconds() / 60
print(f"Detection: {detection_time} mins\nTotal IR: {total_time} mins")
