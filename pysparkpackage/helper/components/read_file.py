from doctest import master
from pyspark.sql import SparkSession

class read_file_helper():
    @staticmethod
    def read_file(path, file_type):
        if file_type == 'parquet':
            return read_file_helper.read_file_spark(path)

    @staticmethod
    def read_file_spark(path):
        spark = SparkSession.builder \
                .appName('read file spark') \
                .master('local[*]') \
                .getOrCreate()

        return spark.read.parquet(path)