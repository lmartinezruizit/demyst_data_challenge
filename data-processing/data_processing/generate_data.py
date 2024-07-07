from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType
import random
import string
from datetime import date


def generate_data(output_path="data/output_csv", num_records=1000000):
    spark = SparkSession.builder.appName("GenerateData").getOrCreate()

    schema = StructType(
        [
            StructField("first_name", StringType(), True),
            StructField("last_name", StringType(), True),
            StructField("address", StringType(), True),
            StructField("date_of_birth", DateType(), True),
        ]
    )

    def random_string(length=10):
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    def random_date(start_year=1950, end_year=2023):
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return date(year, month, day)

    data = [
        (random_string(5), random_string(7), random_string(15), random_date())
        for _ in range(num_records)
    ]

    df = spark.createDataFrame(data, schema)

    df.write.csv(output_path, header=True, mode="overwrite")

    spark.stop()


if __name__ == "__main__":
    generate_data()
