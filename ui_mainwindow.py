# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QHeaderView,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QComboBox, QLabel, QGroupBox)

class Ui_btn_send(object):
    def setupUi(self, btn_send):
        if not btn_send.objectName():
            btn_send.setObjectName(u"btn_send")
        btn_send.resize(900, 700)
        self.centralwidget = QWidget(btn_send)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_chat = QListWidget(self.tab)
        self.list_chat.setObjectName(u"list_chat")

        self.verticalLayout_2.addWidget(self.list_chat)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_input = QLineEdit(self.tab)
        self.txt_input.setObjectName(u"txt_input")

        self.horizontalLayout.addWidget(self.txt_input)

        self.btn_send_2 = QPushButton(self.tab)
        self.btn_send_2.setObjectName(u"btn_send_2")

        self.horizontalLayout.addWidget(self.btn_send_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        
        # Search and Filter Bar
        self.filter_layout = QHBoxLayout()
        self.filter_layout.setObjectName(u"filter_layout")
        
        # Search input
        self.lbl_search = QLabel(self.tab_2)
        self.lbl_search.setObjectName(u"lbl_search")
        self.filter_layout.addWidget(self.lbl_search)
        
        self.txt_search = QLineEdit(self.tab_2)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setMinimumWidth(150)
        self.filter_layout.addWidget(self.txt_search)
        
        # Filter combo box
        self.lbl_filter = QLabel(self.tab_2)
        self.lbl_filter.setObjectName(u"lbl_filter")
        self.filter_layout.addWidget(self.lbl_filter)
        
        self.cmb_filter = QComboBox(self.tab_2)
        self.cmb_filter.setObjectName(u"cmb_filter")
        self.cmb_filter.addItem("Ngày")
        self.cmb_filter.addItem("Tuần")
        self.cmb_filter.addItem("Tháng")
        self.cmb_filter.addItem("Tất cả")
        self.filter_layout.addWidget(self.cmb_filter)
        
        # Search button
        self.btn_search = QPushButton(self.tab_2)
        self.btn_search.setObjectName(u"btn_search")
        self.filter_layout.addWidget(self.btn_search)
        
        # Export JSON button
        self.btn_export = QPushButton(self.tab_2)
        self.btn_export.setObjectName(u"btn_export")
        self.filter_layout.addWidget(self.btn_export)
        
        self.filter_layout.addStretch()
        
        self.verticalLayout_4.addLayout(self.filter_layout)
        
        # Main content layout
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.calendar_widget = QCalendarWidget(self.tab_2)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))

        self.horizontalLayout_2.addWidget(self.calendar_widget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        
        # Table with 5 columns now (added Nhac nho)
        self.table_events = QTableWidget(self.tab_2)
        if (self.table_events.columnCount() < 5):
            self.table_events.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_events.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_events.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_events.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_events.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_events.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_events.setObjectName(u"table_events")
        self.table_events.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_events.setSelectionMode(QTableWidget.SingleSelection)

        self.verticalLayout_5.addWidget(self.table_events)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add = QPushButton(self.tab_2)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.tab_2)
        self.btn_edit.setObjectName(u"btn_edit")

        self.horizontalLayout_3.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.tab_2)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        
        # ==================== TAB 3: LICH SU NHAC NHO ====================
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        
        # Filter for reminder history
        self.reminder_filter_layout = QHBoxLayout()
        self.reminder_filter_layout.setObjectName(u"reminder_filter_layout")
        
        self.lbl_reminder_filter = QLabel(self.tab_3)
        self.lbl_reminder_filter.setObjectName(u"lbl_reminder_filter")
        self.reminder_filter_layout.addWidget(self.lbl_reminder_filter)
        
        self.cmb_reminder_filter = QComboBox(self.tab_3)
        self.cmb_reminder_filter.setObjectName(u"cmb_reminder_filter")
        self.cmb_reminder_filter.addItem("Tất cả")
        self.cmb_reminder_filter.addItem("Đã thông báo")
        self.cmb_reminder_filter.addItem("Chưa thông báo")
        self.reminder_filter_layout.addWidget(self.cmb_reminder_filter)
        
        self.btn_refresh_reminders = QPushButton(self.tab_3)
        self.btn_refresh_reminders.setObjectName(u"btn_refresh_reminders")
        self.reminder_filter_layout.addWidget(self.btn_refresh_reminders)
        
        self.reminder_filter_layout.addStretch()
        
        self.verticalLayout_6.addLayout(self.reminder_filter_layout)
        
        # Reminder history table
        self.table_reminders = QTableWidget(self.tab_3)
        if (self.table_reminders.columnCount() < 6):
            self.table_reminders.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_reminders.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.table_reminders.setObjectName(u"table_reminders")
        self.table_reminders.setSelectionBehavior(QTableWidget.SelectRows)
        
        self.verticalLayout_6.addWidget(self.table_reminders)
        
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        btn_send.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(btn_send)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        btn_send.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(btn_send)
        self.statusbar.setObjectName(u"statusbar")
        btn_send.setStatusBar(self.statusbar)

        self.retranslateUi(btn_send)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(btn_send)
    # setupUi

    def retranslateUi(self, btn_send):
        btn_send.setWindowTitle(QCoreApplication.translate("btn_send", u"Trợ Lý Quản Lý Lịch Trình", None))
        
        # Tab 1: Chat
        self.txt_input.setPlaceholderText(QCoreApplication.translate("btn_send", u"Nhập lệnh tại đây...", None))
        self.btn_send_2.setText(QCoreApplication.translate("btn_send", u"Gui", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("btn_send", u"Chat với trợ lý", None))
        
        # Tab 2: Quản lý lịch
        self.lbl_search.setText(QCoreApplication.translate("btn_send", u"Tìm kiếm:", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("btn_send", u"Nhập tên sự kiện...", None))
        self.lbl_filter.setText(QCoreApplication.translate("btn_send", u"Lọc theo:", None))
        self.btn_search.setText(QCoreApplication.translate("btn_send", u"Tìm", None))
        self.btn_export.setText(QCoreApplication.translate("btn_send", u"Xuất JSON", None))
        
        ___qtablewidgetitem = self.table_events.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("btn_send", u"ID", None))
        ___qtablewidgetitem1 = self.table_events.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("btn_send", u"Sự kiện", None))
        ___qtablewidgetitem2 = self.table_events.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("btn_send", u"Thời gian", None))
        ___qtablewidgetitem3 = self.table_events.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("btn_send", u"Địa điểm", None))
        ___qtablewidgetitem4 = self.table_events.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("btn_send", u"Nhắc nhở", None))
        
        self.btn_add.setText(QCoreApplication.translate("btn_send", u"Thêm Sự kiện", None))
        self.btn_edit.setText(QCoreApplication.translate("btn_send", u"Sửa Sự kiện", None))
        self.btn_delete.setText(QCoreApplication.translate("btn_send", u"Xóa Sự kiện", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("btn_send", u"Quản lý Lịch", None))
        
        # Tab 3: Lịch sử nhắc nhở
        self.lbl_reminder_filter.setText(QCoreApplication.translate("btn_send", u"Trạng thái:", None))
        self.btn_refresh_reminders.setText(QCoreApplication.translate("btn_send", u"Làm mới", None))
        
        ___qtablewidgetitem5 = self.table_reminders.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("btn_send", u"ID", None))
        ___qtablewidgetitem6 = self.table_reminders.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("btn_send", u"Sự kiện", None))
        ___qtablewidgetitem7 = self.table_reminders.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("btn_send", u"Thời gian SK", None))
        ___qtablewidgetitem8 = self.table_reminders.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("btn_send", u"Nhắc trước", None))
        ___qtablewidgetitem9 = self.table_reminders.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("btn_send", u"Thời gian nhắc", None))
        ___qtablewidgetitem10 = self.table_reminders.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("btn_send", u"Trạng thái", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("btn_send", u"Lịch sử nhắc nhở", None))
    # retranslateUi
