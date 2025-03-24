## 1 videolabel_tff_3cls.py
### generate annotation txt
modify paths for input_video_folder, input_csv_folder, output_txt_folder

## 2 landingPoint_sampleGeneration.py
### from txt to csv
modify path of file_folder (contains all labeled txts),
modify path of train_val_csv_folder (the output folder)
tip: change parameter 'adjacent' in function 'rough_landing' if you want to select different feature num

## 3 csv_split.py
### split csv into train and val
modify csv_folder

## 3.5 count_land_fly.py
### count curve nums

## 4 auto_train.py
change paths for data_folder and output_folder
tip: change feature_number if you changed adjacent in 2nd step

