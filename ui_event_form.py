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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateTimeEdit, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(359, 397)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        Dialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_title_event = QLabel(Dialog)
        self.lb_title_event.setObjectName(u"lb_title_event")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_title_event.sizePolicy().hasHeightForWidth())
        self.lb_title_event.setSizePolicy(sizePolicy)
        self.lb_title_event.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lb_title_event.setFont(font1)
        self.lb_title_event.setFrameShape(QFrame.Shape.NoFrame)
        self.lb_title_event.setScaledContents(False)
        self.lb_title_event.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_title_event)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.txt_event = QLineEdit(Dialog)
        self.txt_event.setObjectName(u"txt_event")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.txt_event.setFont(font3)

        self.horizontalLayout.addWidget(self.txt_event)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.dt_start = QDateTimeEdit(Dialog)
        self.dt_start.setObjectName(u"dt_start")
        self.dt_start.setFont(font2)
        self.dt_start.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))

        self.horizontalLayout_3.addWidget(self.dt_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.txt_location = QLineEdit(Dialog)
        self.txt_location.setObjectName(u"txt_location")
        self.txt_location.setFont(font3)

        self.horizontalLayout_4.addWidget(self.txt_location)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.sb_reminder = QSpinBox(Dialog)
        self.sb_reminder.setObjectName(u"sb_reminder")
        self.sb_reminder.setFont(font2)

        self.horizontalLayout_5.addWidget(self.sb_reminder)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.buttonBox.setFont(font4)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Thêm Sự kiện", None))
        self.lb_title_event.setText(QCoreApplication.translate("Dialog", u"Thêm Sự kiện", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Tên sự kiện:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Thời gian:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Địa điểm:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nhắc trước (phút):", None))
    # retranslateUi
