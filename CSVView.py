# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSVView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CSVTool(object):
    """
    Diese Klasse stellt die View-Klasse der Applikation dar. Es wird das notwendige Label zum Anzeigen des Inhalts
    vom CSV-File erstellt und passend im Fenster positioniert. Die Gestaltung der GUI erfolgte ueber den QT-Designer,
    die Konvertierung in ein Python-File wurde mittels eines Pyside-Befehls erledigt.
    """
    def setupUi(self, CSVTool):
        """
        Diese Methode dient dazu, das notwendige Label zu erstellen und im Fenster zu positionieren.

        :param CSVTool: das Fenster, welches man laden moechte
        """
        CSVTool.setObjectName("CSVTool")
        CSVTool.resize(816, 582)
        self.verticalLayoutWidget = QtWidgets.QWidget(CSVTool)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 821, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.csv = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.csv.setObjectName("csv")
        self.csvContent = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.csvContent.setAlignment(QtCore.Qt.AlignCenter)
        self.csvContent.setWordWrap(True)
        self.csvContent.setObjectName("csvContent")
        self.csv.addWidget(self.csvContent)

        self.retranslateUi(CSVTool)
        QtCore.QMetaObject.connectSlotsByName(CSVTool)

    def retranslateUi(self, CSVTool):
        """
        Hier werden die Namen des Fensters und des Labels gesetzt.

        :param CSVTool: das Fenster, in welchem die Texte angezeigt werden
        """
        _translate = QtCore.QCoreApplication.translate
        CSVTool.setWindowTitle(_translate("CSVTool", "CSV-Tool"))
        self.csvContent.setText(_translate("CSVTool", "TextLabel"))

