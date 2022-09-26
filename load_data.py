import progressbar
from os import path
from hdfs import InsecureClient
from bin import upload_to_hdfs
client2 = InsecureClient('http://localhost:9870', user='root')
client2.makedirs("/random-dot")

#upload_to_hdfs('magiceye_gen/color-polygons/stereograms', '/random-dot/train-data', 16000)
bar = progressbar.ProgressBar(max_value=16000)
barprogress = 0
def progress(file, bytes):
    if(progress == -1):
        barprogress += 1
        bar.update(barprogress)

dirname = path.dirname(__file__)
train_data_folder = f'{dirname}/magiceye_gen/shapes/stereograms'
client2.upload(hdfs_path='/random-dot/train-data', local_path=train_data_folder, progress=progress)
