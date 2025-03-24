import os
import csv
import random

csv_folder = r"D:\Ai_tennis\Landing\train_val_csv\dataset_0323"
input_csv_path = os.path.join(csv_folder, "train_val.csv")
train_csv = os.path.join(csv_folder, "train.csv")
val_csv = os.path.join(csv_folder, "val.csv")
split_ratio = 0.8

with open(input_csv_path, 'r') as input_file:
    reader = csv.reader(input_file)
    lines = list(reader)

random.shuffle(lines)

split_index = int(len(lines) * split_ratio)

lines1 = lines[:split_index]
lines2 = lines[split_index:]

with open(train_csv, 'w', newline='') as output_file1:
    writer = csv.writer(output_file1)
    writer.writerows(lines1)

with open(val_csv, 'w', newline='') as output_file2:
    writer = csv.writer(output_file2)
    writer.writerows(lines2)
