from pyspark.sql import SparkSession
from pyspark.sql.functions import md5, col


def anonymize_data(
    input_path="data/output_csv", output_path="data/anonymized_output_csv"
):
    spark = SparkSession.builder.appName("AnonymizeData").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    anonymized_df = (
        df.withColumn("first_name", md5(col("first_name")))
        .withColumn("last_name", md5(col("last_name")))
        .withColumn("address", md5(col("address")))
    )

    anonymized_df.write.csv(output_path, header=True, mode="overwrite")

    spark.stop()


if __name__ == "__main__":
    anonymize_data()
