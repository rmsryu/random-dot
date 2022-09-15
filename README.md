# An image recognition study of the art of stereogram images and computer vision visualization

## Developer notes

## Magiceye generation

### Data Folder structure

```
magiceye_gen
 ┣ color-polygons           # Shapes available form https://www.kaggle.com/datasets/gonzalorecioc/color-polygon-images
 ┃ ┣ data
 ┃ ┣ stereograms
 ┃ ┗ targets.csv
 ┣ shapes                   # Shapes available form https://www.kaggle.com/datasets/smeschke/four-shapes
 ┃ ┣ data
 ┃ ┗ stereograms
 ┣ magicpy
 ┃ ┣ magicpy.py
 ┃ ┗ __init__.py
 ┣ color-polygons-gen.ipynb # Test color-polygons-gen autosterograms
 ┣ color-polygons-gen.py    # Generate color-polygons grayscale autosterograms
 ┣ shapes-gen.ipynb         # Test shapes autosterograms
 ┗ shapes-gen.py            # Generate shapes grayscale autosterograms
```

### Hadoop
1. python client for hdfs `pip install hdfs`
2. 
