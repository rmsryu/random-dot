#!/usr/bin/python
# Shapes available form https://www.kaggle.com/datasets/gonzalorecioc/color-polygon-images
import progressbar
from magicpy import autostereogram_from_file_path, convert_image_black_white
import pandas as pd
from os import path, mkdir

inputDir = "color-polygons/data"
outputDirBlackWhite = "color-polygons/data-black-white"
outputDir = "color-polygons/stereograms"

# Images available from https://www.kaggle.com/datasets/gonzalorecioc/color-polygon-images by Gonzalo Recio
df_images = pd.read_csv("color-polygons/targets.csv")

# Generate autostereograms 
for i in progressbar.progressbar(range(df_images.shape[0])):
    row = df_images.values[i]
    fileName = row[1]
    image_class = row[2]    
    outputDirClass = f"{outputDir}/{image_class}"

    if not path.exists(f"{outputDirClass}/{fileName}"):
        # Create data_grayscale folder
        if not path.exists(outputDirBlackWhite):
            mkdir(outputDirBlackWhite)

        if not path.exists(f"{outputDirBlackWhite}/{fileName}"):
            convert_image_black_white(f"{inputDir}/{fileName}",f"{outputDirBlackWhite}/{fileName}")

        # Create class folder
        if not path.exists(outputDir):
            mkdir(outputDir)
        if not path.exists(f"color-polygons/stereograms/{image_class}"):
            mkdir(outputDirClass)

        # Create random-dot stereogram
        autostereogram_from_file_path(f"{outputDirBlackWhite}/{fileName}",f"{outputDirClass}/{fileName}", 8, 1, True)