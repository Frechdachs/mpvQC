import io
import json
import locale
import os
from os import path
from typing import Dict

from PyQt5.QtCore import QCoreApplication
from appdirs import unicode

from src import constants
from src.files import Files

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

_translate = QCoreApplication.translate

# The following list exists only for easing the translation process
__for_translation_only = [
    _translate("CommentTypes", "Translation"),
    _translate("CommentTypes", "Punctuation"),
    _translate("CommentTypes", "Spelling"),
    _translate("CommentTypes", "Phrasing"),
    _translate("CommentTypes", "Timing"),
    _translate("CommentTypes", "Typeset"),
    _translate("CommentTypes", "Note"),
    _translate("CommentTypes", "Type here to add new comment types")
]


class Settings:
    """
    Class for managing user settings which are read and written to disc.
    todo replace with QSettings API
    """

    # Full path of the settings.json file (file name included)
    SETTINGS_JSON_FILE = Files.FILE_SETTINGS

    class Holder:
        """
        Each entry defines a property which is saved to a file.

                * *normal* settings are stored in one *settings.json*
                * *CONF* settings are stored per file
        """

        class Entry:
            """
            An entry represents a property which is saved to disc.
            """

            def __init__(self, identifier: str or path, default_value):
                """
                :param identifier:
                    * *normal* setting: the json key to read and write
                    * *CONF* setting: the full canonical file path to read and write
                :param default_value:
                    the default value
                """

                self.identifier = identifier
                self.default_value = default_value

                self.temporary_value = None
                self._value = None

            @property
            def value(self):
                return self._value

            @value.setter
            def value(self, val):
                self._value = val

            def save(self) -> None:
                """
                Saves the current temporary value, but does **not** write to disc [use Setting.save()] to write to disc.
                """

                if self.temporary_value is not None:
                    self.value = self.temporary_value

                self.temporary_value = None

            def reset(self) -> None:
                """
                Sets the value to the default value and the temporary value to *None*.
                """

                self.value = self.default_value
                self.temporary_value = None

            def changed(self) -> bool:
                """
                :return: whether the value and the temporary value are different.
                """
                return self.temporary_value is not None and self.value != self.temporary_value

        class CommentTypesEntry(Entry):
            def __init__(self, identifier: str or path, default_value):
                super().__init__(identifier, default_value)
                self.current_lang_to_english = {}

            def update(self):
                """
                Will update the internal dictionary to map current language to English.
                :return:
                """
                self.current_lang_to_english.clear()
                for ct in self.default_value:
                    self.current_lang_to_english.update({_translate("CommentTypes", ct): ct})

            @property
            def value(self):
                retu = []
                for ct in self._value if self._value is not None else self.default_value:
                    retu.append(_translate("CommentTypes", ct))
                return retu

            @value.setter
            def value(self, val):
                eng = []
                for ct in val:
                    eng.append(self.current_lang_to_english.get(ct, ct))

                self._value = eng

            def save(self) -> None:
                """
                Saves the current temporary value, but does **not** write to disc [use Setting.save()] to write to disc.
                """

                if self.temporary_value is not None:
                    self.value = self.temporary_value

                self.temporary_value = None

            def reset(self) -> None:
                """
                Sets the value to the default value and the temporary value to *None*.
                """

                self.value = self.default_value
                self.temporary_value = None

            def changed(self) -> bool:
                """
                :return: whether the value and the temporary value are different.
                """
                return self.temporary_value is not None and self.value != self.temporary_value

        VERSION = \
            Entry("version", "0.0.1")

        PLAYER_LAST_PLAYED_DIR = \
            Entry("player_last_played_directory", "")

        NICKNAME = \
            Entry("nickname", "nick")

        LANGUAGE = \
            Entry("language", "German" if locale.getdefaultlocale()[0].startswith("de") else "English")

        AUTOSAVE_ENABLED = \
            Entry("autosave_enabled", True)

        AUTOSAVE_INTERVAL = \
            Entry("autosave_interval_seconds", 90)

        QC_DOC_WRITE_VIDEO_PATH_TO_FILE = \
            Entry("qc_doc_write_video_path_to_file", True)

        QC_DOC_WRITE_NICK_TO_FILE = \
            Entry("qc_doc_write_nick_to_file", True)

        COMMENT_TYPES = \
            CommentTypesEntry("comment_types", ["Spelling", "Punctuation", "Translation", "Phrasing",
                                                "Timing", "Typeset", "Note"])
        CONF_INPUT = \
            Entry(Files.FILE_CONF_INPUT, constants.CFG_INPUT)

        CONF_MPV = \
            Entry(Files.FILE_CONF_MPV, constants.CFG_MPV)

        CUSTOMIZATION_WINDOW_TITLE = \
            Entry("customization_window_title_nothing_name_full", 1)

    json = (
        Holder.VERSION,
        Holder.PLAYER_LAST_PLAYED_DIR,
        Holder.NICKNAME,
        Holder.LANGUAGE,
        Holder.AUTOSAVE_ENABLED,
        Holder.AUTOSAVE_INTERVAL,
        Holder.QC_DOC_WRITE_NICK_TO_FILE,
        Holder.QC_DOC_WRITE_VIDEO_PATH_TO_FILE,
        Holder.COMMENT_TYPES,

        Holder.CUSTOMIZATION_WINDOW_TITLE
    )

    confs = (
        Holder.CONF_INPUT,
        Holder.CONF_MPV
    )

    json_and_conf = json + confs

    @staticmethod
    def __read_json():
        file = Files.FILE_SETTINGS
        if not os.path.isfile(file):
            Settings.__write_json()

        with open(Settings.SETTINGS_JSON_FILE) as df:
            json_values: Dict = json.load(df)

        for json_setting in Settings.json:
            json_setting._value = json_values.get(json_setting.identifier, json_setting.default_value)
            # todo logger

    @staticmethod
    def __write_json():
        dictionary = {}
        for s in Settings.json:
            # noinspection PyProtectedMember
            dictionary.update({
                s.identifier: s._value if s._value is not None else s.default_value
            })

        with io.open(Settings.SETTINGS_JSON_FILE, 'w', encoding='utf8') as file:
            str_ = json.dumps(dictionary, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False)
            file.write(to_unicode(str_))
            #  todo logger

    @staticmethod
    def __read_confs():
        for conf in Settings.confs:
            if not os.path.isfile(conf.identifier):
                Settings.__write_confs(True)
                # That may override the other config, but I think that this will never happen in "production"
            with open(conf.identifier, "r", encoding="utf-8") as file:
                conf._value = file.read()
                # todo logger

    @staticmethod
    def __write_confs(default_value=False):
        for conf in Settings.confs:
            with open(conf.identifier, "w", encoding="utf-8") as file:
                file.write(conf._value if not default_value else conf.default_value)
            #  todo logger

    @staticmethod
    def read() -> None:
        """
        Reads all values from their files.
        Will assign a value to the corresponding entry if a value was found.
        """

        Settings.__read_json()
        Settings.__read_confs()

    @staticmethod
    def save() -> None:
        """
        Saves **and writes** all entries to disc (their current value).
        """

        Settings.__write_json()
        Settings.__write_confs()


Settings.read()
