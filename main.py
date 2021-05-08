# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice


class oakos_welcome(QWidget):
    def __init__(self):
        super(oakos_welcome, self).__init__()
        self.load_ui()

#    def load_ui(self):
#        loader = QUiLoader()
#        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
#        ui_file = QFile(path)
#        ui_file.open(QFile.ReadOnly)
#        loader.load(ui_file, self)
#        ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.closeButton.clicked.connect(lambda: sys.exit(0))
#    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
#    widget = oakos_welcome()
#    widget.show()
    sys.exit(app.exec_())

