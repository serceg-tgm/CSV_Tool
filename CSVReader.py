from csv import Sniffer, DictReader

class CSVReader:

    @staticmethod
    def read(filename):

        with open(filename, "r") as csvfile:

            sniffer = Sniffer()
            sample = csvfile.read(1024)
            dialect = sniffer.sniff(sample, delimiters=[';', ','])

            if sniffer.has_header(sample):
                # file has header
                pass

            csvfile.seek(0)

            lines_reader = DictReader(csvfile, dialect=dialect)

            lines = []
            for line in lines_reader:
                lines.append(line)

            return lines