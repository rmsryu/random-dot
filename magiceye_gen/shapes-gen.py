from magicpy import autostereogram_from_image
from os import path, mkdir
import tensorflow as tf

batch_size = 5
dataset_images = tf.keras.utils.image_dataset_from_directory(directory="shapes/data", color_mode='grayscale', batch_size=batch_size)

iterator = iter(dataset_images)
class_names = dataset_images.class_names
x = 0

try: 
    # Keep running next_batch till the Dataset is exhausted
    while True:
        images, labels = iterator.get_next()
        for i in range(batch_size):
            x+=1
            className = class_names[labels[i]]
            dirname = path.dirname(__file__)
            baseDir = f"{dirname}\\shapes\\stereograms"
            outputDir=f"{baseDir}\\{className}"
            
            if path.exists(baseDir) is False:
                mkdir(baseDir)

            if path.exists(outputDir) is False:
                mkdir(outputDir)

            img = tf.keras.utils.array_to_img(images[i])

            output=f"{outputDir}\\{className}_{x}.png"
            if path.exists(output) is False:
                autostereogram_from_image(img, output=output, pattern_div=8, invert=1)
            
        
except tf.errors.OutOfRangeError:
    pass