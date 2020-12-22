#  mpvQC
#
#  Copyright (C) 2020 mpvQC developers
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


from typing import Optional

from mpvqc.engine.interface import App
from mpvqc.gui.messageboxes import MessageBoxes, ExistingCommentsDuringImportResponse as MbResponse


class ExistingCommentsMessageBox:

    def __init__(self, app: App):
        self._parent = app.parent()
        self._response: Optional[MbResponse] = None

    def do_we_abort(self) -> bool:
        self._ensure_response()
        return self._response == MbResponse.CANCEL_IMPORT

    def do_we_clear_table(self) -> bool:
        self._ensure_response()
        return self._response == MbResponse.DELETE_COMMENTS

    def ask(self):
        self._ensure_response()

    def _ensure_response(self):
        if self._we_dont_have_response():
            self._we_ask()

    def _we_dont_have_response(self):
        return not bool(self._response)

    def _we_ask(self):
        self._response = MessageBoxes.existing_comments_during_import(self._parent)
