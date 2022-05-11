from functools import partial
from PyQt6.QtWidgets import QFileDialog
from os import name as osname


class AppController:
    """
    Generic controller class for use in DosApp and BandsApp modules.
    """

    def __init__(self, view):
        self.view = view
        self.disable_window()
        osys = osname
        if osys == "posix":
            self.home_path = "/Users"
        else:
            self.home_path = "C:\\"
        # Connecting buttons to functions
        self.view.atom_tabs.currentChanged.connect(self.clear_atom_tabs)
        self.view.states_tabs.currentChanged.connect(self.clear_states_tabs)


    def clear_atom_tabs(self):
        """
        Method for resetting input in atom tabs
        """
        self.view.atom_comb.setCurrentIndex(0)
        self.view.atom_text.clear()

    def clear_states_tabs(self):
        """
        Method for resetting input in states tabs
        """
        for box in self.view.subshell_box_list:
            box.setChecked(False)
        for box in self.view.orbital_box_list:
            box.setChecked(False)

    def reset_input(self):
        """
        Resets selection in the window
        """
        self.clear_atom_tabs()
        self.clear_states_tabs()
        self.view.name_text.clear()
        self.view.color_comb.setCurrentIndex(0)
        self.view.spin_btn_group.setExclusive(False)
        for btn in self.view.spin_btn_list:
            btn.setChecked(False)
        self.view.spin_btn_group.setExclusive(True)

    def disable_window(self):
        """
        Method for disabling functions in the window
        """
        self.view.atom_sel_box.setDisabled(True)
        self.reset_input()
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