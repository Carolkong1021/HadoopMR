#!/bin/sh
read -p 'Start point:' start
read -p 'End point:' end
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /mapreduce-test/mapreduce-test-data/access.log /lab2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../BigDataAsn/mapper4.py -mapper ../BigDataAsn/mapper4.py \
-file ../BigDataAsn/reducer4.py -reducer '../BigDataAsn/reducer4.py  ${start} ${end}' \
-input /lab2/input/* -output /lab2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output/
bash /mapreduce-test/stop.sh
