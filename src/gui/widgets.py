from typing import List, Tuple

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt, QPoint, QModelIndex
from PyQt5.QtGui import QMouseEvent, QWheelEvent, QKeyEvent, QCursor, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QFrame, QTableView, QStatusBar, QMenu, QAbstractItemView, QLabel

from src import settings
from src.files import Files
from src.gui import delegates, utils
from src.gui.delegates import CommentTypeDelegate, CommentTimeDelegate, CommentNoteDelegate, TYPEWRITER_FONT
from src.gui.uihandler.main import MainHandler
from src.gui.utils import KEY_MAPPINGS
from src.player import bindings
from src.player.observedproperties import MpvPropertyObserver
from src.player.players import MpvPlayer, ActionType
from src.qcutils import Comment

_translate = QtCore.QCoreApplication.translate


class MpvWidget(QFrame):

    def __init__(self, main_handler: MainHandler):
        super(MpvWidget, self).__init__(main_handler)
        self.main_handler = main_handler
        self.application = main_handler.application

        self.setStyleSheet("background-color:black;")
        self.setMouseTracking(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.cursor_timer = QTimer(self)
        self.cursor_timer.setSingleShot(True)
        # noinspection PyUnresolvedReferences
        self.cursor_timer.timeout.connect(
            lambda arg=False, f=self.main_handler.display_mouse_cursor: f(arg))

        mpv = bindings.MPV(
            wid=str(int(self.winId())),
            keep_open="yes",
            idle="yes",
            osc="yes",
            cursor_autohide="no",
            input_cursor="no",
            input_default_bindings="no",
            config="yes",
            config_dir=Files.DIRECTORY_CONFIGURATION,
            ytdl="yes",
            # log_handler=mpvLogHandler,
        )

        MpvPropertyObserver(mpv)
        self.mpv_player = MpvPlayer(mpv)

    def mouseMoveEvent(self, e: QMouseEvent):

        if e.type() == QMouseEvent.MouseMove:
            try:
                self.mpv_player.mouse_move(e.pos().x(), e.pos().y())
            except OSError:
                # todo logger
                pass

        self.main_handler.display_mouse_cursor(display=True)

    def mousePressEvent(self, e: QMouseEvent):
        button = e.button()
        self.setFocus()

        if button == Qt.LeftButton:
            self.mpv_player.mouse_action(0, ActionType.DOWN)
        elif button == Qt.MiddleButton:
            self.mpv_player.mouse_action(1, ActionType.PRESS)
        elif button == Qt.RightButton and self.mpv_player.is_video_loaded():
            self.main_handler.widget_context_menu.exec_()
        elif button == Qt.BackButton:
            self.mpv_player.mouse_action(5, ActionType.PRESS)
        elif button == Qt.ForwardButton:
            self.mpv_player.mouse_action(6, ActionType.PRESS)

    def mouseReleaseEvent(self, e: QMouseEvent):
        button = e.button()

        if button == Qt.LeftButton:
            self.mpv_player.mouse_action(0, ActionType.UP)

    def mouseDoubleClickEvent(self, mev: QMouseEvent):
        button = mev.button()

        if button == Qt.LeftButton and self.mpv_player.video_file_current():
            self.main_handler.toggle_fullscreen()
            self.mpv_player.mouse_action(0, ActionType.PRESS)
        elif button == Qt.MiddleButton:
            self.mpv_player.mouse_action(1, ActionType.PRESS)
        elif button == Qt.BackButton:
            self.mpv_player.mouse_action(5, ActionType.PRESS)
        elif button == Qt.ForwardButton:
            self.mpv_player.mouse_action(6, ActionType.PRESS)
        else:
            return super().mouseDoubleClickEvent(mev)

    def wheelEvent(self, e: QWheelEvent):
        delta = e.angleDelta()

        x_d = delta.x()
        y_d = delta.y()

        if x_d == 0 and y_d != 0:
            if y_d > 0:
                self.mpv_player.mouse_action(3, ActionType.PRESS)
            else:
                self.mpv_player.mouse_action(4, ActionType.PRESS)
        else:
            super().wheelEvent(e)

    def keyPressEvent(self, e: QKeyEvent):
        mod = int(self.application.keyboardModifiers())
        key = e.key()
        cmd = ""

        # List view bindings
        if (key == Qt.Key_Up or key == Qt.Key_Down) and mod == Qt.NoModifier:
            self.main_handler.widget_comments.keyPressEvent(e)
        elif key == Qt.Key_Delete:
            self.main_handler.widget_comments.delete_current_selected_comment()
        elif key == Qt.Key_Return or key == Qt.Key_Backspace:  # Backspace or Enter
            self.main_handler.widget_comments.edit_current_selected_comment()
        elif key == Qt.Key_C and mod == Qt.CTRL:
            self.main_handler.widget_comments.copy_current_selected_comment()

        #
        elif key == Qt.Key_F and mod == Qt.NoModifier and self.mpv_player.is_video_loaded():
            self.main_handler.toggle_fullscreen()
        elif key == Qt.Key_E and mod == Qt.NoModifier and self.mpv_player.is_video_loaded():
            self.main_handler.widget_context_menu.exec_()
        elif key == Qt.Key_Escape and mod == Qt.NoModifier:
            self.main_handler.display_normal()
        elif key in KEY_MAPPINGS:
            cmd = utils.command_generator(mod, *KEY_MAPPINGS[key])
        elif key != 0:
            try:
                ks = chr(key)
            except ValueError:
                pass
            else:
                cmd = utils.command_generator(mod, ks, is_char=True)
        else:
            super(MpvWidget, self).keyPressEvent(e)

        if cmd:
            self.mpv_player.button_action(cmd, ActionType.PRESS)


class ContextMenu(QMenu):
    """
    Pseudo context menu when user right clicks into the video or presses the 'e' button.
    """

    def __init__(self, main_handler: MainHandler):
        super().__init__()
        self.main_handler = main_handler
        self.widget_comments = main_handler.widget_comments
        self.mpv_player = main_handler.widget_mpv.mpv_player
        self.update_entries()

    def update_entries(self):
        """
        Will update the entries of this context menu to match the comment types from the settings.
        """

        self.clear()

        ct_list = settings.Setting_Custom_General_COMMENT_TYPES.value
        if not ct_list:
            no_ct_action = _translate("CommentTypes",
                                      "No comment types defined." + " " + "Define new comment types in the settings.")
            ac = self.addAction(no_ct_action)
            ac.setEnabled(False)
        else:
            for ct in ct_list:
                act = self.addAction(ct)
                act.triggered.connect(lambda x, t=ct, f=self.widget_comments.add_comment: f(t))

    def exec_(self):
        """
        Will display the menu with comment types.
        """

        self.mpv_player.pause()
        self.main_handler.display_normal()

        m_pos = QCursor.pos()

        # Fixes following: Qt puts the context menu in a place
        # where double clicking would trigger the fist menu option
        # instead of just calling the menu a second time
        # or ignoring the second press
        super().exec_(QPoint(m_pos.x() + 1, m_pos.y()))


class CommentsTable(QTableView):
    """
    The comment table below the video.
    """

    def __init__(self, main_handler: MainHandler):
        super().__init__()
        self.main_handler = main_handler
        self.application = main_handler.application
        self.widget_mpv = main_handler.widget_mpv
        self.mpv_player = self.widget_mpv.mpv_player

        # Headers
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()

        # Model
        self.model = QStandardItemModel(self)
        self.setModel(self.model)

        # Delegates
        self.comment_time_delegate = CommentTimeDelegate(self, self.on_after_user_changed_time)
        self.comment_type_delegate = CommentTypeDelegate(self, self.on_after_user_changed_comment_type)
        self.comment_note_delegate = CommentNoteDelegate(self, self.on_after_user_changed_comment_note)
        self.setItemDelegateForColumn(0, self.comment_time_delegate)
        self.setItemDelegateForColumn(1, self.comment_type_delegate)
        self.setItemDelegateForColumn(2, self.comment_note_delegate)

        # Misc
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setWordWrap(True)
        self.setShowGrid(False)

        self.scroll_position = 0
        self.comments_amount = 0
        self.comments_up_to_date = True

    def delete_current_selected_comment(self) -> None:
        """
        Will delete the current selected comment row.
        If selection is empty, no action will be invoked.
        """

        def delete(selected: List[QModelIndex]):
            self.model.removeRows(selected[0].row(), 1)
            self.comments_up_to_date = False
            self.__update_row_count_in_status_bar()

        self.__do_with_selected_comment_row(delete)

    def edit_current_selected_comment(self) -> None:
        """
        Will start edit mode on selected comment row.
        If selection is empty, no action will be invoked.
        """

        def edit(selected: List[QModelIndex]):
            row = selected[0].row()
            idx = self.model.item(row, 2).index()
            self.edit(idx)
            self.comments_up_to_date = False

        self.__do_with_selected_comment_row(edit)

    def copy_current_selected_comment(self) -> None:
        """
        Will copy the complete row to clipboard.
        If selection is empty, no action will be invoked.
        """

        def copy(selected: List[QModelIndex]):
            row = selected[0].row()
            time = self.model.item(row, 0).text()
            coty = self.model.item(row, 1).text()
            note = self.model.item(row, 2).text()
            self.application.clipboard().setText("[{}][{}] {}".format(time, coty, note))

        self.__do_with_selected_comment_row(copy)

    def __do_with_selected_comment_row(self, consume_selected_function) -> None:
        """
        This function takes a **function** as argument.

        *It will call the function with the current selection as argument if selection is not empty.*

        :param consume_selected_function: The function to apply if selection is not empty
        """

        is_empty: bool = self.model.rowCount() == 0

        if not is_empty:
            selected = self.selectionModel().selectedRows()

            if selected:
                consume_selected_function(selected)

    def add_comment(self, comment_type: str, comment_text: str = "", time: str = None,
                    sort: bool = True, will_change_qc=True, edit_mode_active=True) -> None:
        """
        Will add a new comment type to the list view.

        :param comment_type: The comment type to add
        :param comment_text: The text to add
        :param time: The time to add. If None the current video time will be used.
        :param sort: If True, the complete table will be sorted after the insertion.
        :param edit_mode_active: True then edit mode will be started.
        :param will_change_qc: True if qc is changed with the addition.
        """

        if time is None:
            time: str = self.widget_mpv.mpv_player.position_current()

        ti = QStandardItem(time)
        ti.setFont(delegates.TYPEWRITER_FONT)

        ct = QStandardItem(_translate("CommentTypes", comment_type))
        ct.setFont(delegates.TYPEWRITER_FONT)

        note = QStandardItem(comment_text)

        new_entry = [ti, ct, note]
        self.model.appendRow([ti, ct, note])

        self.__after_comment_added(new_entry, sort, edit_mode_active, will_change_qc)

    def __after_comment_added(self, new_entry: List[QStandardItem], sort: bool,
                              edit_mode: bool, will_change_qc: bool) -> None:
        """

        :param new_entry: The newly added entry
        :param sort: If True, the complete table will be sorted after the insertion.
        :param edit_mode: True then edit mode will be started.
        :param will_change_qc: True if qc is changed with the addition.
        """

        self.__update_row_count_in_status_bar()

        if sort:
            self.sort()
        self.resizeColumnToContents(1)

        new_index = self.model.indexFromItem(new_entry[2])
        self.scrollTo(new_index)
        self.setCurrentIndex(new_index)

        if edit_mode:
            self.edit(new_index)

        if will_change_qc:
            self.comments_up_to_date = False

    def get_all_comments(self) -> Tuple[Comment]:
        """
        Returns all comments.

        :return: all comments.
        """

        ret_list = []
        model = self.model

        for r in range(0, model.rowCount()):
            time = model.item(r, 0).text()
            coty = model.item(r, 1).text()
            note = model.item(r, 2).text()
            ret_list.append(Comment(time=time, coty=coty, note=note))
        return tuple(ret_list)

    def reset_comments_table(self) -> None:
        """
        Will clear all comments.
        """

        self.model.clear()
        self.comments_up_to_date = True
        self.__update_row_count_in_status_bar()

    def on_before_fullscreen(self) -> None:
        """
        Action to invoke before switching to fullscreen.
        """

        self.scroll_position = self.verticalScrollBar().value()

    def on_after_fullscreen(self) -> None:
        """
        Action to invoke after switching back from fullscreen.
        """

        self.verticalScrollBar().setValue(self.scroll_position)

    def on_after_user_changed_time(self) -> None:
        """
        Action to invoke after time was changed manually by the user.
        """

        self.sort()
        self.comments_up_to_date = False

    def on_after_user_changed_comment_type(self) -> None:
        """
        Action to invoke after comment type was changed manually by the user.
        """

        self.resizeColumnToContents(1)
        self.comments_up_to_date = False

    def on_after_user_changed_comment_note(self) -> None:
        """
        Action to invoke after comment note was changed manually by the user.
        """

        self.comments_up_to_date = False

    def sort(self) -> None:
        """
        Will sort the comments table by time column.
        """

        self.sortByColumn(0, Qt.AscendingOrder)

    def __update_row_count_in_status_bar(self) -> None:
        """
        Updates the row count variable.
        """

        self.comments_amount = self.model.rowCount()

    def keyPressEvent(self, e: QKeyEvent):

        mod = int(self.application.keyboardModifiers())
        key = e.key()

        if (key == Qt.Key_Up or key == Qt.Key_Down) and mod == Qt.NoModifier:
            super().keyPressEvent(e)
        else:
            self.widget_mpv.keyPressEvent(e)

    def mousePressEvent(self, e: QMouseEvent):

        if e.button() == Qt.LeftButton:
            mdi: QModelIndex = self.indexAt(e.pos())
            if mdi.column() == 0 and self.mpv_player.is_video_loaded():
                position = self.model.item(mdi.row(), 0).text()
                self.widget_mpv.mpv_player.position_jump(position=position)
            elif mdi.column() == 1:
                self.edit(mdi)
            e.accept()
        super().mousePressEvent(e)


class StatusBar(QStatusBar):
    class ClickableQLabel(QLabel):
        """
        A QLabel which listens to left and right click.
        """

        def __init__(self):
            super().__init__()
            self.on_right_mouse_click = None
            self.on_left_mouse_click = None
            self.setFont(TYPEWRITER_FONT)

        def mousePressEvent(self, e: QMouseEvent):
            button = e.button()

            if button == Qt.LeftButton and self.on_left_mouse_click:
                self.on_left_mouse_click()
            elif button == Qt.RightButton and self.on_right_mouse_click:
                self.on_right_mouse_click()

    def __init__(self, main_handler):
        super().__init__(main_handler)
        self.main_handler = main_handler
        self.widget_comments = main_handler.widget_comments

        self.time_format = settings.Setting_Custom_Appearance_StatusBar_CurrentTime

        # Label and Widget
        def on_current_remaining_time_clicked():
            self.time_format.value = not self.time_format.value

        self.label_information = StatusBar.ClickableQLabel()
        self.label_information.on_left_mouse_click = on_current_remaining_time_clicked
        self.label_information.setAlignment(Qt.AlignRight)

        self.addPermanentWidget(QLabel(), 1)
        self.addPermanentWidget(self.label_information, 0)

        # Timer updates status bar each 50 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status_bar_text)
        self.timer.start(50)

    def update_status_bar_text(self) -> None:
        """
        Will update the current status bar information about video time and comments
        """

        comments = self.widget_comments.comments_amount

        time = MpvPropertyObserver.VIDEO_TIME_CURRENT \
            if self.time_format.value else MpvPropertyObserver.VIDEO_TIME_REMAINING

        percent = MpvPropertyObserver.VIDEO_PERCENT \
            if self.time_format.value else 100 - MpvPropertyObserver.VIDEO_PERCENT

        self.label_information.setText("#{}{:2}{:>8}{:2}{:3}%".format(comments, "", time, "", percent))
