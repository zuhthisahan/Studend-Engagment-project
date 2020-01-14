import pandas as pd
import csv
import warnings

warnings.filterwarnings('ignore')

csvData = ['Happiness', 'Sadness', 'Surprise', 'Fear', 'Anger', 'Disgust', 'Contempt']

# 6 + 12  AU06_683+AU12_687
# 1 + 4 + 15  AU01_679+AU04_681+AU15_689
# 1 + 2 + 5 + 26  AU01_679+AU02_680+AU05_682+AU26_694

# 1 + 2 + 4 + 5 + 7 + 20 + 26  AU01_679+AU02_680+AU04_681+AU05_682+AU07_684+AU20_691+AU26_694
# 4 + 5 + 7 + 23  AU04_681+AU05_682+AU07_684+AU23_692
# 9 + 15 + 16 AU09_685+AU15_689+AU25_693
# 12 + 14 AU12_687+AU14_688


with open('pre_Process.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(csvData)
csvFile.close()

df = pd.read_csv('output.csv')

data = []

for row in df.iterrows():
    data = [row[1][683] + row[1][687], row[1][679] + row[1][681] + row[1][689],
            row[1][679] + row[1][680] + row[1][682] + row[1][694],
            row[1][679] + row[1][680] + row[1][681] + row[1][682] + row[1][684] + row[1][691] + row[1][694],
            row[1][681] + row[1][682] + row[1][684] + row[1][692], row[1][685] + row[1][689] + row[1][693],
            row[1][687] + row[1][688]]
    with open('pre_Process.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(data)

csvFile.close()
print("Saving pre processed data")
