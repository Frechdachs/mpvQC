# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPlayerView(object):
    def setupUi(self, MainPlayerView):
        MainPlayerView.setObjectName("MainPlayerView")
        MainPlayerView.resize(800, 600)
        self.mainWindowContentWidget = QtWidgets.QWidget(MainPlayerView)
        self.mainWindowContentWidget.setObjectName("mainWindowContentWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindowContentWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainWindowContentSplitter = QtWidgets.QSplitter(self.mainWindowContentWidget)
        self.mainWindowContentSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mainWindowContentSplitter.setObjectName("mainWindowContentSplitter")
        self.verticalLayout.addWidget(self.mainWindowContentSplitter)
        MainPlayerView.setCentralWidget(self.mainWindowContentWidget)
        self.mainWindowMenuBar = QtWidgets.QMenuBar(MainPlayerView)
        self.mainWindowMenuBar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.mainWindowMenuBar.setObjectName("mainWindowMenuBar")
        self.mainWindowFileMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowFileMenu.setObjectName("mainWindowFileMenu")
        self.mainWindowVideoMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowVideoMenu.setObjectName("mainWindowVideoMenu")
        self.mainWindowSettingsMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowSettingsMenu.setObjectName("mainWindowSettingsMenu")
        self.menuWindowTitle = QtWidgets.QMenu(self.mainWindowSettingsMenu)
        self.menuWindowTitle.setObjectName("menuWindowTitle")
        self.menuDocumentSettings = QtWidgets.QMenu(self.mainWindowSettingsMenu)
        self.menuDocumentSettings.setObjectName("menuDocumentSettings")
        self.menuLanguage = QtWidgets.QMenu(self.mainWindowSettingsMenu)
        self.menuLanguage.setObjectName("menuLanguage")
        self.mainWindowAboutMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowAboutMenu.setObjectName("mainWindowAboutMenu")
        MainPlayerView.setMenuBar(self.mainWindowMenuBar)
        self.actionNewQcDocument = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNewQcDocument.setIcon(icon)
        self.actionNewQcDocument.setObjectName("actionNewQcDocument")
        self.actionOpenQcDocuments = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("document-open-recent")
        self.actionOpenQcDocuments.setIcon(icon)
        self.actionOpenQcDocuments.setObjectName("actionOpenQcDocuments")
        self.actionSaveQcDocument = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSaveQcDocument.setIcon(icon)
        self.actionSaveQcDocument.setObjectName("actionSaveQcDocument")
        self.actionSaveQcDocumentAs = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionSaveQcDocumentAs.setIcon(icon)
        self.actionSaveQcDocumentAs.setObjectName("actionSaveQcDocumentAs")
        self.actionExitMpvQc = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionExitMpvQc.setIcon(icon)
        self.actionExitMpvQc.setObjectName("actionExitMpvQc")
        self.actionOpenVideoFile = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("mpv")
        self.actionOpenVideoFile.setIcon(icon)
        self.actionOpenVideoFile.setObjectName("actionOpenVideoFile")
        self.actionOpenNetworkStream = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("network-server")
        self.actionOpenNetworkStream.setIcon(icon)
        self.actionOpenNetworkStream.setObjectName("actionOpenNetworkStream")
        self.actionResizeVideoToOriginalResolution = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("image-resize")
        self.actionResizeVideoToOriginalResolution.setIcon(icon)
        self.actionResizeVideoToOriginalResolution.setObjectName("actionResizeVideoToOriginalResolution")
        self.actionCheckForUpdates = QtWidgets.QAction(MainPlayerView)
        self.actionCheckForUpdates.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("arrow-down")
        self.actionCheckForUpdates.setIcon(icon)
        self.actionCheckForUpdates.setObjectName("actionCheckForUpdates")
        self.actionAboutQt = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAboutQt.setIcon(icon)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionAboutMpvQc = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAboutMpvQc.setIcon(icon)
        self.actionAboutMpvQc.setObjectName("actionAboutMpvQc")
        self.actionSettings = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("preferences-other")
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionOpenSubtitleFile = QtWidgets.QAction(MainPlayerView)
        self.actionOpenSubtitleFile.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("media-view-subtitles-symbolic")
        self.actionOpenSubtitleFile.setIcon(icon)
        self.actionOpenSubtitleFile.setObjectName("actionOpenSubtitleFile")
        self.actionEditCommentTypes = QtWidgets.QAction(MainPlayerView)
        self.actionEditCommentTypes.setObjectName("actionEditCommentTypes")
        self.actionEditNickname = QtWidgets.QAction(MainPlayerView)
        self.actionEditNickname.setObjectName("actionEditNickname")
        self.actionWindowTitleDefault = QtWidgets.QAction(MainPlayerView)
        self.actionWindowTitleDefault.setCheckable(True)
        self.actionWindowTitleDefault.setChecked(False)
        self.actionWindowTitleDefault.setObjectName("actionWindowTitleDefault")
        self.actionWindowTitleFile = QtWidgets.QAction(MainPlayerView)
        self.actionWindowTitleFile.setCheckable(True)
        self.actionWindowTitleFile.setChecked(False)
        self.actionWindowTitleFile.setObjectName("actionWindowTitleFile")
        self.actionWindowTitlePath = QtWidgets.QAction(MainPlayerView)
        self.actionWindowTitlePath.setCheckable(True)
        self.actionWindowTitlePath.setChecked(False)
        self.actionWindowTitlePath.setObjectName("actionWindowTitlePath")
        self.actionDarkTheme = QtWidgets.QAction(MainPlayerView)
        self.actionDarkTheme.setCheckable(True)
        self.actionDarkTheme.setObjectName("actionDarkTheme")
        self.actionEditMpvConf = QtWidgets.QAction(MainPlayerView)
        self.actionEditMpvConf.setObjectName("actionEditMpvConf")
        self.actionEditInputConf = QtWidgets.QAction(MainPlayerView)
        self.actionEditInputConf.setObjectName("actionEditInputConf")
        self.actionDocumentBackups = QtWidgets.QAction(MainPlayerView)
        self.actionDocumentBackups.setCheckable(True)
        self.actionDocumentBackups.setObjectName("actionDocumentBackups")
        self.actionDocumentBackupInterval = QtWidgets.QAction(MainPlayerView)
        self.actionDocumentBackupInterval.setObjectName("actionDocumentBackupInterval")
        self.actionSaveNickNameToDocument = QtWidgets.QAction(MainPlayerView)
        self.actionSaveNickNameToDocument.setCheckable(True)
        self.actionSaveNickNameToDocument.setChecked(False)
        self.actionSaveNickNameToDocument.setObjectName("actionSaveNickNameToDocument")
        self.actionSaveVideoPathToDocument = QtWidgets.QAction(MainPlayerView)
        self.actionSaveVideoPathToDocument.setCheckable(True)
        self.actionSaveVideoPathToDocument.setObjectName("actionSaveVideoPathToDocument")
        self.action_3 = QtWidgets.QAction(MainPlayerView)
        self.action_3.setObjectName("action_3")
        self.mainWindowFileMenu.addAction(self.actionNewQcDocument)
        self.mainWindowFileMenu.addAction(self.actionOpenQcDocuments)
        self.mainWindowFileMenu.addAction(self.actionSaveQcDocument)
        self.mainWindowFileMenu.addAction(self.actionSaveQcDocumentAs)
        self.mainWindowFileMenu.addSeparator()
        self.mainWindowFileMenu.addAction(self.actionExitMpvQc)
        self.mainWindowVideoMenu.addAction(self.actionOpenVideoFile)
        self.mainWindowVideoMenu.addAction(self.actionOpenSubtitleFile)
        self.mainWindowVideoMenu.addAction(self.actionOpenNetworkStream)
        self.mainWindowVideoMenu.addSeparator()
        self.mainWindowVideoMenu.addAction(self.actionResizeVideoToOriginalResolution)
        self.menuWindowTitle.addAction(self.actionWindowTitleDefault)
        self.menuWindowTitle.addAction(self.actionWindowTitleFile)
        self.menuWindowTitle.addAction(self.actionWindowTitlePath)
        self.menuDocumentSettings.addAction(self.actionSaveVideoPathToDocument)
        self.menuDocumentSettings.addAction(self.actionSaveNickNameToDocument)
        self.menuLanguage.addAction(self.action_3)
        self.mainWindowSettingsMenu.addAction(self.actionEditNickname)
        self.mainWindowSettingsMenu.addAction(self.actionEditCommentTypes)
        self.mainWindowSettingsMenu.addSeparator()
        self.mainWindowSettingsMenu.addAction(self.menuWindowTitle.menuAction())
        self.mainWindowSettingsMenu.addAction(self.actionDarkTheme)
        self.mainWindowSettingsMenu.addSeparator()
        self.mainWindowSettingsMenu.addAction(self.menuLanguage.menuAction())
        self.mainWindowSettingsMenu.addSeparator()
        self.mainWindowSettingsMenu.addAction(self.actionEditMpvConf)
        self.mainWindowSettingsMenu.addAction(self.actionEditInputConf)
        self.mainWindowSettingsMenu.addSeparator()
        self.mainWindowSettingsMenu.addAction(self.menuDocumentSettings.menuAction())
        self.mainWindowSettingsMenu.addAction(self.actionDocumentBackups)
        self.mainWindowSettingsMenu.addAction(self.actionDocumentBackupInterval)
        self.mainWindowAboutMenu.addAction(self.actionAboutQt)
        self.mainWindowAboutMenu.addAction(self.actionAboutMpvQc)
        self.mainWindowMenuBar.addAction(self.mainWindowFileMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowVideoMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowSettingsMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowAboutMenu.menuAction())

        self.retranslateUi(MainPlayerView)
        QtCore.QMetaObject.connectSlotsByName(MainPlayerView)

    def retranslateUi(self, MainPlayerView):
        _translate = QtCore.QCoreApplication.translate
        MainPlayerView.setWindowTitle(_translate("MainPlayerView", "mpvQC"))
        self.mainWindowFileMenu.setTitle(_translate("MainPlayerView", "&File"))
        self.mainWindowVideoMenu.setTitle(_translate("MainPlayerView", "Vi&deo"))
        self.mainWindowSettingsMenu.setTitle(_translate("MainPlayerView", "Optio&ns"))
        self.menuWindowTitle.setTitle(_translate("MainPlayerView", "Window title"))
        self.menuDocumentSettings.setTitle(_translate("MainPlayerView", "Document settings"))
        self.menuLanguage.setTitle(_translate("MainPlayerView", "Language"))
        self.mainWindowAboutMenu.setTitle(_translate("MainPlayerView", "Abo&ut"))
        self.actionNewQcDocument.setText(_translate("MainPlayerView", "&New QC document"))
        self.actionNewQcDocument.setShortcut(_translate("MainPlayerView", "Ctrl+N"))
        self.actionOpenQcDocuments.setText(_translate("MainPlayerView", "&Open QC document(s) ..."))
        self.actionOpenQcDocuments.setShortcut(_translate("MainPlayerView", "Ctrl+O"))
        self.actionSaveQcDocument.setText(_translate("MainPlayerView", "&Save QC document"))
        self.actionSaveQcDocument.setShortcut(_translate("MainPlayerView", "Ctrl+S"))
        self.actionSaveQcDocumentAs.setText(_translate("MainPlayerView", "S&ave QC document as ..."))
        self.actionSaveQcDocumentAs.setShortcut(_translate("MainPlayerView", "Ctrl+Shift+S"))
        self.actionExitMpvQc.setText(_translate("MainPlayerView", "&Exit mpvQC"))
        self.actionExitMpvQc.setShortcut(_translate("MainPlayerView", "Ctrl+Q"))
        self.actionOpenVideoFile.setText(_translate("MainPlayerView", "Open &video ..."))
        self.actionOpenVideoFile.setShortcut(_translate("MainPlayerView", "Ctrl+Shift+O"))
        self.actionOpenNetworkStream.setText(_translate("MainPlayerView", "Open &network stream ..."))
        self.actionOpenNetworkStream.setShortcut(_translate("MainPlayerView", "Ctrl+Alt+Shift+O"))
        self.actionResizeVideoToOriginalResolution.setText(_translate("MainPlayerView", "&Resize video to original resolution"))
        self.actionResizeVideoToOriginalResolution.setShortcut(_translate("MainPlayerView", "Ctrl+R"))
        self.actionCheckForUpdates.setText(_translate("MainPlayerView", "&Check For Updates ..."))
        self.actionAboutQt.setText(_translate("MainPlayerView", "About &Qt"))
        self.actionAboutMpvQc.setText(_translate("MainPlayerView", "About &mpvQC"))
        self.actionSettings.setText(_translate("MainPlayerView", "&Settings"))
        self.actionSettings.setShortcut(_translate("MainPlayerView", "Ctrl+Alt+S"))
        self.actionOpenSubtitleFile.setText(_translate("MainPlayerView", "&Open subtitle ..."))
        self.actionEditCommentTypes.setText(_translate("MainPlayerView", "Edit comment types ..."))
        self.actionEditNickname.setText(_translate("MainPlayerView", "Edit nickname ..."))
        self.actionWindowTitleDefault.setText(_translate("MainPlayerView", "Default title"))
        self.actionWindowTitleFile.setText(_translate("MainPlayerView", "Video file"))
        self.actionWindowTitlePath.setText(_translate("MainPlayerView", "Video path"))
        self.actionDarkTheme.setText(_translate("MainPlayerView", "Dark theme"))
        self.actionEditMpvConf.setText(_translate("MainPlayerView", "Edit mpv.conf ..."))
        self.actionEditInputConf.setText(_translate("MainPlayerView", "Edit input.conf ..."))
        self.actionDocumentBackups.setText(_translate("MainPlayerView", "Document backups"))
        self.actionDocumentBackupInterval.setText(_translate("MainPlayerView", "Document backup interval ..."))
        self.actionSaveNickNameToDocument.setText(_translate("MainPlayerView", "Save nick name"))
        self.actionSaveVideoPathToDocument.setText(_translate("MainPlayerView", "Save video path"))
        self.action_3.setText(_translate("MainPlayerView", "__"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPlayerView = QtWidgets.QMainWindow()
    ui = Ui_MainPlayerView()
    ui.setupUi(MainPlayerView)
    MainPlayerView.show()
    sys.exit(app.exec_())
