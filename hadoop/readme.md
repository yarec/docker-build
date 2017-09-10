docker pull sequenceiq/hadoop-docker:2.7.0

docker run -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash


cd $HADOOP_PREFIX
# run the mapreduce
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar grep input output 'dfs[a-z.]+'

# check the output
bin/hdfs dfs -cat output/*
