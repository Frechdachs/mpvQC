# Copyright (C) 2016-2017 Frechdachs <frechdachs@rekt.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import platform

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox, QDialog

from src import settings, constants
from src.gui import TYPEWRITER_FONT
from src.gui.generated.preferences import Ui_PreferencesView
from src.gui.messageboxes import ConfigurationResetMB, ConfigurationHasChangedMB
from start import APPLICATION_VERSION, APPLICATION_NAME

_translate = QtCore.QCoreApplication.translate


class PreferenceHandler(QDialog):
    """
    The dialog for the preferences.
    """

    # Will be set by MpvWidget on start up
    VERSION_MPV = ""
    VERSION_FFMPEG = ""

    class PreferenceBinder:

        def __init__(self, user_interface: Ui_PreferencesView, pref_dialog: 'PreferenceHandler'):
            self.__connected_elements = []
            self.__outer = pref_dialog
            self.__ui = user_interface
            self.__setup_button_box()
            self.__setup_language()
            self.__setup_nickname()
            self.__setup_comments()
            self.__setup_autosave_checkbox()
            self.__setup_autosave_interval()
            self.__setup_qc_write_video_path_to_file()
            self.__setup_qc_write_nick_to_file()
            self.__setup_appearance_window_title()
            self.__setup_conf_input()
            self.__setup_conf_mpv()
            self.__setup_about()

            # Timer for updating the apply button
            self.btn_apply_update_timer = QTimer(self.__outer.parent())
            self.__observe_changes()

        def __observe_changes(self):
            btn_apply = self.__ui.buttonBox.button(QDialogButtonBox.Apply)

            def on_update():
                btn_apply.setEnabled(self.changed())

            self.btn_apply_update_timer.timeout.connect(on_update)
            self.btn_apply_update_timer.start(100)

        def __setup_button_box(self):
            button_box = self.__ui.buttonBox

            btn_apply = button_box.button(QDialogButtonBox.Apply)
            btn_apply.clicked.connect(self.__outer.accept)
            btn_apply.setText(_translate("PreferencesView", "Apply"))
            btn_apply.setEnabled(False)

            btn_close = button_box.button(QDialogButtonBox.Close)
            btn_close.setIcon(QIcon())
            btn_close.setText(_translate("PreferencesView", "Close"))

            btn_restore_defaults = button_box.button(QDialogButtonBox.RestoreDefaults)
            btn_restore_defaults.clicked.connect(self.__outer.on_restore_default)
            btn_restore_defaults.setText(_translate("PreferencesView", "Defaults"))
            self.__connected_elements.extend([btn_apply, btn_restore_defaults])

        def __setup_language(self):
            language_box = self.__ui.comboBox
            language_box.setCurrentIndex(
                max(language_box.findText(
                    _translate("PreferencesView", settings.Setting_Custom_Language_LANGUAGE.value)), 0))

            def f(new_language):
                languages = {
                    _translate("PreferencesView", "English"): "English",
                    _translate("PreferencesView", "German"): "German"
                }
                settings.Setting_Custom_Language_LANGUAGE.temporary_value = languages[new_language]

            language_box.currentTextChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(language_box)

        def __setup_nickname(self):
            nick = self.__ui.authorLineEdit
            nick.setText(settings.Setting_Custom_General_NICKNAME.value)

            def f(new_nickname):
                settings.Setting_Custom_General_NICKNAME.temporary_value = new_nickname

            nick.textChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(nick)

        def __setup_comments(self):
            from src.gui.widgets import PreferenceCommentTypesWidget

            self.ctypes_widget = PreferenceCommentTypesWidget(self.__ui.kTypesLineEdit,
                                                              self.__ui.kTypesListWidget,
                                                              self.__ui.kTypesAddButton,
                                                              self.__ui.kTypesRemoveButton,
                                                              self.__ui.kTypesMoveUpButton,
                                                              self.__ui.kTypesMoveDownButton)

            for ct in settings.Setting_Custom_General_COMMENT_TYPES.value:
                self.__ui.kTypesListWidget.addItem(ct)

            def f():
                settings.Setting_Custom_General_COMMENT_TYPES.temporary_value = self.ctypes_widget.items()

            self.ctypes_widget.changed.connect(lambda fun=f: fun())
            self.__connected_elements.append(self.ctypes_widget)

        def __setup_autosave_checkbox(self):
            chk_box = self.__ui.autoSaveEnabledCheckBox_4
            chk_box.setChecked(settings.Setting_Custom_QcDocument_AUTOSAVE_ENABLED.value)

            def f(new_state):
                settings.Setting_Custom_QcDocument_AUTOSAVE_ENABLED.temporary_value = bool(new_state)

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(chk_box)

        def __setup_autosave_interval(self):
            spin_box = self.__ui.autosaveSpinBox_4
            spin_box.setValue(settings.Setting_Custom_QcDocument_AUTOSAVE_INTERVAL.value)

            def f(new_value):
                settings.Setting_Custom_QcDocument_AUTOSAVE_INTERVAL.temporary_value = new_value

            spin_box.valueChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(spin_box)

        def __setup_qc_write_video_path_to_file(self):
            chk_box = self.__ui.saveVideoPathCheckBox
            chk_box.setChecked(settings.Setting_Custom_QcDocument_WRITE_VIDEO_PATH_TO_FILE.value)

            def f(n_state):
                settings.Setting_Custom_QcDocument_WRITE_VIDEO_PATH_TO_FILE.temporary_value = bool(n_state)

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(chk_box)

        def __setup_qc_write_nick_to_file(self):
            chk_box = self.__ui.saveNickNameCheckBox
            chk_box.setChecked(settings.Setting_Custom_QcDocument_WRITE_NICK_TO_FILE.value)

            def f(new_state):
                settings.Setting_Custom_QcDocument_WRITE_NICK_TO_FILE.temporary_value = bool(new_state)

            chk_box.stateChanged.connect(lambda value, fun=f: fun(value))
            self.__connected_elements.append(chk_box)

        def __setup_appearance_window_title(self):
            win_box = self.__ui.window_title_combo_box
            win_box.setCurrentIndex(settings.Setting_Custom_Appearance_General_WINDOW_TITLE.value)

            def fun(new_index):
                settings.Setting_Custom_Appearance_General_WINDOW_TITLE.temporary_value = new_index

            win_box.currentIndexChanged.connect(lambda value, f=fun: f(value))
            self.__connected_elements.append(win_box)

        def __setup_conf_input(self):
            text_input = self.__ui.input_conf_plain_text_edit
            text_input.setPlainText(settings.Setting_Custom_Configuration_INPUT.value)
            text_input.setFont(TYPEWRITER_FONT)

            def f():
                settings.Setting_Custom_Configuration_INPUT.temporary_value = text_input.toPlainText()

            text_input.textChanged.connect(lambda fun=f: fun())
            self.__connected_elements.append(text_input)

        def __setup_conf_mpv(self):
            text_input = self.__ui.mpv_conf_plain_text_edit
            text_input.setPlainText(settings.Setting_Custom_Configuration_MPV.value)
            text_input.setFont(TYPEWRITER_FONT)

            def f():
                settings.Setting_Custom_Configuration_MPV.temporary_value = text_input.toPlainText()

            text_input.textChanged.connect(lambda fun=f: fun())
            self.__connected_elements.append(text_input)

        def __setup_about(self):
            self.__ui.creditsBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
            self.__ui.creditsBrowser.setHtml(constants.CREDITS)
            self.__ui.licenceBrowser.setTextInteractionFlags(Qt.TextBrowserInteraction)
            self.__ui.licenceBrowser.setHtml(constants.LICENCE)

            self.__ui.aboutBrowser.setOpenExternalLinks(True)
            self.__ui.aboutBrowser.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
            self.__ui.aboutBrowser.setHtml(constants.ABOUT.format(
                APPLICATION_VERSION,
                platform.architecture()[0],
                APPLICATION_NAME,
                PreferenceHandler.VERSION_MPV,
                PreferenceHandler.VERSION_FFMPEG,
                "2016-2017")
            )

        def display_about_page(self) -> None:
            """
            Will display the about page.
            """

            self.__ui.navigationList.setCurrentRow(self.__ui.navigationList.model().rowCount() - 1)

        def save(self):
            for setting in settings.SettingJsonSettingConfs:
                setting.save()

        def reset(self):
            for setting in settings.SettingJsonSettingConfs:
                setting.reset()

            for c in self.__connected_elements:
                try:
                    c.disconnect()
                except TypeError:
                    pass  # throws a typeError if no connection available, but we don't care

        def changed(self) -> bool:
            for setting in settings.SettingJsonSettingConfs:
                if setting.changed():
                    return True
            return False

        def clean_up(self):
            self.btn_apply_update_timer.stop()
            for setting in settings.SettingJsonSettingConfs:
                setting.temporary_value = None

    def __init__(self, display_about):
        super().__init__()

        ui: Ui_PreferencesView = Ui_PreferencesView()
        ui.setupUi(self)

        self.preference_binder = PreferenceHandler.PreferenceBinder(ui, self)

        if display_about:
            self.preference_binder.display_about_page()

    def mousePressEvent(self, mouse_ev: QtGui.QMouseEvent):
        """
        On mouse pressed event (pressed anywhere except the comment type widget)
        the focus needs to be removed from the comment type widget.
        """

        self.preference_binder.ctypes_widget.remove_focus()

        super().mousePressEvent(mouse_ev)

    def reject(self):
        """
        Action when discard button is pressed.
        """

        if self.preference_binder.changed():
            if ConfigurationHasChangedMB().exec_():
                return

        self.preference_binder.clean_up()
        super().reject()

    def accept(self):
        """
        Action when apply button is pressed.
        """

        self.preference_binder.save()
        settings.save()

    def on_restore_default(self):
        """
        Action when restore default button is pressed.
        """

        if not ConfigurationResetMB().exec_():
            self.preference_binder.reset()
            self.preference_binder.clean_up()
            settings.save()
            super().reject()
