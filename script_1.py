import pandas as pd
import plotly.graph_objects as go
import csv
from scipy.ndimage.filters import gaussian_filter1d
import warnings

warnings.filterwarnings('ignore')

with open('video_1.5.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file);

    # next(csv_reader)

    with open('new_video_1.5.csv', 'w', newline='') as new_file:
        fieldnames = ['Frame', 'Happiness', 'Sadness', 'Surprise', 'Fear', 'Anger', 'Disgust', 'Contempt']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for line in csv_reader:
            # print(line[683], line[687], line[681], line[689], line[679], line[680], line[699], line[694], line[682])
            try:
                x = float(line[0]) + float(line[3])
                csv_writer.writerow({'Frame': line[0], 'Happiness': float(line[683]) + float(line[687]),
                                     'Sadness': float(line[679]) + float(line[681]) + float(line[689]),
                                     'Surprise': float(line[679]) + float(line[680]) + float(line[699]) + float(
                                         line[694]),
                                     'Fear': float(line[679]) + float(line[680]) + float(line[681]) + float(
                                         line[682]) + float(line[684]) + float(line[691]) + float(line[694]),
                                     'Anger': float(line[681]) + float(line[682]) + float(line[684]) + float(line[692]),
                                     'Disgust': float(line[685]) + float(line[689]) + float(line[693]),
                                     'Contempt': float(line[687]) + float(line[688])

                                     })

            except ValueError as e:
                print()
df = pd.read_csv('new_video_1.5.csv')
fig = go.Figure()
x = df['Frame']

sigmaValue = 5
y = df['Happiness'] / df['Happiness'].max()
Happiness = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Happiness, mode='lines', name='Happiness'))


y = df['Sadness'] / df['Sadness'].max()
Sadness = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Sadness + 2, mode='lines', name='Sadness'))

y = df['Surprise'] / df['Surprise'].max()
Surprise = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Surprise + 4, mode='lines', name='Surprise'))

y = df['Fear'] / df['Fear'].max()
Fear = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Fear + 6, mode='lines', name='Fear'))

y = df['Anger'] / df['Anger'].max()
Anger = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Anger + 8, mode='lines', name='Anger'))

y = df['Disgust'] / df['Disgust'].max()
Disgust = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Disgust + 10, mode='lines', name='Disgust'))

y = df['Contempt'] / df['Contempt'].max()
Contempt = gaussian_filter1d(y, sigma=sigmaValue)
fig.add_trace(go.Scatter(x=x, y=Contempt + 12, mode='lines', name='Contempt'))

fig.show()