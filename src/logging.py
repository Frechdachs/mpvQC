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

# todo implement proper logging

def mpv_log_handler(log_lvl, component, message) -> None:
    """
    Defines the log handler for the mpv player.

    :param log_lvl: The log level
    :param component: The component
    :param message: The message to log
    :return:
    """

    print("[{}] {}: {}".format(log_lvl, component, message))
