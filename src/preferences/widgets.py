from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QLineEdit, QAbstractItemView, QListView

from src.gui.dialogs import ConfigurationResetQMessageBox, ConfigurationHasChangedQMessageBox
from src.gui.preferences import Ui_Dialog
from src.preferences import settings

_translate = QtCore.QCoreApplication.translate


class PreferenceDialog(QDialog):
    """
    The dialog for the preferences.
    """

    class PreferenceBinder:

        def __init__(self, user_interface: Ui_Dialog, pref_dialog: 'PreferenceDialog'):
            self.connected_elements = []
            self.SETTINGS = settings.Settings
            self.outer = pref_dialog
            self.ui = user_interface
            self.__setup_button_box()
            self.__setup_language()
            self.__setup_nickname()
            self.__setup_comments()
            self.__setup_autosave_checkbox()
            self.__setup_autosave_interval()
            self.__setup_qc_write_video_path_to_file()
            self.__setup_qc_write_nick_to_file()
            self.__setup_conf_input()
            self.__setup_conf_mpv()

        def __setup_button_box(self):
            button_box = self.ui.buttonBox

            btn_apply = button_box.button(QDialogButtonBox.Apply)
            btn_apply.clicked.connect(self.outer.accept)
            btn_apply.setText(_translate("PreferenceDialog", "Apply"))

            btn_close = button_box.button(QDialogButtonBox.Close)
            btn_close.setIcon(QIcon())
            btn_close.setText(_translate("PreferenceDialog", "Close"))

            btn_restore_defaults = button_box.button(QDialogButtonBox.RestoreDefaults)
            btn_restore_defaults.clicked.connect(self.outer.on_restore_default)
            btn_restore_defaults.setText(_translate("PreferenceDialog", "Defaults"))
            self.connected_elements.extend([btn_apply, btn_restore_defaults])

        def __setup_language(self):
            languages = {
                _translate("PreferenceDialog", "English"): "English",
                _translate("PreferenceDialog", "German"): "German"
            }
            language_box = self.ui.comboBox
            language_box.setCurrentIndex(
                max(language_box.findText(_translate("Dialog", self.SETTINGS.Holder.LANGUAGE.value)), 0))

            def f(new_language):
                self.SETTINGS.Holder.LANGUAGE.temporary_value = languages[new_language]

            language_box.currentTextChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(language_box)

        def __setup_nickname(self):
            nick = self.ui.authorLineEdit
            nick.setPlaceholderText(_translate("Misc", "Type here to change the nick name"))
            nick.setText(self.SETTINGS.Holder.NICKNAME.value)

            def f(new_nickname):
                self.SETTINGS.Holder.NICKNAME.temporary_value = new_nickname

            nick.textChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(nick)

        def __setup_comments(self):
            cts = self.ui.kCommentTypes
            cts.setStyleSheet(" QPushButton { text-align:left; padding: 8px; } ")

            cts.addButton().setText(_translate("PreferenceDialog", "Add"))
            cts.removeButton().setText(_translate("PreferenceDialog", "Remove"))
            cts.upButton().setText(_translate("PreferenceDialog", "Move Up"))
            cts.downButton().setText(_translate("PreferenceDialog", "Move Down"))

            cts_lv: QListView = cts.listView()
            cts_lv.setEditTriggers(QAbstractItemView.NoEditTriggers)

            cts_lv_le: QLineEdit = cts.lineEdit()
            cts_lv_le.setPlaceholderText(_translate("PreferenceDialog", "Type here to add new comment types"))
            cts.clear()

            cts_eng = {}
            for ct in self.SETTINGS.Holder.COMMENT_TYPES.default_value:
                cts_eng.update({_translate("Misc", ct): ct})

            for ct in self.SETTINGS.Holder.COMMENT_TYPES.value:
                cts.insertItem(_translate("Misc", ct))

            def f():
                self.SETTINGS.Holder.COMMENT_TYPES.temporary_value = [cts_eng.get(x, x).strip() for x in cts.items()]

            cts.changed.connect(lambda fun=f: fun())
            self.connected_elements.append(cts)

        def __setup_autosave_checkbox(self):
            chk_box = self.ui.autoSaveEnabledCheckBox_4
            chk_box.setChecked(self.SETTINGS.Holder.AUTOSAVE_ENABLED.value)

            def f(new_state):
                self.SETTINGS.Holder.AUTOSAVE_ENABLED.temporary_value = new_state

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(chk_box)

        def __setup_autosave_interval(self):
            spin_box = self.ui.autosaveSpinBox_4
            spin_box.setValue(self.SETTINGS.Holder.AUTOSAVE_INTERVAL.value)

            def f(new_value):
                self.SETTINGS.Holder.AUTOSAVE_INTERVAL.temporary_value = new_value

            spin_box.valueChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(spin_box)

        def __setup_qc_write_video_path_to_file(self):
            chk_box = self.ui.saveVideoPathCheckBox
            chk_box.setChecked(self.SETTINGS.Holder.QC_DOC_WRITE_VIDEO_PATH_TO_FILE.value)

            def f(new_state):
                self.SETTINGS.Holder.QC_DOC_WRITE_VIDEO_PATH_TO_FILE.temporary_value = new_state

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(chk_box)

        def __setup_qc_write_nick_to_file(self):
            chk_box = self.ui.saveNickNameCheckBox
            chk_box.setChecked(self.SETTINGS.Holder.QC_DOC_WRITE_NICK_TO_FILE.value)

            def f(new_state):
                self.SETTINGS.Holder.QC_DOC_WRITE_NICK_TO_FILE.temporary_value = new_state

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.connected_elements.append(chk_box)

        def __setup_conf_input(self):
            text_input = self.ui.input_conf_plain_text_edit
            text_input.setPlainText(self.SETTINGS.Holder.CONF_INPUT.value)
            text_input.setFont(QFont(QFontDatabase.systemFont(QFontDatabase.FixedFont)))

            def f():
                self.SETTINGS.Holder.CONF_INPUT.temporary_value = text_input.toPlainText()

            text_input.textChanged.connect(lambda fun=f: fun())
            self.connected_elements.append(text_input)

        def __setup_conf_mpv(self):
            text_input = self.ui.mpv_conf_plain_text_edit
            text_input.setPlainText(self.SETTINGS.Holder.CONF_MPV.value)
            text_input.setFont(QFont(QFontDatabase.systemFont(QFontDatabase.FixedFont)))

            def f():
                self.SETTINGS.Holder.CONF_MPV.temporary_value = text_input.toPlainText()

            text_input.textChanged.connect(lambda fun=f: fun())
            self.connected_elements.append(text_input)

        def save(self):
            for setting in self.SETTINGS.json_and_conf:
                setting.save()

        def reset(self):
            for setting in self.SETTINGS.json_and_conf:
                setting.reset()

            for c in self.connected_elements:
                try:
                    c.disconnect()
                except TypeError:
                    pass  # throws a typeError if no connection available, but we don't care

        def changed(self) -> bool:
            for setting in self.SETTINGS.json_and_conf:
                if setting.changed():
                    return True
            return False

        def clean_up(self):
            for setting in self.SETTINGS.json_and_conf:
                setting.temporary_value = None

    def __init__(self):
        super().__init__()

        self.ui: Ui_Dialog = Ui_Dialog()
        self.ui.setupUi(self)

        self.preference_binder = PreferenceDialog.PreferenceBinder(self.ui, self)

    def mousePressEvent(self, mouse_ev: QtGui.QMouseEvent):
        """
        On mouse pressed event (pressed anywhere except the comment type widget)
        the focus needs to be removed from the comment type widget.
        """

        cts = self.ui.kCommentTypes
        ct_list_view: QListView = cts.listView()

        if ct_list_view.selectionModel().selectedIndexes():
            ct_list_view.clearSelection()
            edit = cts.lineEdit()
            edit.setReadOnly(False)
            edit.setPlaceholderText(_translate("PreferenceDialog", "Type here to add new comment types"))

            for btn in [cts.addButton(), cts.removeButton(), cts.upButton(), cts.downButton()]:
                btn.setEnabled(False)

        super().mousePressEvent(mouse_ev)

    def reject(self):
        """
        Action when discard button is pressed.
        """

        if self.preference_binder.changed():
            if ConfigurationHasChangedQMessageBox().exec_():
                return

        self.preference_binder.clean_up()
        super().reject()

    def accept(self):
        """
        Action when apply button is pressed.
        """

        self.preference_binder.save()
        self.preference_binder.SETTINGS.save()

    def on_restore_default(self):
        """
        Action when restore default button is pressed.
        """

        if not ConfigurationResetQMessageBox().exec_():
            self.preference_binder.reset()
            self.preference_binder.SETTINGS.save()
            super().reject()
