from unittest import TestCase
from CSVReader import CSVReader

csvFile = "RealEstateTransactions.csv"

class CSVToolTests(TestCase):

    def testFileNotFoundError(self):
        self.assertRaises(FileNotFoundError, CSVReader.read, "kleiner Test...")

    def testFirstLineOfFile(self):
        lines = CSVReader.read(csvFile)
        self.assertEqual("5601 REXLEIGH DR", lines[0]["street"])

    def testSecondLineOfFile(self):
        lines = CSVReader.read(csvFile)
        self.assertEqual("1909 YARNELL WAY", lines[1]["street"])

    def testThirdLineOfFile(self):
        lines = CSVReader.read(csvFile)
        self.assertEqual("9169 GARLINGTON CT", lines[2]["street"])

    def testFourthLineOfFile(self):
        lines = CSVReader.read(csvFile)
        self.assertEqual("6932 RUSKUT WAY", lines[3]["street"])