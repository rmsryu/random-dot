import progressbar
import os
import glob
from hdfs import InsecureClient

def upload_to_hdfs(local_folder:str, hdfs_folder:str, total_count:int):
    x = 0
    #bar = progressbar.ProgressBar(max_value=16000)
    #barprogress += 1
    #bar.update(barprogress)
    # root_dir needs a trailing slash (i.e. /root/dir/)
    for filename in glob.iglob(local_folder + '**/*.png', recursive=True):
        print(filename)
        
    