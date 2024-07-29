# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(180, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(180, 380))
        Widget.setMaximumSize(QSize(180, 380))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 161, 101))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 144, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_MW3PortNumber = QLineEdit(self.layoutWidget)
        self.lineEdit_MW3PortNumber.setObjectName(u"lineEdit_MW3PortNumber")

        self.horizontalLayout.addWidget(self.lineEdit_MW3PortNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButtonMW3Connect = QPushButton(self.layoutWidget)
        self.pushButtonMW3Connect.setObjectName(u"pushButtonMW3Connect")

        self.verticalLayout.addWidget(self.pushButtonMW3Connect)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 120, 161, 91))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 151, 56))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_PixelSizeUM = QLineEdit(self.widget)
        self.lineEdit_PixelSizeUM.setObjectName(u"lineEdit_PixelSizeUM")

        self.horizontalLayout_2.addWidget(self.lineEdit_PixelSizeUM)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.pushButton_StartDrawing = QPushButton(self.widget)
        self.pushButton_StartDrawing.setObjectName(u"pushButton_StartDrawing")

        self.verticalLayout_5.addWidget(self.pushButton_StartDrawing)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(11, 216, 161, 151))
        self.widget1 = QWidget(self.groupBox_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 30, 161, 114))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ReadyForExposures = QPushButton(self.widget1)
        self.pushButton_ReadyForExposures.setObjectName(u"pushButton_ReadyForExposures")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_ReadyForExposures.sizePolicy().hasHeightForWidth())
        self.pushButton_ReadyForExposures.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.pushButton_ReadyForExposures)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_Dose = QLineEdit(self.widget1)
        self.lineEdit_Dose.setObjectName(u"lineEdit_Dose")

        self.verticalLayout_2.addWidget(self.lineEdit_Dose)

        self.lineEdit_Focus = QLineEdit(self.widget1)
        self.lineEdit_Focus.setObjectName(u"lineEdit_Focus")

        self.verticalLayout_2.addWidget(self.lineEdit_Focus)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.pushButton_StartTheExposure = QPushButton(self.widget1)
        self.pushButton_StartTheExposure.setObjectName(u"pushButton_StartTheExposure")
        sizePolicy1.setHeightForWidth(self.pushButton_StartTheExposure.sizePolicy().hasHeightForWidth())
        self.pushButton_StartTheExposure.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.pushButton_StartTheExposure)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Drawing", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"MW3 connection", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Port", None))
        self.lineEdit_MW3PortNumber.setText(QCoreApplication.translate("Widget", u"8888", None))
        self.pushButtonMW3Connect.setText(QCoreApplication.translate("Widget", u"Connect!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Drawing", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Pixel size (um)", None))
        self.lineEdit_PixelSizeUM.setText(QCoreApplication.translate("Widget", u"1.0", None))
        self.pushButton_StartDrawing.setText(QCoreApplication.translate("Widget", u"Start drawing!", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Exposure", None))
        self.pushButton_ReadyForExposures.setText(QCoreApplication.translate("Widget", u"Ready for exposures!", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Dose (mJ/cm2)", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Focus (um)", None))
        self.lineEdit_Dose.setText(QCoreApplication.translate("Widget", u"100", None))
        self.lineEdit_Focus.setText(QCoreApplication.translate("Widget", u"0", None))
        self.pushButton_StartTheExposure.setText(QCoreApplication.translate("Widget", u"Start the exposure!", None))
    # retranslateUi

