# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_widget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.title_input.setObjectName("title_input")
        self.verticalLayout.addWidget(self.title_input)
        self.year_spin = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.year_spin.setObjectName("year_spin")
        self.verticalLayout.addWidget(self.year_spin)
        self.genres_combo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genres_combo.sizePolicy().hasHeightForWidth())
        self.genres_combo.setSizePolicy(sizePolicy)
        self.genres_combo.setObjectName("genres_combo")
        self.verticalLayout.addWidget(self.genres_combo)
        self.duration_spin = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.duration_spin.setObjectName("duration_spin")
        self.verticalLayout.addWidget(self.duration_spin)
        self.errors = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errors.sizePolicy().hasHeightForWidth())
        self.errors.setSizePolicy(sizePolicy)
        self.errors.setText("")
        self.errors.setObjectName("errors")
        self.verticalLayout.addWidget(self.errors)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить!"))