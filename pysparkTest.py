from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
context = SparkContext(conf=conf)
print(context.version)
context.stop()
