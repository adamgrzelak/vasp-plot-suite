from sys import exit
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtTest import QTest
from PyQt6.QtCore import pyqtSignal, QObject
from bands.qtdesign import BandsAppWindow
from bands.vaspbandtools import BandStructure
from controller import AppController
import numpy as np


class Signal(QObject):
    closed = pyqtSignal()


class BandsAppView(QDialog, BandsAppWindow):
    """
    Main window object
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.signal = Signal()

    def closeEvent(self, e):
        self.signal.closed.emit()


class BandsAppController(AppController):

    def __init__(self, view):
        """
        connects buttons to functions
        :param view: BandsAppView instance
        """
        super().__init__(view)
        self.view.refresh_plot_btn.clicked.connect(self.refresh_plot)
        # path to sample file for debugging purposes
        self.view.load_txt.setText(
            "/Users/adambialy/Documents/Coding/Python-portfolio/vasp-integrated/AgF2-sample/bands/vasprun.xml")

    def load_data(self):
        """
        Load VASP output into a Bandstructure object
        """
        QTest.qWait(5)
        self.view.load_label.setText("Loading...")
        QTest.qWait(5)
        self.active_path = self.view.load_txt.text()
        try:
            QTest.qWait(5)
            self.view.load_label.setText("Loading bands...")
            QTest.qWait(5)
            self.loaded_data = BandStructure(self.active_path, load_all=False)
            data_per_point = self.loaded_data.nbands * self.loaded_data.nions
            if self.loaded_data.spin:
                data_per_point = data_per_point * 2
            gen = self.loaded_data._datagen()
            data = []
            i = 0
            for r in gen:
                i += 1
                if i % data_per_point == 0:
                    QTest.qWait(5)
                    self.view.load_label.setText(f"Processing k-point {i // data_per_point}/{self.loaded_data.nkpts}...")
                    QTest.qWait(5)
                data.append(r)
            QTest.qWait(5)
            self.view.load_label.setText("Finishing up...")
            QTest.qWait(5)
            self.loaded_data._set_data(data)
            # account for different shorthands for dx2-y2 orbital depending on VASP version
            if "x2-y2" in self.loaded_data.levels:
                self.loaded_data.levels[np.where(self.loaded_data.levels == "x2-y2")] = "dx2"
                self.loaded_data.leveldict["dx2"] = self.loaded_data.leveldict.pop("x2-y2")
            while self.view.ax._children:
                self.view.ax._children[0].remove()
            self.toggle_plot()
            self.adjust_window()
            QTest.qWait(5)
            self.view.load_label.setText("Plotting...")
            QTest.qWait(5)
            self.plot_basic_bands()
            msg = f"<b>{self.loaded_data.name}</b> system was loaded successfully"
            self.view.load_label.setText(msg)
        except Exception as e:
            self.view.load_label.setText(e.args[0])
            QTest.qWait(2000)
            self.view.load_label.setText("Browse files and load a system")
            self.disable_window()

    def plot_added_data(self, atoms, states, spin, name, color):
        sel_dataset = self.loaded_data.select(atoms, states, spin, name)
        for i in range(self.loaded_data.nbands):
            if sel_dataset.data.max() != 0:
                markers = sel_dataset.data[:, i] / sel_dataset.data.max() * 100
            else:
                markers = np.zeros(self.loaded_data.nkpts)
            self.view.ax.scatter(self.loaded_data.xaxis, self.loaded_data.bands[0, :, i],
                                 s=markers, color=color, label=sel_dataset.name)

    def remove_dataset(self):
        """
        Remove a dataset from dataset list
        """
        try:
            to_remove = self.view.datasets_list.currentItem().text()
            while to_remove in [line._label for line in self.view.ax._children]:
                for line in self.view.ax._children:
                    if line._label == to_remove:
                        line.remove()
        except Exception:
            self.view.dataset_label.setText("Select a dataset to remove")
            QTest.qWait(2000)
            self.view.dataset_label.setText("Select atoms and states, and add them to datasets")
        self.populate_items()
        self.toggle_plot()

    def populate_items(self):
        """
        Refresh content of dataset list
        """
        self.view.datasets_list.clear()
        labels = []
        for line in self.view.ax._children:
            if "_" not in line._label:
                labels.append(line._label)
        labels = list(set(labels))
        labels.remove("main")
        for label in labels:
            self.view.datasets_list.addItem(f"{label}")

    def plot_basic_bands(self):
        if self.view.ax.lines:
            low, high = self.view.ax.get_ylim()
        else:
            low, high = self.loaded_data.bands.min() - 1, self.loaded_data.bands.max() + 1
        for i in range(self.loaded_data.nbands):
            self.view.ax.plot(self.loaded_data.xaxis, self.loaded_data.bands[0, :, i], color="black", label="main")
        self.view.ax.hlines(0, 0, self.loaded_data.xaxis[-1], color="black", ls="--")
        vlines = self.loaded_data.xaxis[np.where(self.loaded_data.xaxis[1:] - self.loaded_data.xaxis[:-1] == 0)]
        vlines = np.insert(vlines, 0, 0)
        vlines = np.append(vlines, self.loaded_data.xaxis.max())
        self.view.ax.set_ylim([low, high])
        self.view.ax.vlines(vlines, low, high, color="black", ls="dotted")
        self.view.ax.set_xlim([self.loaded_data.xaxis.min(), self.loaded_data.xaxis.max()])
        self.view.ax.set_xticks(vlines)
        self.view.ax.set_xticklabels([])
        self.view.canvas.draw()

    def toggle_plot(self):
        self.view.canvas.draw()

    def refresh_plot(self):
        self.add_kpoints()
        self.view.canvas.draw()

    def add_kpoints(self):
        kpoints = self.view.kpoint_text.text().upper().replace(",", " ").replace("G", "Γ").split()
        if len(kpoints) == len(self.view.ax.get_xticks()):
            self.view.ax.set_xticklabels(kpoints)
        else:
            self.view.dataset_label.setText("Invalid k-point list")
            QTest.qWait(2000)
            self.view.dataset_label.setText("Add datasets by selecting atoms and states, or plot datasets")


def main():
    """
    Main function - creates an instance of window (view)
    and applies controller to it
    """
    app = QApplication([])
    view = BandsAppView()
    BandsAppController(view)
    view.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
