bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output1/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /mapreduce-test/mapreduce-test-data/access.log /lab1/input1/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../BigDataAsn/mapper3.py -mapper ../BigDataAsn/mapper3.py \
-file ../BigDataAsn/reducer3.py -reducer ../BigDataAsn/reducer3.py \
-input /lab1/input1/* -output /lab1/output1/
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output1/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output1/
bash /mapreduce-test/stop.sh
