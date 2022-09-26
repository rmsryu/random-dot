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


## Tensorflow

Learning tutorial
https://www.tensorflow.org/tutorials/images/transfer_learning

## Simplify data conversion from Spark to TensorFlow
https://learn.microsoft.com/en-us/azure/databricks/_static/notebooks/deep-learning/petastorm-spark-converter-tensorflow.html


# Distributed training
> Install horovod: https://horovod.readthedocs.io/en/stable/install_include.html (only linux)
