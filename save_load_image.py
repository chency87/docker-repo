import os

hadoop_dockerfile_path = '/home/chunyu/.db/hudi/hudi/docker/hoodie/docker-repo'

# ['base', 'namenode', 'datanode', 'historyserver', 'hive_base', 'spark_base', 'sparkmaster', 'sparkworker', 'sparkadhoc', 'prestobase']


HADOOP_VERSION = '2.10.2'
HIVE_VERSION = '3.1.2'
SPARK_VERSION = '2.4.4'
# SPARK_VERSION = '3.1.2'
PRESTO_VERSION = '0.271'

docker_dict = {
    'base' : f'hudi/hadoop-base_{HADOOP_VERSION}:latest',
    'namenode': f'hudi/hadoop-base_{HADOOP_VERSION}-namenode:latest',
    'datanode': f'hudi/hadoop-base_{HADOOP_VERSION}-datanode:latest',
    'historyserver': f'hudi/hadoop-base_{HADOOP_VERSION}-historyserver:latest', 
    'hive_base': f'hudi/hadoop-base_{HADOOP_VERSION}-hive_base_{HIVE_VERSION}:latest', 
    'spark_base': f'hudi/hadoop-base_{HADOOP_VERSION}-hive_base_{HIVE_VERSION}-sparkbase_{SPARK_VERSION}:latest', 
    'sparkmaster': f'hudi/hadoop-base_{HADOOP_VERSION}-hive_base_{HIVE_VERSION}-sparkmaster_{SPARK_VERSION}:latest', 
    'sparkworker': f'hudi/hadoop-base_{HADOOP_VERSION}-hive_base_{HIVE_VERSION}-sparkworker_{SPARK_VERSION}:latest', 
    'sparkadhoc': f'hudi/hadoop-base_{HADOOP_VERSION}-hive_base_{HIVE_VERSION}-sparkadhoc_{SPARK_VERSION}:latest',
    # 'prestobase': f'hudi/hadoop-base_{HADOOP_VERSION}-prestobase_{PRESTO_VERSION}:latest'
}
import subprocess
for dirname, target in docker_dict.items():
    
    dockerfile_path = os.path.join(hadoop_dockerfile_path, 'apachehudi')
    cmd = f"docker save {target} > {target.split(':')[0]}.tar"
    print(cmd)
    # print(dockerfile_path)
    os.chdir(hadoop_dockerfile_path)
    res = os.system(cmd)
    print(res)
    print('***' * 15)
    
    # p = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)

    # print(p.communicate())



# for dirname in os.listdir(hadoop_dockerfile_path):
    
#     print(dirname)

# for root, dirs, files in os.walk(hadoop_dockerfile_path):
#     path = root.split(os.sep)
#     for dirname in dirs:
#         print(dirname)

