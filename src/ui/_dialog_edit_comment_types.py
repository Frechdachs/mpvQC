# -*- coding: utf-8 -*-

# Form implementation ui from reading ui file 'uiutil/dialog_edit_comment_types.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentTypesDialog(object):
    def setupUi(self, CommentTypesDialog):
        CommentTypesDialog.setObjectName("CommentTypesDialog")
        CommentTypesDialog.resize(400, 400)
        CommentTypesDialog.setMinimumSize(QtCore.QSize(400, 400))
        self.gridLayout = QtWidgets.QGridLayout(CommentTypesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(CommentTypesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.subtitle = QtWidgets.QLabel(CommentTypesDialog)
        self.subtitle.setObjectName("subtitle")
        self.verticalLayout.addWidget(self.subtitle)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(CommentTypesDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.widget = QtWidgets.QWidget(CommentTypesDialog)
        self.widget.setStyleSheet("QPushButton { text-align:left; padding: 8px; }")
        self.widget.setObjectName("widget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_15.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_15.addWidget(self.listWidget)
        self.buttonContainer = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonContainer.sizePolicy().hasHeightForWidth())
        self.buttonContainer.setSizePolicy(sizePolicy)
        self.buttonContainer.setObjectName("buttonContainer")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.buttonContainer)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.buttonContainerInside = QtWidgets.QWidget(self.buttonContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonContainerInside.sizePolicy().hasHeightForWidth())
        self.buttonContainerInside.setSizePolicy(sizePolicy)
        self.buttonContainerInside.setObjectName("buttonContainerInside")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.buttonContainerInside)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.buttonAdd = QtWidgets.QPushButton(self.buttonContainerInside)
        self.buttonAdd.setEnabled(False)
        self.buttonAdd.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.buttonAdd.setIcon(icon)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_22.addWidget(self.buttonAdd)
        self.buttonRemove = QtWidgets.QPushButton(self.buttonContainerInside)
        self.buttonRemove.setEnabled(False)
        self.buttonRemove.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.buttonRemove.setIcon(icon)
        self.buttonRemove.setObjectName("buttonRemove")
        self.verticalLayout_22.addWidget(self.buttonRemove)
        self.buttonUp = QtWidgets.QPushButton(self.buttonContainerInside)
        self.buttonUp.setEnabled(False)
        self.buttonUp.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.buttonUp.setIcon(icon)
        self.buttonUp.setObjectName("buttonUp")
        self.verticalLayout_22.addWidget(self.buttonUp)
        self.buttonDown = QtWidgets.QPushButton(self.buttonContainerInside)
        self.buttonDown.setEnabled(False)
        self.buttonDown.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon.fromTheme("go-down")
        self.buttonDown.setIcon(icon)
        self.buttonDown.setObjectName("buttonDown")
        self.verticalLayout_22.addWidget(self.buttonDown)
        self.verticalLayout_21.addWidget(self.buttonContainerInside)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem)
        self.horizontalLayout_15.addWidget(self.buttonContainer)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CommentTypesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(CommentTypesDialog)
        self.buttonBox.accepted.connect(CommentTypesDialog.accept)
        self.buttonBox.rejected.connect(CommentTypesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CommentTypesDialog)

    def retranslateUi(self, CommentTypesDialog):
        _translate = QtCore.QCoreApplication.translate
        CommentTypesDialog.setWindowTitle(_translate("CommentTypesDialog", "Edit comment types"))
        CommentTypesDialog.setAccessibleName(_translate("CommentTypesDialog", "Comment types"))
        self.title.setText(_translate("CommentTypesDialog", "Manage comment types "))
        self.subtitle.setText(_translate("CommentTypesDialog", "Add new comment types or rearange them"))
        self.lineEdit.setPlaceholderText(_translate("CommentTypesDialog", "Type here to add new comment types"))
        self.buttonAdd.setText(_translate("CommentTypesDialog", "Add"))
        self.buttonRemove.setText(_translate("CommentTypesDialog", "Remove"))
        self.buttonUp.setText(_translate("CommentTypesDialog", "Move Up"))
        self.buttonDown.setText(_translate("CommentTypesDialog", "Move Down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CommentTypesDialog = QtWidgets.QDialog()
    ui = Ui_CommentTypesDialog()
    ui.setupUi(CommentTypesDialog)
    CommentTypesDialog.show()
    sys.exit(app.exec_())