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


def run(dir_program: str, app_version: str, app_name: str):
    from mpvqc._metadata import set_metadata
    from mpvqc._files import set_files
    from mpvqc._settings import set_settings
    from mpvqc._resources import set_resources, get_resources

    set_metadata(dir_program, app_version, app_name)
    set_files()
    set_resources()
    set_settings()

    import sys

    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QIcon

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(get_resources().get_path_app_icon()))

    from mpvqc.uihandler import MainHandler

    container = MainHandler(app)
    container.show()

    sys.exit(app.exec_())


def main():
    import locale
    import os
    import platform
    import sys
    # noinspection PyUnresolvedReferences
    import mpvqc._resources_rc

    dir_program = sys._MEIPASS if getattr(sys, "frozen", False) else os.path.dirname(os.path.realpath(__file__))
    dir_program = os.path.dirname(dir_program)
    app_version = "0.7.0"
    app_name = "mpvQC"

    if platform.system() == "Windows":
        os.add_dll_directory(dir_program)

    locale.setlocale(locale.LC_NUMERIC, "C")

    run(
        dir_program=dir_program,
        app_version=app_version,
        app_name=app_name
    )


if __name__ == '__main__':
    main()
