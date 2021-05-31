# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtcrop.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from QtCrop.area_selector import AreaSelector
from QtCrop.area_selector import Workspace

import assets_rc

class Ui_QtCrop(object):
    def setupUi(self, QtCrop):
        if not QtCrop.objectName():
            QtCrop.setObjectName(u"QtCrop")
        QtCrop.resize(664, 576)
        QtCrop.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(QtCrop)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbar = QWidget(QtCrop)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.toolbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelX = QLabel(self.toolbar)
        self.labelX.setObjectName(u"labelX")

        self.horizontalLayout.addWidget(self.labelX)

        self.spinBoxX = QSpinBox(self.toolbar)
        self.spinBoxX.setObjectName(u"spinBoxX")
        self.spinBoxX.setMinimumSize(QSize(72, 0))
        self.spinBoxX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spinBoxX)

        self.labelY = QLabel(self.toolbar)
        self.labelY.setObjectName(u"labelY")

        self.horizontalLayout.addWidget(self.labelY)

        self.spinBoxY = QSpinBox(self.toolbar)
        self.spinBoxY.setObjectName(u"spinBoxY")
        self.spinBoxY.setMinimumSize(QSize(72, 0))
        self.spinBoxY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spinBoxY)

        self.labelW = QLabel(self.toolbar)
        self.labelW.setObjectName(u"labelW")

        self.horizontalLayout.addWidget(self.labelW)

        self.spinBoxW = QSpinBox(self.toolbar)
        self.spinBoxW.setObjectName(u"spinBoxW")
        self.spinBoxW.setMinimumSize(QSize(72, 0))
        self.spinBoxW.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spinBoxW)

        self.labelH = QLabel(self.toolbar)
        self.labelH.setObjectName(u"labelH")

        self.horizontalLayout.addWidget(self.labelH)

        self.spinBoxH = QSpinBox(self.toolbar)
        self.spinBoxH.setObjectName(u"spinBoxH")
        self.spinBoxH.setMinimumSize(QSize(72, 0))
        self.spinBoxH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spinBoxH)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.toolbar)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.toolbar)

        self.line = QFrame(QtCrop)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(QtCrop)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.workspace = Workspace()
        self.workspace.setObjectName(u"workspace")
        self.workspace.setGeometry(QRect(0, 0, 638, 478))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(51, 51, 51, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.workspace.setPalette(palette)
        self.gridLayout = QGridLayout(self.workspace)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 224, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.frame = QFrame(self.workspace)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.selector = AreaSelector(self.frame)
        self.selector.setObjectName(u"selector")
        self.selector.setStyleSheet(u"background:url(:/img/grid-pattern.png);")
        self.selector.setFrameShape(QFrame.NoFrame)
        self.selector.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.selector)


        self.gridLayout.addWidget(self.frame, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(305, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.workspace)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(QtCrop)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(QtCrop)
        self.buttonBox.accepted.connect(QtCrop.accept)
        self.buttonBox.rejected.connect(QtCrop.reject)
        self.selector.area_changed.connect(QtCrop.update_crop_values)
        self.spinBoxX.valueChanged.connect(QtCrop.update_crop_area)
        self.spinBoxY.valueChanged.connect(QtCrop.update_crop_area)
        self.spinBoxW.valueChanged.connect(QtCrop.update_crop_area)
        self.spinBoxH.valueChanged.connect(QtCrop.update_crop_area)
        self.pushButton.clicked.connect(QtCrop.reset_crop_values)

        QMetaObject.connectSlotsByName(QtCrop)
    # setupUi

    def retranslateUi(self, QtCrop):
        QtCrop.setWindowTitle(QCoreApplication.translate("", u"QtCrop", None))
        self.labelX.setText(QCoreApplication.translate("", u"X:", None))
        self.spinBoxX.setSuffix(QCoreApplication.translate("", u"px", None))
        self.labelY.setText(QCoreApplication.translate("", u"Y:", None))
        self.spinBoxY.setSuffix(QCoreApplication.translate("", u"px", None))
        self.labelW.setText(QCoreApplication.translate("", u"Width:", None))
        self.spinBoxW.setSuffix(QCoreApplication.translate("", u"px", None))
        self.labelH.setText(QCoreApplication.translate("", u"Height:", None))
        self.spinBoxH.setSuffix(QCoreApplication.translate("", u"px", None))
        self.pushButton.setText(QCoreApplication.translate("", u"Reset", None))
        self.selector.setText("")
    # retranslateUi

