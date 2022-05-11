
from PyQt6.QtWidgets import QApplication, QDialog
from sys import exit
from mainwindow import MainWindow
from dos import DosAppView, DosAppController
from bands import BandsAppView, BandsAppController


class MainView(QDialog, MainWindow):
    """
    Main window object. Details of the functioning of each of the modules
    can be found in their respective files and folders (dos and bands).
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.DosButton.clicked.connect(self.open_dos_window)
        self.BandsButton.clicked.connect(self.open_bands_window)

    def open_dos_window(self):
        self.dos_window = DosAppView()
        DosAppController(self.dos_window)
        self.DosButton.setDisabled(True)
        self.dos_window.signal.closed.connect(self.close_dos_window)
        self.dos_window.show()

    def close_dos_window(self):
        self.DosButton.setEnabled(True)

    def open_bands_window(self):
        self.bands_window = BandsAppView()
        BandsAppController(self.bands_window)
        self.BandsButton.setDisabled(True)
        self.bands_window.signal.closed.connect(self.close_bands_window)
        self.bands_window.show()

    def close_bands_window(self):
        self.BandsButton.setEnabled(True)


def main():
    """
    Main function - creates an instance of window (view)
    and applies controller to it
    """
    app = QApplication([])
    view = MainView()
    view.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
