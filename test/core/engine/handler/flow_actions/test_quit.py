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


import unittest
from unittest.mock import patch, Mock

from mpvqc.core.engine.handler.flow_actions import QuitFlowQuestion
from test.core.engine import DEFAULT_OPTIONS


class TestSubtitleImportFlowActions(unittest.TestCase):
    MB_QUIT_DO_WE = 'mpvqc.core.engine.handler.flow_actions.quit.QuitUnsavedMessageBox.do_we_quit'

    def test_have_unsaved_changes(self):
        we = QuitFlowQuestion(DEFAULT_OPTIONS, have_unsaved_changes=True)
        self.assertTrue(we.have_unsaved_changes())

    def test_dont_have_unsaved_changes(self):
        we = QuitFlowQuestion(DEFAULT_OPTIONS, have_unsaved_changes=False)
        self.assertFalse(we.have_unsaved_changes())

    @patch(MB_QUIT_DO_WE)
    def test_ask_to_quit(self, mocked_ask: Mock):
        we = QuitFlowQuestion(DEFAULT_OPTIONS, have_unsaved_changes=True)
        we.ask_via_message_box_to_quit()
        mocked_ask.assert_called()

    def test_response_default(self):
        we = QuitFlowQuestion(DEFAULT_OPTIONS, have_unsaved_changes=True)
        self.assertFalse(we.get_the_response())

    @patch(MB_QUIT_DO_WE, return_value=True)
    def test_response_quit(self, *_):
        we = QuitFlowQuestion(DEFAULT_OPTIONS, have_unsaved_changes=True)
        we.ask_via_message_box_to_quit()
        self.assertTrue(we.get_the_response())
