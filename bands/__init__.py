from sys import exit
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt6.QtTest import QTest
from PyQt6.QtCore import pyqtSignal, QObject
from bands.qtdesign import BandsAppWindow
from bands.vaspbandtools import BandStructure
from functools import partial
from os import name as osname
from os import path as ospath
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


class BandsAppController:

    def __init__(self, view):
        """
        connects buttons to functions
        :param view: BandsAppView instance
        """
        self.view = view
        self._disable_window()
        osys = osname
        if osys == "posix":
            self.home_path = "/Users"
        else:
            self.home_path = "C:\\"
        # Connecting buttons to functions
        self.view.atom_tabs.currentChanged.connect(self._clear_atom_tabs)
        self.view.states_tabs.currentChanged.connect(self._clear_states_tabs)
        self.view.browse_btn.clicked.connect(partial(self._browse, self.view))
        self.view.load_btn.clicked.connect(self._load_data)
        self.view.add_data_btn.clicked.connect(self._add_dataset)
        self.view.remove_data_btn.clicked.connect(self._remove_dataset)
        self.view.refresh_plot_btn.clicked.connect(self._toggle_plot)
        # path to sample file for debugging purposes
        # self.view.load_txt.setText(
        #     "/Users/adambialy/Documents/Coding/Python-portfolio/vasp-bands/AgF2-sample/bands/vasprun.xml")

    def _browse(self, view):
        """
        Browse directories
        """
        chosen_file = QFileDialog.getOpenFileName(view, "Choose file:", self.home_path, "(vasprun.xml)")[0]
        self.view.load_txt.setText(chosen_file)
        new_home_path = ospath.dirname(ospath.dirname(chosen_file))
        self.home_path = new_home_path

    def _load_data(self):
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
            self._toggle_plot()
            self._adjust_window()
            QTest.qWait(5)
            self.view.load_label.setText("Plotting...")
            QTest.qWait(5)
            self._plot_basic_bands()
            msg = f"<b>{self.loaded_data.name}</b> system was loaded successfully"
            self.view.load_label.setText(msg)
        except Exception as e:
            self.view.load_label.setText(e.args[0])
            QTest.qWait(2000)
            self.view.load_label.setText("Browse files and load a system")
            self._disable_window()

    def _adjust_window(self):
        """
        Method for selectively enabling functionalities in the window
        based on the loaded VASP data
        """
        self._disable_window()
        # enable and load atoms
        self.view.atom_sel_box.setEnabled(True)
        self.view.atom_comb.clear()
        self.view.atom_comb.addItems([""] + self.loaded_data.atomnames)
        # enable spin if spin-polarized
        if self.loaded_data.spin:
            self.view.spin_box.setEnabled(True)
        else:
            self.view.spin_box.setDisabled(True)
        # enable states and subshells
        self.view.states_box.setEnabled(True)
        self.view.subshell_tab.setEnabled(True)
        for level in self.loaded_data.subshells:
            self.view.subshell_box_dict[level].setEnabled(True)
        # enable orbitals if lorbit is 11
        if self.loaded_data.lorbit == 10:
            self.view.orbital_tab.setDisabled(True)
        else:
            self.view.orbital_tab.setEnabled(True)
            for level in self.loaded_data.subshells:
                for box in self.view.orbital_box_dict[level]:
                    box.setEnabled(True)
        # enable processing buttons
        for btn in self.view.dataset_btns:
            btn.setEnabled(True)
        self.view.datasets_list.setEnabled(True)
        self.view.datasets_list.clear()
        self.view.properties_box.setEnabled(True)

    def _disable_window(self):
        """
        Method for disabling functions in the window
        """
        self.view.atom_sel_box.setDisabled(True)
        self._reset_input()
        self.view.states_box.setDisabled(True)
        self.view.spin_box.setDisabled(True)
        for btn in self.view.dataset_btns:
            btn.setDisabled(True)
        self.view.datasets_list.clear()
        self.view.datasets_list.setDisabled(True)
        for box in self.view.subshell_box_list:
            box.setDisabled(True)
        for box in self.view.orbital_box_list:
            box.setDisabled(True)
        self.view.properties_box.setDisabled(True)

    def _reset_input(self):
        """
        Resets selection in the window
        """
        self._clear_atom_tabs()
        self._clear_states_tabs()
        self.view.name_text.clear()
        self.view.color_comb.setCurrentIndex(0)
        self.view.spin_btn_group.setExclusive(False)
        for btn in self.view.spin_btn_list:
            btn.setChecked(False)
        self.view.spin_btn_group.setExclusive(True)

    def _clear_atom_tabs(self):
        """
        Method for resetting input in atom tabs
        """
        self.view.atom_comb.setCurrentIndex(0)
        self.view.atom_text.clear()

    def _clear_states_tabs(self):
        """
        Method for resetting input in states tabs
        """
        for box in self.view.subshell_box_list:
            box.setChecked(False)
        for box in self.view.orbital_box_list:
            box.setChecked(False)

    def _add_dataset(self):
        """
        Creates projected bands based on user selection and
        adds it to dataset list and to plot
        """
        if self.view.atom_tabs.currentIndex() == 0:
            atoms = [self.view.atom_comb.currentText()]
        else:
            atoms = self.view.atom_text.text().split()
            try:
                atoms = np.array(atoms).astype(int)
            except ValueError:
                atoms = np.array(atoms)
        states = []
        if self.view.states_tabs.currentIndex() == 0:
            for box in self.view.subshell_box_list:
                if box.isChecked():
                    states.append(box.text())
        else:
            for box in self.view.orbital_box_list:
                if box.isChecked():
                    states.append(box.text())
        states = np.array(states)
        if len(states) > 0:
            states[np.where(states == "dx2-y2")] = "dx2"
        if self.view.spin_box.isEnabled() and self.view.spin_btn_group.checkedButton() is not None:
            spin = self.view.spin_btn_group.checkedButton().text()
        else:
            spin = "both"
        color = self.view.color_comb.currentText()
        name = self.view.name_text.text()
        condition = (len(states) > 0) and (len(atoms) > 0) and \
                    (not np.isin("", atoms)) and (name != "") and (color != "")
        if condition:
            try:
                sel_dataset = self.loaded_data.select(atoms, states, spin, name)
                for i in range(self.loaded_data.nbands):
                    if sel_dataset.data.max() != 0:
                        markers = sel_dataset.data[:, i] / sel_dataset.data.max() * 100
                    else:
                        markers = np.zeros(self.loaded_data.nkpts)
                    self.view.ax.scatter(self.loaded_data.xaxis, self.loaded_data.bands[0, :, i],
                                         s=markers, color=color, label=sel_dataset.name)
                self.view.dataset_label.setText("Dataset successfully added")
                self._reset_input()
            except Exception as e:
                print(e)
                self.view.dataset_label.setText(e.args[0])
        else:
            self.view.dataset_label.setText("Make sure you made a valid (non-null) selection")
        self._toggle_plot()
        self._populate_items()
        QTest.qWait(2000)
        self.view.dataset_label.setText("Select atoms and states, and add them to datasets")

    def _remove_dataset(self):
        """
        Removes a dataset from dataset list
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
        self._populate_items()
        self._toggle_plot()

    def _populate_items(self):
        """
        Method for refreshing content of dataset list
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

    def _plot_basic_bands(self):
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

    def _toggle_plot(self):
        kpoints = self.view.kpoint_text.text().replace(",", " ").split()
        if kpoints:
            try:
                self.view.ax.set_xticklabels(kpoints)
            except Exception:
                self.view.dataset_label.setText("Invalid k-point list")
                QTest.qWait(2000)
                self.view.dataset_label.setText("Add datasets by selecting atoms and states, or plot datasets")
        self.view.canvas.draw()


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
