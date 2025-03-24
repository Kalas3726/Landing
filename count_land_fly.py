import cv2
import csv
import ast
import os

def count_rough_landing(csv_file):
    landing_count, flying_count, serving_count = 0, 0, 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            label = ast.literal_eval(row[-1])
            if label == 1:
                landing_count += 1
            elif label == 0:
                flying_count += 1
            elif label == 2:
                serving_count += 1
    return landing_count, flying_count, serving_count

def count_precise_landing(csv_file):
    count_dict = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            label = ast.literal_eval(row[-1])
            if label not in count_dict:
                count_dict[label] = 1
            else:
                count_dict[label] += 1
    return count_dict

file_folder = r"D:\Ai_tennis\Landing\train_val_csv\dataset_0323"

# for root, dirs, filenames in os.walk(file_folder):
#     for file in filenames:
#         if file.endswith(".csv"):
#             file_path = os.path.join(root, file)
#             count_dict = count_precise_landing(file_path)
#             for key, value in count_dict.items():
#                 print(f"{key}的数量:{value}")
for root, dirs, filenames in os.walk(file_folder):
    for file in filenames:
        if file.endswith(".csv"):
            file_path = os.path.join(root, file)
            landing_count, flying_count, serving_count = count_rough_landing(file_path)
            print(f"{file_path}, len(labels_landing): {landing_count}, len(labels_flying): {flying_count}, len(labels_serving): {serving_count}")
