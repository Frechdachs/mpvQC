from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QFrame

from src.player import bindings
from src.player.players import MpvPlayer


class MpvWidget(QFrame):

    def __init__(self, parent=None):
        super(MpvWidget, self).__init__(parent)

        self.setStyleSheet("background-color:black;")
        self.setMouseTracking(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.cursor_timer = QTimer(self)
        self.cursor_timer.setSingleShot(True)
        # self.cursortimer.timeout.connect(hideCursor)

        mpv_mpv = bindings.MPV(
            wid=str(int(self.winId())),
            keep_open="yes",
            idle="yes",
            osc="yes",
            cursor_autohide="no",
            input_cursor="no",
            input_default_bindings="no",
            config="yes",
            # config_dir=self.paths.dir_main_cfg,
            ytdl="yes",
            # log_handler=mpvLogHandler,
        )
        self.mpv_player = MpvPlayer(mpv_mpv)

    def mousePressEvent(self, mouse_event: QtGui.QMouseEvent):

        
        return self.mpv_player.handle_mouse_button_events(mouse_event)
