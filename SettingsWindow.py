# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName("SettingDialog")
        SettingDialog.resize(441, 621)
        SettingDialog.setMinimumSize(QtCore.QSize(0, 0))
        SettingDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget = QtWidgets.QTabWidget(SettingDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 131))
        self.groupBox.setObjectName("groupBox")
        self.quietCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.quietCheckBox.setGeometry(QtCore.QRect(10, 20, 371, 18))
        self.quietCheckBox.setObjectName("quietCheckBox")
        self.verboseCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.verboseCheckBox.setGeometry(QtCore.QRect(10, 40, 371, 18))
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.warningsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.warningsCheckBox.setGeometry(QtCore.QRect(10, 60, 371, 18))
        self.warningsCheckBox.setObjectName("warningsCheckBox")
        self.ignoreCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.ignoreCheckBox.setGeometry(QtCore.QRect(10, 80, 371, 18))
        self.ignoreCheckBox.setObjectName("ignoreCheckBox")
        self.overwriteCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.overwriteCheckBox.setGeometry(QtCore.QRect(10, 100, 371, 18))
        self.overwriteCheckBox.setObjectName("overwriteCheckBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 401, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 401, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 391, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.forceurl = QtWidgets.QCheckBox(self.groupBox_2)
        self.forceurl.setGeometry(QtCore.QRect(10, 20, 371, 18))
        self.forceurl.setObjectName("forceurl")
        self.forcetitle = QtWidgets.QCheckBox(self.groupBox_2)
        self.forcetitle.setGeometry(QtCore.QRect(10, 40, 371, 18))
        self.forcetitle.setObjectName("forcetitle")
        self.forceid = QtWidgets.QCheckBox(self.groupBox_2)
        self.forceid.setGeometry(QtCore.QRect(10, 60, 371, 18))
        self.forceid.setObjectName("forceid")
        self.forcethumbnail = QtWidgets.QCheckBox(self.groupBox_2)
        self.forcethumbnail.setGeometry(QtCore.QRect(10, 80, 371, 18))
        self.forcethumbnail.setObjectName("forcethumbnail")
        self.forcedescription = QtWidgets.QCheckBox(self.groupBox_2)
        self.forcedescription.setGeometry(QtCore.QRect(10, 100, 371, 18))
        self.forcedescription.setObjectName("forcedescription")
        self.forcefilename = QtWidgets.QCheckBox(self.groupBox_2)
        self.forcefilename.setGeometry(QtCore.QRect(10, 120, 371, 18))
        self.forcefilename.setObjectName("forcefilename")
        self.forceduration = QtWidgets.QCheckBox(self.groupBox_2)
        self.forceduration.setGeometry(QtCore.QRect(10, 140, 371, 18))
        self.forceduration.setObjectName("forceduration")
        self.forcejson = QtWidgets.QCheckBox(self.groupBox_2)
        self.forcejson.setGeometry(QtCore.QRect(10, 160, 371, 18))
        self.forcejson.setObjectName("forcejson")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 391, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.age_limit = QtWidgets.QLineEdit(self.groupBox_3)
        self.age_limit.setGeometry(QtCore.QRect(100, 20, 71, 20))
        self.age_limit.setObjectName("age_limit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 371, 21))
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.min_views = QtWidgets.QLineEdit(self.groupBox_3)
        self.min_views.setGeometry(QtCore.QRect(100, 50, 71, 20))
        self.min_views.setObjectName("min_views")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 371, 21))
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.max_views = QtWidgets.QLineEdit(self.groupBox_3)
        self.max_views.setGeometry(QtCore.QRect(100, 80, 71, 20))
        self.max_views.setObjectName("max_views")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 371, 21))
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.record_file = QtWidgets.QLineEdit(self.groupBox_3)
        self.record_file.setGeometry(QtCore.QRect(100, 110, 71, 20))
        self.record_file.setObjectName("record_file")
        self.select_record_file_button = QtWidgets.QPushButton(self.groupBox_3)
        self.select_record_file_button.setGeometry(QtCore.QRect(180, 110, 31, 21))
        self.select_record_file_button.setObjectName("select_record_file_button")
        self.tabWidget.addTab(self.tab_3, "")
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 590, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(SettingDialog)
        self.tabWidget.setCurrentIndex(2)
        self.quietCheckBox.toggled['bool'].connect(self.verboseCheckBox.setDisabled)
        self.quietCheckBox.toggled['bool'].connect(self.warningsCheckBox.setDisabled)
        self.buttonBox.rejected.connect(SettingDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingDialog.setWindowTitle(_translate("SettingDialog", "Settings"))
        self.groupBox.setTitle(_translate("SettingDialog", "Software Settings"))
        self.quietCheckBox.setText(_translate("SettingDialog", "Quiet mode"))
        self.verboseCheckBox.setText(_translate("SettingDialog", "Verbose Mode"))
        self.warningsCheckBox.setText(_translate("SettingDialog", "No warnings"))
        self.ignoreCheckBox.setText(_translate("SettingDialog", "Ignore errors"))
        self.overwriteCheckBox.setText(_translate("SettingDialog", "Prevent file overwrite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingDialog", "Main"))
        self.label.setText(_translate("SettingDialog", "User name:"))
        self.label_2.setText(_translate("SettingDialog", "Password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingDialog", "User"))
        self.groupBox_2.setTitle(_translate("SettingDialog", "Force Options"))
        self.forceurl.setText(_translate("SettingDialog", "Force printing final URL"))
        self.forcetitle.setText(_translate("SettingDialog", "Force printing title"))
        self.forceid.setText(_translate("SettingDialog", "Force printing ID"))
        self.forcethumbnail.setText(_translate("SettingDialog", "Force printing thumbnail URL"))
        self.forcedescription.setText(_translate("SettingDialog", "Force printing description"))
        self.forcefilename.setText(_translate("SettingDialog", "Force printing final filenname"))
        self.forceduration.setText(_translate("SettingDialog", "Force printing duration"))
        self.forcejson.setText(_translate("SettingDialog", "Force printing info_dict as JSON"))
        self.groupBox_3.setTitle(_translate("SettingDialog", "Video Settings"))
        self.label_3.setText(_translate("SettingDialog", "Age limit: "))
        self.label_4.setText(_translate("SettingDialog", "Minimum views:"))
        self.label_5.setText(_translate("SettingDialog", "Maximum views: "))
        self.label_6.setText(_translate("SettingDialog", "Record file: "))
        self.select_record_file_button.setText(_translate("SettingDialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingDialog", "Video"))

