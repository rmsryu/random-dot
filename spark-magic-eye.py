from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from petastorm.spark import SparkDatasetConverter, make_spark_converter
import io
import numpy as np
import tensorflow as tf
from PIL import Image
from petastorm import TransformSpec
from tensorflow import keras

from hyperopt import fmin, tpe, hp, SparkTrials, STATUS_OK

IMG_SHAPE = (1024, 1024, 3)
BATCH_SIZE = 32
NUM_EPOCHS = 5

#hdfs_directory = 'hdfs://localhost:9870/random-dot/train-data'
#dataset_images = tf.keras.utils.image_dataset_from_directory(directory=hdfs_directory, color_mode='grayscale', batch_size=BATCH_SIZE)
master_container_id = "16087a9ad851"
conf = SparkConf() \
    .setAppName('random-dot') \
    .setMaster(f'spark://{master_container_id}:7077')\
    .set("spark.driver.host",master_container_id)
sc = SparkContext(conf=conf)
spark = SparkSession.builder.config.getOrCreate()
