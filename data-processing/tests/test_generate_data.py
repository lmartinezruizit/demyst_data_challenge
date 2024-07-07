import unittest
import os
from pyspark.sql import SparkSession


class TestGenerateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestGenerateData").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_generate_data_output_exists(self):
        self.assertTrue(os.path.exists("data/output_csv"))

    def test_generate_data_output_content(self):
        csv_files = os.listdir("data/output_csv")
        self.assertGreater(len(csv_files), 0, "No CSV files found in output directory")

        for csv_file in csv_files:
            if csv_file.endswith(".csv"):
                df = self.spark.read.csv(
                    f"data/output_csv/{csv_file}", header=True, inferSchema=True
                )
                self.assertGreater(df.count(), 0, f"CSV file {csv_file} is empty")


if __name__ == "__main__":
    unittest.main()
