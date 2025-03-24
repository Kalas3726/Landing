'''1'''
import os
import csv
import ast

def rough_landing(txt_file, adjacent=4):
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = [line.split(",") for line in f.readlines()]
    samples, labels = [], []
    label0, label1 = [], []
    for i in range(len(content)-(adjacent*2+1)):
        sample = []
        recent_label = []
        for j in range(adjacent*2+1):
            sample.append(content[i+j][0])
            sample.append(content[i+j][1])
            recent_label.append(int(content[i+j][2][:2]))
        samples.append(sample)
        if 1 in recent_label and 1 not in recent_label[:2] and 1 not in recent_label[-2:]:
            labels.append(1)
        elif 2 in recent_label and 2 not in recent_label[:2] and 2 not in recent_label[-2:]:
            labels.append(2)
        else:
            labels.append(0)
        
    return samples, labels

def precise_landing(txt_file, interval=1, adjacent=4):
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = [line.split(",") for line in f.readlines()]
    samples, labels = [], []
    label0, label1 = [], []
    for i in range(len(content) - (adjacent * 2 + 1)):
        sample = []
        recent_label = []
        for j in range(adjacent * 2 + 1):
            sample.append(content[i + j][0])
            sample.append(content[i + j][1])
            recent_label.append(int(content[i + j][2][:2]))
        if 1 in recent_label and 1 not in recent_label[:1] and 1 not in recent_label[-1:]:
            samples.append(sample)
            labels.append(recent_label.index(1))

    return samples, labels

def sandwich__prediction(csv_file, adjacent=3):
    ball_locations = []
    height, width = 720, 1280
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        for row in reader:
            ball_location = ast.literal_eval(row[5])
            # 将ball_location字符串解析为列表
            ball_locations.append(ball_location)
            # height, width = ast.literal_eval(row[11])[0], ast.literal_eval(row[11])[1]
    samples, labels = [], []
    for i in range(len(ball_locations) - (adjacent * 2)):
        sample = []
        label = []
        for j in range(adjacent * 2 + 1):
            sample.append(ball_locations[i + j][0] / width)
            sample.append(ball_locations[i + j][1] / height)
        label.append(sample.pop(adjacent * 2))
        label.append(sample.pop(adjacent * 2))
        if all(x > 0 for x in sample) and all(y > 0 for y in label):
            samples.append(sample)
            labels.append(label)

    return samples, labels

def front_prediction(csv_file, adjacent=2):
    ball_locations = []
    height, width = 720, 1280
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        for row in reader:
            ball_location = ast.literal_eval(row[5]) # 将ball_location字符串解析为列表
            ball_locations.append(ball_location)
            # height, width = ast.literal_eval(row[11])[0], ast.literal_eval(row[11])[1]
    samples, labels = [], []
    for i in range(len(ball_locations) - adjacent):
        sample = []
        label = []
        for j in range(adjacent + 1):
            # sample.append(ball_locations[i + j][0])
            # sample.append(ball_locations[i + j][1])
            sample.append(ball_locations[i + j][0] / width)
            sample.append(ball_locations[i + j][1] / height)
        label.append(sample.pop(adjacent*2))
        label.append(sample.pop(adjacent*2))
        if all(x > 0 for x in sample) and all(y > 0 for y in label):
            samples.append(sample)
            labels.append(label)

    return samples, labels

# file_folder = "labeled_input_csv_folder"
#
# # 使用 os.walk 遍历文件夹及其子文件夹，找出所有 .csv 文件
# files = []
# for root, dirs, filenames in os.walk(file_folder):
#     for file in filenames:
#         if file.endswith(".csv"):
#             files.append(os.path.join(root, file))
# samples, labels = [], []
# for file in files:
#     s, l = front_prediction(file)
#     samples += s
#     labels += l
#
# # input_csv_file = r"D:\Ai_tennis\yolov7_main\landing_csv\xzy_upper\20231011_xzy_yt_9.csv"
# # samples, labels = miss_location_prediction(input_csv_file)
# output_csv_file = os.path.join("prediction_dataset", "train_val.csv")
# with open(output_csv_file, "w", newline='') as f:
#     writer = csv.writer(f)
#     for sample, label in zip(samples, labels):
#         row = sample + label
#         writer.writerow(row)
#         # sample_str = ",".join(sample) + ",{}\n".format(label)
#         # f.write(sample_str)


file_folder = r"D:\Ai_tennis\Landing\relabel_txt_folder\txt_0322"

# 使用 os.walk 遍历文件夹及其子文件夹，找出所有 .txt 文件
files = []
for root, dirs, filenames in os.walk(file_folder):
    for file in filenames:
        if file.endswith(".txt"):
            files.append(os.path.join(root, file))
samples, labels = [], []
for file in files:
    s, l = rough_landing(file)
    samples += s
    labels += l

train_val_csv_folder = r"D:\Ai_tennis\Landing\train_val_csv\dataset_0323"
csv_file = os.path.join(train_val_csv_folder, "train_val.csv")
with open(csv_file, "w") as f:
    for sample, label in zip(samples, labels):
        sample_str = ",".join(sample) + ",{}\n".format(label)
        f.write(sample_str)



