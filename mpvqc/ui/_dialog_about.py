# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/ui/dialog_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(750, 750)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setText("mpvQC")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.subtitle = QtWidgets.QLabel(AboutDialog)
        self.subtitle.setText("")
        self.subtitle.setObjectName("subtitle")
        self.verticalLayout.addWidget(self.subtitle)
        self.tabWidget = QtWidgets.QTabWidget(AboutDialog)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.aboutTextBrowser = QtWidgets.QTextBrowser(self.widget1)
        self.aboutTextBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.aboutTextBrowser.setObjectName("aboutTextBrowser")
        self.horizontalLayout_9.addWidget(self.aboutTextBrowser)
        self.tabWidget.addTab(self.widget1, "")
        self.widget2 = QtWidgets.QWidget()
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.creditsTextBrowser = QtWidgets.QTextBrowser(self.widget2)
        self.creditsTextBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Fira Sans\';\"><br /></p></body></html>")
        self.creditsTextBrowser.setObjectName("creditsTextBrowser")
        self.horizontalLayout_10.addWidget(self.creditsTextBrowser)
        self.tabWidget.addTab(self.widget2, "")
        self.widget3 = QtWidgets.QWidget()
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.licenceTextBrowser = QtWidgets.QTextBrowser(self.widget3)
        self.licenceTextBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.licenceTextBrowser.setObjectName("licenceTextBrowser")
        self.horizontalLayout_11.addWidget(self.licenceTextBrowser)
        self.tabWidget.addTab(self.widget3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About mpvQC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget1), _translate("AboutDialog", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget2), _translate("AboutDialog", "Credits"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget3), _translate("AboutDialog", "Licence"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutDialog = QtWidgets.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())
