# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/elias/PycharmProjects/mpvQC/gui/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreferencesView(object):
    def setupUi(self, PreferencesView):
        PreferencesView.setObjectName("PreferencesView")
        PreferencesView.resize(700, 551)
        PreferencesView.setMinimumSize(QtCore.QSize(700, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(PreferencesView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(PreferencesView)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_13 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.navigationList = QtWidgets.QListWidget(self.widget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigationList.sizePolicy().hasHeightForWidth())
        self.navigationList.setSizePolicy(sizePolicy)
        self.navigationList.setMinimumSize(QtCore.QSize(130, 0))
        self.navigationList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.navigationList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.navigationList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.navigationList.setLineWidth(0)
        self.navigationList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.navigationList.setProperty("showDropIndicator", False)
        self.navigationList.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.navigationList.setAlternatingRowColors(False)
        self.navigationList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.navigationList.setTextElideMode(QtCore.Qt.ElideRight)
        self.navigationList.setMovement(QtWidgets.QListView.Static)
        self.navigationList.setResizeMode(QtWidgets.QListView.Fixed)
        self.navigationList.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.navigationList.setViewMode(QtWidgets.QListView.ListMode)
        self.navigationList.setUniformItemSizes(True)
        self.navigationList.setSelectionRectVisible(False)
        self.navigationList.setObjectName("navigationList")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("systemsettings")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("photocollage")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("mpv")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("text-editor")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("internet-archive")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon.fromTheme("help")
        item.setIcon(icon)
        self.navigationList.addItem(item)
        self.horizontalLayout_6.addWidget(self.navigationList)
        self.horizontalLayout.addWidget(self.widget_13)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageGeneral = QtWidgets.QWidget()
        self.pageGeneral.setObjectName("pageGeneral")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageGeneral)
        self.verticalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.pageGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.pageGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_5)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.authorLabel = QtWidgets.QLabel(self.widget_5)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.kTypesLineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.kTypesLineEdit.setObjectName("kTypesLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kTypesLineEdit)
        self.kTypesParentWidget = QtWidgets.QWidget(self.widget_5)
        self.kTypesParentWidget.setStyleSheet("QPushButton { text-align:left; padding: 8px; }")
        self.kTypesParentWidget.setObjectName("kTypesParentWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.kTypesParentWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.kTypesListWidget = QtWidgets.QListWidget(self.kTypesParentWidget)
        self.kTypesListWidget.setObjectName("kTypesListWidget")
        self.horizontalLayout_12.addWidget(self.kTypesListWidget)
        self.widget_19 = QtWidgets.QWidget(self.kTypesParentWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_19)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_18 = QtWidgets.QWidget(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.kTypesAddButton = QtWidgets.QPushButton(self.widget_18)
        self.kTypesAddButton.setEnabled(False)
        self.kTypesAddButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("add")
        self.kTypesAddButton.setIcon(icon)
        self.kTypesAddButton.setObjectName("kTypesAddButton")
        self.verticalLayout_15.addWidget(self.kTypesAddButton)
        self.kTypesRemoveButton = QtWidgets.QPushButton(self.widget_18)
        self.kTypesRemoveButton.setEnabled(False)
        self.kTypesRemoveButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("remove")
        self.kTypesRemoveButton.setIcon(icon)
        self.kTypesRemoveButton.setObjectName("kTypesRemoveButton")
        self.verticalLayout_15.addWidget(self.kTypesRemoveButton)
        self.kTypesMoveUpButton = QtWidgets.QPushButton(self.widget_18)
        self.kTypesMoveUpButton.setEnabled(False)
        self.kTypesMoveUpButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("arrow-up")
        self.kTypesMoveUpButton.setIcon(icon)
        self.kTypesMoveUpButton.setObjectName("kTypesMoveUpButton")
        self.verticalLayout_15.addWidget(self.kTypesMoveUpButton)
        self.kTypesMoveDownButton = QtWidgets.QPushButton(self.widget_18)
        self.kTypesMoveDownButton.setEnabled(False)
        self.kTypesMoveDownButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("arrow-down")
        self.kTypesMoveDownButton.setIcon(icon)
        self.kTypesMoveDownButton.setObjectName("kTypesMoveDownButton")
        self.verticalLayout_15.addWidget(self.kTypesMoveDownButton)
        self.verticalLayout_16.addWidget(self.widget_18)
        self.widget_20 = QtWidgets.QWidget(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy)
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_16.addWidget(self.widget_20)
        self.horizontalLayout_12.addWidget(self.widget_19)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kTypesParentWidget)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.pageGeneral)
        self.pageAppearance = QtWidgets.QWidget()
        self.pageAppearance.setObjectName("pageAppearance")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pageAppearance)
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_11 = QtWidgets.QWidget(self.pageAppearance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.verticalLayout_11.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.pageAppearance)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_12)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabGeneral = QtWidgets.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tabGeneral)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_14 = QtWidgets.QWidget(self.tabGeneral)
        self.widget_14.setObjectName("widget_14")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget_14)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.widget_14)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.window_title_combo_box = QtWidgets.QComboBox(self.widget_14)
        self.window_title_combo_box.setObjectName("window_title_combo_box")
        self.window_title_combo_box.addItem("")
        self.window_title_combo_box.addItem("")
        self.window_title_combo_box.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.window_title_combo_box)
        self.horizontalLayout_7.addWidget(self.widget_14)
        self.tabWidget_2.addTab(self.tabGeneral, "")
        self.horizontalLayout_4.addWidget(self.tabWidget_2)
        self.verticalLayout_11.addWidget(self.widget_12)
        self.stackedWidget.addWidget(self.pageAppearance)
        self.pageConfiguration = QtWidgets.QWidget()
        self.pageConfiguration.setObjectName("pageConfiguration")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pageConfiguration)
        self.verticalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_9 = QtWidgets.QWidget(self.pageConfiguration)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.verticalLayout_8.addWidget(self.widget_9)
        self.label_8 = QtWidgets.QLabel(self.pageConfiguration)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.widget_10 = QtWidgets.QWidget(self.pageConfiguration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_10)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mpv_conf_plain_text_edit = QtWidgets.QPlainTextEdit(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.mpv_conf_plain_text_edit.setFont(font)
        self.mpv_conf_plain_text_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mpv_conf_plain_text_edit.setObjectName("mpv_conf_plain_text_edit")
        self.horizontalLayout_2.addWidget(self.mpv_conf_plain_text_edit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_conf_plain_text_edit = QtWidgets.QPlainTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.input_conf_plain_text_edit.setFont(font)
        self.input_conf_plain_text_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.input_conf_plain_text_edit.setObjectName("input_conf_plain_text_edit")
        self.horizontalLayout_3.addWidget(self.input_conf_plain_text_edit)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_10.addWidget(self.tabWidget)
        self.verticalLayout_8.addWidget(self.widget_10)
        self.stackedWidget.addWidget(self.pageConfiguration)
        self.pageQcDocument = QtWidgets.QWidget()
        self.pageQcDocument.setObjectName("pageQcDocument")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pageQcDocument)
        self.verticalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.pageQcDocument)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.pageQcDocument)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_7)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.autoSaveEnabledCheckBox_4 = QtWidgets.QCheckBox(self.widget_7)
        self.autoSaveEnabledCheckBox_4.setChecked(True)
        self.autoSaveEnabledCheckBox_4.setObjectName("autoSaveEnabledCheckBox_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.autoSaveEnabledCheckBox_4)
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.autosaveSpinBox_4 = QtWidgets.QSpinBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autosaveSpinBox_4.sizePolicy().hasHeightForWidth())
        self.autosaveSpinBox_4.setSizePolicy(sizePolicy)
        self.autosaveSpinBox_4.setMinimum(15)
        self.autosaveSpinBox_4.setMaximum(1000)
        self.autosaveSpinBox_4.setObjectName("autosaveSpinBox_4")
        self.horizontalLayout_5.addWidget(self.autosaveSpinBox_4)
        self.autosaveTimeUnit_4 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autosaveTimeUnit_4.sizePolicy().hasHeightForWidth())
        self.autosaveTimeUnit_4.setSizePolicy(sizePolicy)
        self.autosaveTimeUnit_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.autosaveTimeUnit_4.setObjectName("autosaveTimeUnit_4")
        self.horizontalLayout_5.addWidget(self.autosaveTimeUnit_4)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget_8)
        self.saveNickNameCheckBox = QtWidgets.QCheckBox(self.widget_7)
        self.saveNickNameCheckBox.setObjectName("saveNickNameCheckBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saveNickNameCheckBox)
        self.saveVideoPathCheckBox = QtWidgets.QCheckBox(self.widget_7)
        self.saveVideoPathCheckBox.setObjectName("saveVideoPathCheckBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.saveVideoPathCheckBox)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.stackedWidget.addWidget(self.pageQcDocument)
        self.pageLanguage = QtWidgets.QWidget()
        self.pageLanguage.setObjectName("pageLanguage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageLanguage)
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.pageLanguage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.pageLanguage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.pageLanguage)
        self.pageAbout = QtWidgets.QWidget()
        self.pageAbout.setObjectName("pageAbout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.pageAbout)
        self.verticalLayout_13.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_15 = QtWidgets.QWidget(self.pageAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.verticalLayout_13.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.pageAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.widget_16)
        self.tabWidget_3.setDocumentMode(True)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.sdasd = QtWidgets.QWidget()
        self.sdasd.setObjectName("sdasd")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.sdasd)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.aboutBrowser = QtWidgets.QTextBrowser(self.sdasd)
        self.aboutBrowser.setObjectName("aboutBrowser")
        self.horizontalLayout_9.addWidget(self.aboutBrowser)
        self.tabWidget_3.addTab(self.sdasd, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.creditsBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.creditsBrowser.setHtml("")
        self.creditsBrowser.setObjectName("creditsBrowser")
        self.horizontalLayout_10.addWidget(self.creditsBrowser)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.licenceBrowser = QtWidgets.QTextBrowser(self.tab_5)
        self.licenceBrowser.setHtml("")
        self.licenceBrowser.setObjectName("licenceBrowser")
        self.horizontalLayout_11.addWidget(self.licenceBrowser)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.horizontalLayout_8.addWidget(self.tabWidget_3)
        self.verticalLayout_13.addWidget(self.widget_16)
        self.stackedWidget.addWidget(self.pageAbout)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesView)
        font = QtGui.QFont()
        font.setKerning(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreferencesView)
        self.navigationList.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.buttonBox.rejected.connect(PreferencesView.reject)
        self.buttonBox.accepted.connect(PreferencesView.accept)
        self.autoSaveEnabledCheckBox_4.toggled['bool'].connect(self.widget_8.setEnabled)
        self.navigationList.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(PreferencesView)

    def retranslateUi(self, PreferencesView):
        _translate = QtCore.QCoreApplication.translate
        PreferencesView.setWindowTitle(_translate("PreferencesView", "Dialog"))
        __sortingEnabled = self.navigationList.isSortingEnabled()
        self.navigationList.setSortingEnabled(False)
        item = self.navigationList.item(0)
        item.setText(_translate("PreferencesView", "General"))
        item = self.navigationList.item(1)
        item.setText(_translate("PreferencesView", "Appearance"))
        item = self.navigationList.item(2)
        item.setText(_translate("PreferencesView", "MPV Settings"))
        item = self.navigationList.item(3)
        item.setText(_translate("PreferencesView", "QC Document"))
        item = self.navigationList.item(4)
        item.setText(_translate("PreferencesView", "Language"))
        item = self.navigationList.item(5)
        item.setText(_translate("PreferencesView", "About"))
        self.navigationList.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("PreferencesView", "General"))
        self.authorLabel.setText(_translate("PreferencesView", "Nick name"))
        self.authorLineEdit.setPlaceholderText(_translate("PreferencesView", "Type here to change the nick name"))
        self.label_3.setText(_translate("PreferencesView", "Comment types"))
        self.kTypesLineEdit.setPlaceholderText(_translate("PreferencesView", "Type here to add new comment types"))
        self.kTypesAddButton.setText(_translate("PreferencesView", "Add"))
        self.kTypesRemoveButton.setText(_translate("PreferencesView", "Remove"))
        self.kTypesMoveUpButton.setText(_translate("PreferencesView", "Move Up"))
        self.kTypesMoveDownButton.setText(_translate("PreferencesView", "Move Down"))
        self.label_9.setText(_translate("PreferencesView", "Appearance"))
        self.label_10.setText(_translate("PreferencesView", "Window Title"))
        self.window_title_combo_box.setItemText(0, _translate("PreferencesView", "Display default title"))
        self.window_title_combo_box.setItemText(1, _translate("PreferencesView", "Display video title"))
        self.window_title_combo_box.setItemText(2, _translate("PreferencesView", "Display video path"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabGeneral), _translate("PreferencesView", "General"))
        self.label_5.setText(_translate("PreferencesView", "MPV Settings"))
        self.label_8.setText(_translate("PreferencesView", "Changes will be applied after restart."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("PreferencesView", "mpv.conf"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PreferencesView", "input.conf"))
        self.label_4.setText(_translate("PreferencesView", "QC Document"))
        self.autoSaveEnabledCheckBox_4.setText(_translate("PreferencesView", "Auto save enabled"))
        self.label_6.setText(_translate("PreferencesView", "each"))
        self.autosaveTimeUnit_4.setText(_translate("PreferencesView", "seconds"))
        self.saveNickNameCheckBox.setText(_translate("PreferencesView", "Save nick name to QC document"))
        self.saveVideoPathCheckBox.setText(_translate("PreferencesView", "Save video path to QC document"))
        self.label.setText(_translate("PreferencesView", "Language"))
        self.label_7.setText(_translate("PreferencesView", "Language"))
        self.comboBox.setItemText(0, _translate("PreferencesView", "English"))
        self.comboBox.setItemText(1, _translate("PreferencesView", "German"))
        self.label_11.setText(_translate("PreferencesView", "About"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.sdasd), _translate("PreferencesView", "About"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("PreferencesView", "Credits"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("PreferencesView", "Licence"))
