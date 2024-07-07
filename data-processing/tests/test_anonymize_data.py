import unittest
import os
from pyspark.sql import SparkSession


class TestAnonymizeData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestAnonymizeData").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_anonymize_data_output_exists(self):
        self.assertTrue(os.path.exists("data/anonymized_output_csv"))

    def test_anonymize_data_output_content(self):
        csv_files = os.listdir("data/anonymized_output_csv")
        self.assertGreater(
            len(csv_files), 0, "No CSV files found in anonymized output directory"
        )

        for csv_file in csv_files:
            if csv_file.endswith(".csv"):
                df = self.spark.read.csv(
                    f"data/anonymized_output_csv/{csv_file}",
                    header=True,
                    inferSchema=True,
                )
                self.assertGreater(df.count(), 0, f"CSV file {csv_file} is empty")


if __name__ == "__main__":
    unittest.main()
