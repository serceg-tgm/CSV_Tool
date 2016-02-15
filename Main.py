from PyQt5.QtWidgets import QApplication
import sys
from CSVContentLoader import CSVContentLoader

class ApplicationRunner:
    """
    Diese Klasse stellt die Main-Klasse des CSV-Tools dar. Die Applikation wird gestartet und das Fenster wird
    angezeigt, indem ein Objekt von der CSVContentLoader-Klasse erstellt wird.
    """

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        c = CSVContentLoader()
        c.show()
        sys.exit(app.exec_())