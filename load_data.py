from hdfs import InsecureClient
client2 = InsecureClient('http://localhost:9870', user='hduser')
client2.makedirs("/random-dot")

# from hdfs3 import HDFileSystem
# hdfs=HDFileSystem(host='localhost',port=9000)
# hdfs.ls('/')


# from pyarrow import fs
# host="localhost"
# port=9000
# user="root"
# hdfs = fs.HadoopFileSystem(host, port, user=user)