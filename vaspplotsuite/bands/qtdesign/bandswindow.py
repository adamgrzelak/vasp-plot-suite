# Created by: PyQt6 UI code generator 6.2.3
import os

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
from PyQt6.QtCore import QMetaObject
from PyQt6.QtCore import QRect
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QButtonGroup
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QGroupBox
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QListWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QRadioButton
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QTabWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

from ...static import font


class BandsAppWindow(object):

    if os.name == "nt":
        q = 0.8
    else:
        q = 1
    font1 = QFont(font[0])
    font1.setPointSize(int(13 * q))
    font1.setWeight(QFont.Weight(75))
    font2 = QFont(font[0])
    font2.setPointSize(int(13 * q))
    font2.setWeight(QFont.Weight(50))
    font3 = QFont(font[0])
    font3.setPointSize(int(13 * q))

    def setupUi(self, main_window):
        # MAIN WINDOW INIT
        main_window.setObjectName("main_window")
        main_window.resize(1200, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(1200, 640))
        main_window.setMaximumSize(QSize(1200, 640))
        main_window.setAutoFillBackground(False)

        # SPIN SELECTION BOX
        self.spin_box = QGroupBox(main_window)
        self.spin_box.setGeometry(QRect(10, 250, 191, 61))
        self.spin_box.setFont(self.font1)
        self.spin_box.setFlat(False)
        self.spin_box.setCheckable(False)
        self.spin_box.setChecked(False)
        self.spin_box.setObjectName("spin_box")
        self.layoutWidget = QWidget(self.spin_box)
        self.layoutWidget.setGeometry(QRect(0, 30, 191, 20))
        self.layoutWidget.setObjectName("layoutWidget")
        self.spin_layout = QHBoxLayout(self.layoutWidget)
        self.spin_layout.setContentsMargins(0, 0, 0, 0)
        self.spin_layout.setObjectName("spin_layout")
        self.spin_both_btn = QRadioButton(self.layoutWidget)
        self.spin_both_btn.setFont(self.font2)
        self.spin_both_btn.setCheckable(True)
        self.spin_both_btn.setChecked(False)
        self.spin_both_btn.setObjectName("spin_both_btn")
        self.spin_layout.addWidget(self.spin_both_btn)
        self.spin_up_btn = QRadioButton(self.layoutWidget)
        self.spin_up_btn.setFont(self.font2)
        self.spin_up_btn.setCheckable(True)
        self.spin_up_btn.setChecked(False)
        self.spin_up_btn.setAutoExclusive(True)
        self.spin_up_btn.setObjectName("spin_up_btn")
        self.spin_layout.addWidget(self.spin_up_btn)
        self.spin_down_btn = QRadioButton(self.layoutWidget)
        self.spin_down_btn.setFont(self.font2)
        self.spin_down_btn.setCheckable(True)
        self.spin_down_btn.setChecked(False)
        self.spin_down_btn.setObjectName("spin_down_btn")
        self.spin_layout.addWidget(self.spin_down_btn)
        self.spin_btn_group = QButtonGroup()
        self.spin_btn_group.addButton(self.spin_both_btn)
        self.spin_btn_group.addButton(self.spin_up_btn)
        self.spin_btn_group.addButton(self.spin_down_btn)
        self.spin_btn_list = [self.spin_both_btn, self.spin_up_btn, self.spin_down_btn]

        # LOAD VASP DATA BOX
        self.load_box = QGroupBox(main_window)
        self.load_box.setGeometry(QRect(10, 10, 411, 91))
        self.load_box.setFont(self.font1)
        self.load_box.setObjectName("load_box")
        self.verticalLayout = QVBoxLayout(self.load_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.load_layout = QHBoxLayout()
        self.load_layout.setObjectName("load_layout")
        self.load_txt = QLineEdit(self.load_box)
        self.load_txt.setFont(self.font2)
        self.load_txt.setObjectName("load_txt")
        self.load_layout.addWidget(self.load_txt)
        self.browse_btn = QPushButton(self.load_box)
        self.browse_btn.setFont(self.font2)
        self.browse_btn.setObjectName("browse_btn")
        self.load_layout.addWidget(self.browse_btn)
        self.load_btn = QPushButton(self.load_box)
        self.load_btn.setFont(self.font2)
        self.load_btn.setObjectName("load_btn")
        self.load_layout.addWidget(self.load_btn)
        self.verticalLayout.addLayout(self.load_layout)

        # ATOM SELECTION BOX
        self.atom_sel_box = QGroupBox(main_window)
        self.atom_sel_box.setGeometry(QRect(10, 150, 191, 91))
        self.atom_sel_box.setFont(self.font1)
        self.atom_sel_box.setObjectName("atom_sel_box")
        self.atom_tabs = QTabWidget(self.atom_sel_box)
        self.atom_tabs.setGeometry(QRect(0, 20, 191, 71))
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atom_tabs.sizePolicy().hasHeightForWidth())
        self.atom_tabs.setSizePolicy(sizePolicy)
        self.atom_tabs.setFont(self.font2)
        self.atom_tabs.setAutoFillBackground(False)
        self.atom_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.atom_tabs.setIconSize(QSize(16, 16))
        self.atom_tabs.setTabsClosable(False)
        self.atom_tabs.setMovable(False)
        self.atom_tabs.setTabBarAutoHide(False)
        self.atom_tabs.setObjectName("atom_tab")
        self.atom_sel_tab = QWidget()
        self.atom_sel_tab.setObjectName("atom_sel_tab")
        self.atom_comb = QComboBox(self.atom_sel_tab)
        self.atom_comb.setGeometry(QRect(20, 10, 141, 26))
        self.atom_comb.setObjectName("atom_comb")
        self.atom_tabs.addTab(self.atom_sel_tab, "")
        self.atom_list_tab = QWidget()
        self.atom_list_tab.setObjectName("atom_list_tab")
        self.atom_text = QLineEdit(self.atom_list_tab)
        self.atom_text.setGeometry(QRect(10, 10, 161, 21))
        self.atom_text.setText("")
        self.atom_text.setObjectName("atom_text")
        self.atom_tabs.addTab(self.atom_list_tab, "")

        # STATES SELECTION BOX
        self.states_box = QGroupBox(main_window)
        self.states_box.setGeometry(QRect(220, 150, 201, 261))
        self.states_box.setFont(self.font1)
        self.states_box.setObjectName("states_box")
        self.states_tabs = QTabWidget(self.states_box)
        self.states_tabs.setGeometry(QRect(-1, 19, 201, 241))
        self.states_tabs.setFont(self.font2)
        self.states_tabs.setObjectName("states_tabs")
        # SUBSHELL TAB
        self.subshell_tab = QWidget()
        self.subshell_tab.setObjectName("subshell_tab")
        self.layoutWidget1 = QWidget(self.subshell_tab)
        self.layoutWidget1.setGeometry(QRect(80, 40, 41, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.subshell_layout = QVBoxLayout(self.layoutWidget1)
        self.subshell_layout.setContentsMargins(0, 0, 0, 0)
        self.subshell_layout.setObjectName("subshell_layout")
        self.ss_box = QCheckBox(self.layoutWidget1)
        self.ss_box.setFont(self.font2)
        self.ss_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ss_box.setCheckable(True)
        self.ss_box.setChecked(False)
        self.ss_box.setTristate(False)
        self.ss_box.setObjectName("ss_box")
        self.subshell_layout.addWidget(self.ss_box)
        self.pp_box = QCheckBox(self.layoutWidget1)
        self.pp_box.setFont(self.font2)
        self.pp_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pp_box.setCheckable(True)
        self.pp_box.setChecked(False)
        self.pp_box.setTristate(False)
        self.pp_box.setObjectName("pp_box")
        self.subshell_layout.addWidget(self.pp_box)
        self.dd_box = QCheckBox(self.layoutWidget1)
        self.dd_box.setFont(self.font2)
        self.dd_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dd_box.setCheckable(True)
        self.dd_box.setChecked(False)
        self.dd_box.setTristate(False)
        self.dd_box.setObjectName("dd_box")
        self.subshell_layout.addWidget(self.dd_box)
        self.ff_box = QCheckBox(self.layoutWidget1)
        self.ff_box.setFont(self.font2)
        self.ff_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ff_box.setCheckable(True)
        self.ff_box.setChecked(False)
        self.ff_box.setTristate(False)
        self.ff_box.setObjectName("ff_box")
        self.subshell_layout.addWidget(self.ff_box)
        self.states_tabs.addTab(self.subshell_tab, "")
        self.subshell_box_dict = {
            "s": self.ss_box,
            "p": self.pp_box,
            "d": self.dd_box,
            "f": self.ff_box,
        }
        self.subshell_box_list = self.subshell_box_dict.values()

        # ORBITAL TAB
        self.orbital_tab = QWidget()
        self.orbital_tab.setObjectName("orbital_tab")
        self.layoutWidget_2 = QWidget(self.orbital_tab)
        self.layoutWidget_2.setGeometry(QRect(10, 0, 181, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.orbital_grid = QGridLayout(self.layoutWidget_2)
        self.orbital_grid.setContentsMargins(0, 0, 0, 0)
        self.orbital_grid.setObjectName("orbital_grid")
        self.f1_box = QCheckBox(self.layoutWidget_2)
        self.f1_box.setFont(self.font2)
        self.f1_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.f1_box.setCheckable(True)
        self.f1_box.setChecked(False)
        self.f1_box.setTristate(False)
        self.f1_box.setObjectName("f1_box")
        self.orbital_grid.addWidget(self.f1_box, 5, 1, 1, 1)
        self.dxy_box = QCheckBox(self.layoutWidget_2)
        self.dxy_box.setFont(self.font2)
        self.dxy_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dxy_box.setCheckable(True)
        self.dxy_box.setChecked(False)
        self.dxy_box.setTristate(False)
        self.dxy_box.setObjectName("dxy_box")
        self.orbital_grid.addWidget(self.dxy_box, 2, 0, 1, 1)
        self.fn2_box = QCheckBox(self.layoutWidget_2)
        self.fn2_box.setFont(self.font2)
        self.fn2_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.fn2_box.setCheckable(True)
        self.fn2_box.setChecked(False)
        self.fn2_box.setTristate(False)
        self.fn2_box.setObjectName("fn2_box")
        self.orbital_grid.addWidget(self.fn2_box, 4, 1, 1, 1)
        self.fn1_box = QCheckBox(self.layoutWidget_2)
        self.fn1_box.setFont(self.font2)
        self.fn1_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.fn1_box.setCheckable(True)
        self.fn1_box.setChecked(False)
        self.fn1_box.setTristate(False)
        self.fn1_box.setObjectName("fn1_box")
        self.orbital_grid.addWidget(self.fn1_box, 4, 2, 1, 1)
        self.f0_box = QCheckBox(self.layoutWidget_2)
        self.f0_box.setFont(self.font2)
        self.f0_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.f0_box.setCheckable(True)
        self.f0_box.setChecked(False)
        self.f0_box.setTristate(False)
        self.f0_box.setObjectName("f0_box")
        self.orbital_grid.addWidget(self.f0_box, 5, 0, 1, 1)
        self.dyz_box = QCheckBox(self.layoutWidget_2)
        self.dyz_box.setFont(self.font2)
        self.dyz_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dyz_box.setCheckable(True)
        self.dyz_box.setChecked(False)
        self.dyz_box.setTristate(False)
        self.dyz_box.setObjectName("dyz_box")
        self.orbital_grid.addWidget(self.dyz_box, 2, 1, 1, 1)
        self.dxz_box = QCheckBox(self.layoutWidget_2)
        self.dxz_box.setFont(self.font2)
        self.dxz_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dxz_box.setCheckable(True)
        self.dxz_box.setChecked(False)
        self.dxz_box.setTristate(False)
        self.dxz_box.setObjectName("dxz_box")
        self.orbital_grid.addWidget(self.dxz_box, 3, 0, 1, 1)
        self.px_box = QCheckBox(self.layoutWidget_2)
        self.px_box.setFont(self.font2)
        self.px_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.px_box.setCheckable(True)
        self.px_box.setChecked(False)
        self.px_box.setTristate(False)
        self.px_box.setObjectName("px_box")
        self.orbital_grid.addWidget(self.px_box, 1, 2, 1, 1)
        self.dx2_box = QCheckBox(self.layoutWidget_2)
        self.dx2_box.setFont(self.font2)
        self.dx2_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dx2_box.setCheckable(True)
        self.dx2_box.setChecked(False)
        self.dx2_box.setTristate(False)
        self.dx2_box.setObjectName("dx2_box")
        self.orbital_grid.addWidget(self.dx2_box, 3, 1, 1, 1)
        self.dz2_box = QCheckBox(self.layoutWidget_2)
        self.dz2_box.setFont(self.font2)
        self.dz2_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.dz2_box.setCheckable(True)
        self.dz2_box.setChecked(False)
        self.dz2_box.setTristate(False)
        self.dz2_box.setObjectName("dz2_box")
        self.orbital_grid.addWidget(self.dz2_box, 2, 2, 1, 1)
        self.fn3_box = QCheckBox(self.layoutWidget_2)
        self.fn3_box.setFont(self.font2)
        self.fn3_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.fn3_box.setCheckable(True)
        self.fn3_box.setChecked(False)
        self.fn3_box.setTristate(False)
        self.fn3_box.setObjectName("fn3_box")
        self.orbital_grid.addWidget(self.fn3_box, 4, 0, 1, 1)
        self.s_box = QCheckBox(self.layoutWidget_2)
        self.s_box.setFont(self.font2)
        self.s_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.s_box.setCheckable(True)
        self.s_box.setChecked(False)
        self.s_box.setTristate(False)
        self.s_box.setObjectName("s_box")
        self.orbital_grid.addWidget(self.s_box, 0, 0, 1, 1)
        self.py_box = QCheckBox(self.layoutWidget_2)
        self.py_box.setFont(self.font2)
        self.py_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.py_box.setCheckable(True)
        self.py_box.setChecked(False)
        self.py_box.setTristate(False)
        self.py_box.setObjectName("py_box")
        self.orbital_grid.addWidget(self.py_box, 1, 0, 1, 1)
        self.pz_box = QCheckBox(self.layoutWidget_2)
        self.pz_box.setFont(self.font2)
        self.pz_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pz_box.setCheckable(True)
        self.pz_box.setChecked(False)
        self.pz_box.setTristate(False)
        self.pz_box.setObjectName("pz_box")
        self.orbital_grid.addWidget(self.pz_box, 1, 1, 1, 1)
        self.f2_box = QCheckBox(self.layoutWidget_2)
        self.f2_box.setFont(self.font2)
        self.f2_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.f2_box.setCheckable(True)
        self.f2_box.setChecked(False)
        self.f2_box.setTristate(False)
        self.f2_box.setObjectName("f2_box")
        self.orbital_grid.addWidget(self.f2_box, 5, 2, 1, 1)
        self.f3_box = QCheckBox(self.layoutWidget_2)
        self.f3_box.setFont(self.font2)
        self.f3_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.f3_box.setCheckable(True)
        self.f3_box.setChecked(False)
        self.f3_box.setTristate(False)
        self.f3_box.setObjectName("f3_box")
        self.orbital_grid.addWidget(self.f3_box, 6, 0, 1, 1)
        self.states_tabs.addTab(self.orbital_tab, "")
        self.orbital_box_dict = {
            "s": [self.s_box],
            "p": [self.py_box, self.pz_box, self.px_box],
            "d": [self.dxy_box, self.dyz_box, self.dz2_box, self.dxz_box, self.dx2_box],
            "f": [
                self.fn3_box,
                self.fn2_box,
                self.fn1_box,
                self.f0_box,
                self.f1_box,
                self.f2_box,
                self.f3_box,
            ],
        }
        self.orbital_box_list = [
            box for value in self.orbital_box_dict.values() for box in value
        ]

        # LOAD STATUS LABEL
        self.load_label = QLabel(main_window)
        self.load_label.setGeometry(QRect(10, 110, 411, 20))
        self.load_label.setFont(self.font3)
        self.load_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load_label.setObjectName("load_label")
        self.line1 = QFrame(main_window)
        self.line1.setGeometry(QRect(17, 130, 401, 20))
        self.line1.setFrameShape(QFrame.Shape.HLine)
        self.line1.setFrameShadow(QFrame.Shadow.Sunken)
        self.line1.setObjectName("line1")

        # PROPERTIES BOX
        self.properties_box = QGroupBox(main_window)
        self.properties_box.setGeometry(QRect(10, 320, 191, 91))
        self.properties_box.setFont(self.font1)
        self.properties_box.setObjectName("properties_box")
        self.layoutWidget2 = QWidget(self.properties_box)
        self.layoutWidget2.setGeometry(QRect(10, 30, 171, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.properties_layout = QVBoxLayout(self.layoutWidget2)
        self.properties_layout.setContentsMargins(0, 0, 0, 0)
        self.properties_layout.setObjectName("properties_layout")
        self.name_text = QLineEdit(self.layoutWidget2)
        self.name_text.setFont(self.font2)
        self.name_text.setText("")
        self.name_text.setObjectName("name_text")
        self.properties_layout.addWidget(self.name_text)
        self.color_comb = QComboBox(self.layoutWidget2)
        self.color_comb.setObjectName("color_comb")
        self.color_comb.addItems(
            ["", "red", "cyan", "green", "magenta", "blue", "yellow"]
        )
        self.properties_layout.addWidget(self.color_comb)

        # DATASET LABEL
        self.line2 = QFrame(main_window)
        self.line2.setGeometry(QRect(10, 440, 411, 20))
        self.line2.setFrameShape(QFrame.Shape.HLine)
        self.line2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line2.setObjectName("line2")
        self.dataset_label = QLabel(main_window)
        self.dataset_label.setGeometry(QRect(10, 420, 411, 20))
        self.dataset_label.setFont(self.font3)
        self.dataset_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dataset_label.setObjectName("dataset_label")

        # DATASETS BOX
        self.datasets_box = QGroupBox(main_window)
        self.datasets_box.setGeometry(QRect(220, 455, 200, 173))
        self.datasets_box.setFont(self.font1)
        self.datasets_box.setObjectName("datasets_box")
        self.datasets_list = QListWidget(self.datasets_box)
        self.datasets_list.setGeometry(QRect(0, 19, 200, 155))
        self.datasets_list.setObjectName("datasets_list")

        # DATASET BUTTONS
        self.widget = QWidget(main_window)
        self.widget.setGeometry(QRect(10, 460, 191, 180))
        self.widget.setObjectName("widget")
        self.dataset_btn_layout = QVBoxLayout(self.widget)
        self.dataset_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.dataset_btn_layout.setObjectName("dataset_btn_layout")
        self.add_data_btn = QPushButton(self.widget)
        self.add_data_btn.setObjectName("add_data_btn")
        self.add_data_btn.setFont(self.font3)
        self.dataset_btn_layout.addWidget(self.add_data_btn)
        self.remove_data_btn = QPushButton(self.widget)
        self.remove_data_btn.setObjectName("remove_data_btn")
        self.remove_data_btn.setFont(self.font3)
        self.dataset_btn_layout.addWidget(self.remove_data_btn)
        self.kpoint_text = QLineEdit(self.widget)
        self.kpoint_text.setFont(self.font2)
        self.kpoint_text.setText("")
        self.kpoint_text.setObjectName("kpoint_text")
        self.kpoint_text.setFont(self.font3)
        self.dataset_btn_layout.addWidget(self.kpoint_text)
        self.refresh_plot_btn = QPushButton(self.widget)
        self.refresh_plot_btn.setObjectName("refresh_plot_btn")
        self.refresh_plot_btn.setFont(self.font3)
        self.dataset_btn_layout.addWidget(self.refresh_plot_btn)

        self.dataset_btns = [
            self.add_data_btn,
            self.remove_data_btn,
            self.kpoint_text,
            self.refresh_plot_btn,
        ]

        # PLOT SECTION
        self.plot_widget = QWidget(main_window)
        self.plot_widget.setGeometry(QRect(431, 10, 760, 630))
        self.plot_layout = QtWidgets.QVBoxLayout(self.plot_widget)
        self.canvas = FigureCanvas(Figure())
        self.canvas.figure.set_tight_layout(True)
        self.plot_layout.addWidget(self.canvas)
        self.plot_layout.addWidget(NavigationToolbar(self.canvas, self))
        self.ax = self.canvas.figure.subplots()
        self.ax.set_xlabel("k", fontsize=20)
        self.ax.set_ylabel("E [eV]", fontsize=20)
        self.ax.tick_params(width=1, length=5, labelsize=20)

        self.retranslateUi(main_window)
        self.atom_tabs.setCurrentIndex(0)
        self.states_tabs.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle("BandsApp © AG")
        self.spin_box.setTitle("Spin:")
        self.spin_both_btn.setText("both")
        self.spin_up_btn.setText("up")
        self.spin_down_btn.setText("down")
        self.load_box.setTitle("Load VASP output")
        self.load_txt.setPlaceholderText("Select directory...")
        self.browse_btn.setText("Browse...")
        self.load_btn.setText("Load")
        self.atom_sel_box.setTitle("Atoms:")
        self.atom_tabs.setTabText(self.atom_tabs.indexOf(self.atom_sel_tab), "Select")
        self.atom_text.setPlaceholderText("List atoms...")
        self.atom_tabs.setTabText(self.atom_tabs.indexOf(self.atom_list_tab), "List")
        self.states_box.setTitle("States:")
        self.ss_box.setText("s")
        self.pp_box.setText("p")
        self.dd_box.setText("d")
        self.ff_box.setText("f")
        self.states_tabs.setTabText(
            self.states_tabs.indexOf(self.subshell_tab), "Subshells"
        )
        self.f1_box.setText("f(1)")
        self.dxy_box.setText("dxy")
        self.fn2_box.setText("f(-2)")
        self.fn1_box.setText("f(-1)")
        self.f0_box.setText("f(0)")
        self.dyz_box.setText("dyz")
        self.dxz_box.setText("dxz")
        self.px_box.setText("px")
        self.dx2_box.setText("dx2-y2")
        self.dz2_box.setText("dz2")
        self.fn3_box.setText("f(-3)")
        self.s_box.setText("s")
        self.py_box.setText("py")
        self.pz_box.setText("pz")
        self.f2_box.setText("f(2)")
        self.f3_box.setText("f(3)")
        self.states_tabs.setTabText(
            self.states_tabs.indexOf(self.orbital_tab), "Orbitals"
        )
        self.load_label.setText("Browse files and load a system")
        self.properties_box.setTitle("Properties")
        self.name_text.setPlaceholderText("Enter display name...")
        self.datasets_box.setTitle("Datasets")
        self.dataset_label.setText("Select atoms and states, and add them to datasets")
        self.add_data_btn.setText("Add dataset")
        self.remove_data_btn.setText("Remove dataset")
        self.kpoint_text.setPlaceholderText("Enter a list of k-points...")
        self.refresh_plot_btn.setText("Refresh plot")
