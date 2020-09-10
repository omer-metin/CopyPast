from xml.etree import ElementTree

from PyQt5 import QtWidgets

from clipboard_ui import Ui_MainWindow


COPIESXML = r"copies.xml"


class CopyPastEditor(object):

    def __init__(self):
        self._copies = ElementTree.parse(COPIESXML)

        self._app = QtWidgets.QApplication([])
        self._app.aboutToQuit.connect(self.loadXMLFromUi)

        self.mainWindow = QtWidgets.QMainWindow()
        Ui_MainWindow().setupUi(self.mainWindow)

    def openEditor(self):
        self.loadUiFromXML()
        self.mainWindow.show()
        self._app.exec_()

    def loadUiFromXML(self):
        root = self._copies.getroot()
        texts = [child.text for child in root.getchildren()]
        for i, text in enumerate(texts):
            lineEdit: QtWidgets.QLineEdit = self.mainWindow.findChild(
                QtWidgets.QLineEdit, name="lineEdit_{}".format(i+1))
            lineEdit.setProperty('text', text)

    def loadXMLFromUi(self):
        root = self._copies.getroot()
        for i, child in enumerate(root.getchildren()):
            child.text = self.mainWindow.findChild(
                QtWidgets.QLineEdit, name="lineEdit_{}".format(i+1)).text()
        self._copies.write(COPIESXML, encoding='UTF-8',
                           xml_declaration=True, short_empty_elements=False)

    def _createXML(self):
        root = ElementTree.Element("copies")
        for i in range(1, 10):
            ElementTree.SubElement(root, "copy_{}".format(i))
        tree = ElementTree.ElementTree(root)
        tree.write(COPIESXML, encoding='UTF-8',
                   xml_declaration=True, short_empty_elements=False)


cp = CopyPastEditor()
cp.openEditor()
