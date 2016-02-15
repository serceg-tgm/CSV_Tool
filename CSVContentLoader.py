from PyQt5.QtWidgets import QWidget
import CSVView
import csv

class CSVContentLoader(QWidget):
    """
    In dieser Klasse wird der Inhalt des CSV-Files ausgelesen und im Fenster ausgegeben.
    """

    def __init__(self):
        """
        Im Konstruktor wird ein Objekt der View-Klasse erstellt und die Funktion zum Anzeigen des Inhalts des
        CSV-Files angezeigt.
        """
        super().__init__()
        self.view = CSVView.Ui_CSVTool()
        self.view.setupUi(self)
        self.showCsvContent()

    def showCsvContent(self):
        """
        In dieser Funktion wird der Inhalt aus dem CSV-File "RealEstateTransactions" ausgelesen und zum Label, welches
        im Fenster positioniert wurde, hinzugefuegt.
        """
        temp = ""
        with open('RealEstateTransactions.csv', 'r') as csvfile:
            readLines = csv.reader(csvfile, delimiter=',')
            for row in readLines:
                temp += ', '.join(row)
                temp += '\r\n'
        self.view.csvContent.setText(temp)