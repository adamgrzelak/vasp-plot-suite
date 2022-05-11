"""
Application for plotting electronic density of states (eDOS) graphs
from VASP calculation output
Frontend based on PyQt6
Backend is handled by VASP-DOS-tools mini-library
Developed by AG
(C) 2022
"""

from sys import exit
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt6.QtTest import QTest
from PyQt6.QtCore import pyqtSignal, QObject
from dos.qtdesign import DosAppWindow
import dos.vaspdostools as vdt
from controller import AppController
from functools import partial
from os import path as ospath
import numpy as np


class Signal(QObject):
    closed = pyqtSignal()


class DosAppView(QDialog, DosAppWindow):
    """
    Main window object
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.signal = Signal()

    def closeEvent(self, e):
        self.signal.closed.emit()


class DosAppController(AppController):
    def __init__(self, view):
        """
        connects buttons to functions
        :param view: DosAppView instance
        """
        super().__init__(view)
        # Connecting buttons to functions
        self.view.browse_btn.clicked.connect(partial(self.browse, self.view))
        self.view.load_btn.clicked.connect(self.load_data)
        self.view.add_data_btn.clicked.connect(self.add_dataset)
        self.view.add_total_btn.clicked.connect(self.add_total_dos)
        self.view.remove_data_btn.clicked.connect(self.remove_dataset)
        self.view.export_data_btn.clicked.connect(self.export_dataset)
        self.view.refresh_plot_btn.clicked.connect(self.toggle_plot)
        # path to sample file for debugging purposes
        self.view.load_txt.setText(
            "/Users/adambialy/Documents/Coding/Python-portfolio/vasp-integrated/AgF2-sample/dos/vasprun.xml")

    def browse(self, view):
        """
        Browse directories
        """
        chosen_file = QFileDialog.getOpenFileName(view, "Choose file:", self.home_path, "(vasprun.xml)")[0]
        self.view.load_txt.setText(chosen_file)
        new_home_path = ospath.dirname(ospath.dirname(chosen_file))
        self.home_path = new_home_path

    def load_data(self):
        """
        Load VASP output into a Dos object
        """
        for line in self.view.ax.lines:
            self.view.ax.lines.remove(line)
        self.toggle_plot()
        self.view.load_label.setText("Loading...")
        QTest.qWait(100)
        self.active_path = self.view.load_txt.text()
        try:
            self.selected_datasets = {}
            path_to_file = self.view.load_txt.text()
            self.loaded_data = vdt.extract(path_to_file)
            # account for different shorthands for dx2-y2 orbital depending on VASP version
            if "x2-y2" in self.loaded_data.levels:
                self.loaded_data.levels[np.where(self.loaded_data.levels == "x2-y2")] = "dx2"
                self.loaded_data.leveldict["dx2"] = self.loaded_data.leveldict.pop("x2-y2")
            msg = f"<b>{self.loaded_data.name}</b> system was loaded successfully"
            self.view.load_label.setText(msg)
            self.adjust_window()
        except Exception as e:
            self.view.load_label.setText(e.args[0])
            QTest.qWait(2000)
            self.view.load_label.setText("Browse files and load a system")
            self.disable_window()

    def adjust_window(self):
        """
        Method for selectively enabling functionalities in the window
        based on the loaded VASP data
        """
        self.disable_window()
        # enable and load atoms
        self.view.atom_sel_box.setEnabled(True)
        self.view.atom_comb.clear()
        self.view.atom_comb.addItems([""]+self.loaded_data.atomnames)
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

    def add_dataset(self):
        """
        Creates resolved DOS based on user selection and
        adds it to dataset list
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
                self.view.ax.plot(sel_dataset.dos[:, 0], sel_dataset.dos[:, 1],
                                  color=color, label=sel_dataset.name,
                                  linewidth=4)
                self.view.dataset_label.setText("Dataset successfully added")
                self.reset_input()
            except Exception as e:
                print(e)
                self.view.dataset_label.setText(e.args[0])
        else:
            self.view.dataset_label.setText("Make sure you made a valid (non-null) selection")
        self.populate_items()
        self.toggle_plot()
        QTest.qWait(2000)
        self.view.dataset_label.setText("Select atoms and states, and add them to datasets")

    def add_total_dos(self):
        """
        Selects total DOS from the Dos object and
        adds it to dataset list
        """
        if self.view.spin_box.isEnabled() and self.view.spin_btn_group.checkedButton() is not None:
            spin = self.view.spin_btn_group.checkedButton().text()
        else:
            spin = "both"
        color = self.view.color_comb.currentText()
        if color == "":
            color = "black"
        sel_dataset = self.loaded_data.get_total(spin)
        self.view.ax.plot(sel_dataset.dos[:, 0], sel_dataset.dos[:, 1],
                          color=color, label=sel_dataset.name,
                          linewidth=4)
        self.view.dataset_label.setText("Dataset successfully added")
        self.reset_input()
        self.populate_items()
        self.toggle_plot()
        QTest.qWait(2000)
        self.view.dataset_label.setText("Select atoms and states, and add them to datasets")

    def populate_items(self):
        """
        Functions for refreshing content of dataset list
        """
        self.view.datasets_list.clear()
        for line in self.view.ax.lines:
            self.view.datasets_list.addItem(f"{line._label}")

    def remove_dataset(self):
        """
        Removes a dataset from dataset list
        """
        if self.view.ax.lines:
            self.view.ax.lines.remove(self.view.ax.lines[self.view.datasets_list.currentRow()])
            self.populate_items()
        self.toggle_plot()

    def export_dataset(self):
        """
        Saves the selected dataset to .csv file
        (see DosLib documentation for details)
        """
        if len(self.view.ax.lines) > 0:
            to_save = self.view.ax.lines[self.view.datasets_list.currentRow()]
            path_to_save = ospath.dirname(self.active_path)
            np.savetxt(f"{path_to_save}/{to_save._label}.csv", to_save._xy, fmt='%.7f', delimiter=",")

    def toggle_plot(self):
        try:
            if len(self.view.ax.lines) > 0:
                low, high = self.view.ax.get_xlim()
                ymax = max([(line._y[np.where((line._x >= low) & (line._x <= high))]).max() for line in self.view.ax.lines]) * 1.1
                self.view.ax.set_ylim(0, ymax)
                self.view.ax.vlines(0, 0, ymax, colors='gray', linestyles='dashed', linewidth=4)
                self.legend = self.view.ax.legend(prop={'size': 15})
            else:
                if self.view.ax.get_legend():
                    self.view.ax.get_legend().remove()
        except Exception as e:
            self.view.dataset_label.setText(e.args[0])
            QTest.qWait(2000)
            self.view.dataset_label.setText("Add datasets by selecting atoms and states, or plot datasets")
        self.view.canvas.draw()
        self.populate_items()


def main():
    """
    Main function - creates an instance of window (view)
    and applies controller to it
    """
    app = QApplication([])
    view = DosAppView()
    DosAppController(view)
    view.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
