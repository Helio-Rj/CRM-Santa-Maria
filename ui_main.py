# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(814, 715)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(57, 114, 171);\n"
"border-radius: 5px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ClosedHandCursor))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_cima = QFrame(self.centralwidget)
        self.frame_cima.setObjectName(u"frame_cima")
        self.frame_cima.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_cima.setFrameShape(QFrame.StyledPanel)
        self.frame_cima.setFrameShadow(QFrame.Raised)
        self.main_frame = QFrame(self.frame_cima)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(10, 10, 771, 261))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.cadastro = QLabel(self.main_frame)
        self.cadastro.setObjectName(u"cadastro")
        self.cadastro.setGeometry(QRect(10, 10, 231, 16))
        self.cadastro.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 255);")
        self.frame_cadastro = QFrame(self.main_frame)
        self.frame_cadastro.setObjectName(u"frame_cadastro")
        self.frame_cadastro.setGeometry(QRect(10, 30, 741, 211))
        self.frame_cadastro.setStyleSheet(u"background-color: rgb(247 247, 247);")
        self.frame_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QFrame.Raised)
        self.txt_cnpj = QLineEdit(self.frame_cadastro)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setGeometry(QRect(20, 60, 113, 20))
        self.txt_cnpj.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)
        self.txt_numero = QLineEdit(self.frame_cadastro)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(20, 120, 91, 20))
        self.txt_numero.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_numero.setAlignment(Qt.AlignCenter)
        self.txt_cep = QLineEdit(self.frame_cadastro)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(590, 150, 141, 20))
        self.txt_cep.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_cep.setAlignment(Qt.AlignCenter)
        self.txt_email = QLineEdit(self.frame_cadastro)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(370, 180, 361, 20))
        self.txt_email.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_email.setAlignment(Qt.AlignCenter)
        self.txt_logradouro = QLineEdit(self.frame_cadastro)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setGeometry(QRect(20, 90, 711, 20))
        self.txt_logradouro.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)
        self.txt_nome_empresarial = QLineEdit(self.frame_cadastro)
        self.txt_nome_empresarial.setObjectName(u"txt_nome_empresarial")
        self.txt_nome_empresarial.setGeometry(QRect(140, 60, 591, 20))
        self.txt_nome_empresarial.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_nome_empresarial.setAlignment(Qt.AlignCenter)
        self.txt_complemento = QLineEdit(self.frame_cadastro)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setGeometry(QRect(120, 120, 361, 20))
        self.txt_complemento.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_complemento.setAlignment(Qt.AlignCenter)
        self.txt_uf = QLineEdit(self.frame_cadastro)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setGeometry(QRect(530, 150, 51, 20))
        self.txt_uf.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_uf.setAlignment(Qt.AlignCenter)
        self.txt_tel_cel = QLineEdit(self.frame_cadastro)
        self.txt_tel_cel.setObjectName(u"txt_tel_cel")
        self.txt_tel_cel.setGeometry(QRect(20, 180, 341, 20))
        self.txt_tel_cel.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"")
        self.txt_tel_cel.setAlignment(Qt.AlignCenter)
        self.txt_municipio = QLineEdit(self.frame_cadastro)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setGeometry(QRect(20, 150, 501, 20))
        self.txt_municipio.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_municipio.setAlignment(Qt.AlignCenter)
        self.txt_bairro = QLineEdit(self.frame_cadastro)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(490, 120, 241, 20))
        self.txt_bairro.setStyleSheet(u"font: 87 7pt \"Arial Black\";")
        self.txt_bairro.setAlignment(Qt.AlignCenter)
        self.txt_cnpj_pesquisa = QLineEdit(self.frame_cadastro)
        self.txt_cnpj_pesquisa.setObjectName(u"txt_cnpj_pesquisa")
        self.txt_cnpj_pesquisa.setGeometry(QRect(210, 20, 241, 21))
        self.txt_cnpj_pesquisa.setStyleSheet(u"background-color: rgb(255, 250, 230);\n"
"\n"
"font: 87 9pt \"Arial Black\";")
        self.txt_cnpj_pesquisa.setAlignment(Qt.AlignCenter)
        self.pesquisa_label = QLabel(self.frame_cadastro)
        self.pesquisa_label.setObjectName(u"pesquisa_label")
        self.pesquisa_label.setGeometry(QRect(30, 20, 181, 21))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.pesquisa_label.setFont(font)
        self.pesquisa_label.setStyleSheet(u"font: 87 9pt \"Arial Black\";\n"
"color: rgb(85, 0, 255);")
        self.btn_cadastrar = QPushButton(self.frame_cima)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(590, 280, 160, 31))
        self.btn_cadastrar.setMinimumSize(QSize(160, 31))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(109, 109, 164);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"			\n"
"	\n"
"	\n"
"	font: 87 9pt \"Arial Black\";	\n"
"	\n"
"	background-color: rgb(163, 163, 245);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.frame_cima)

        self.frame_baixo = QFrame(self.centralwidget)
        self.frame_baixo.setObjectName(u"frame_baixo")
        self.frame_baixo.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_baixo.setFrameShape(QFrame.StyledPanel)
        self.frame_baixo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_baixo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_tabela = QFrame(self.frame_baixo)
        self.frame_tabela.setObjectName(u"frame_tabela")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.frame_tabela.setFont(font1)
        self.frame_tabela.setFrameShape(QFrame.StyledPanel)
        self.frame_tabela.setFrameShadow(QFrame.Raised)
        self.label_info_rodape = QLabel(self.frame_tabela)
        self.label_info_rodape.setObjectName(u"label_info_rodape")
        self.label_info_rodape.setGeometry(QRect(580, 290, 181, 16))
        self.label_info_rodape.setStyleSheet(u"font: 25 9pt \"Yu Gothic\";")
        self.tb_company = QTableWidget(self.frame_tabela)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setGeometry(QRect(20, 40, 571, 192))
        self.tb_company.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(148, 148, 148);\n"
"\n"
"	color: rgb(255, 255, 255);	\n"
"\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_info = QLabel(self.frame_tabela)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(20, 10, 231, 16))
        self.label_info.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 255);")
        self.frame_buttons = QFrame(self.frame_tabela)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(610, 39, 141, 191))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_buttons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_excel = QPushButton(self.frame_buttons)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(50, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_excel.setFont(font2)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{	\n"
"	\n"
"	background-color: rgb(171, 255, 165);	\n"
"\n"
"	border-radius: 15px;	\n"
"\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";\n"
"	\n"
"	background-color: rgb(66, 206, 41);	\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.gridLayout.addWidget(self.btn_excel, 0, 0, 1, 1)

        self.btn_excluir = QPushButton(self.frame_buttons)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(50, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{		\n"
"	\n"
";\n"
"	background-color: rgb(255, 164, 164);\n"
"\n"
"	border-radius: 15px;	\n"
"\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";		\n"
"	\n"
"	background-color: rgb(255, 120, 120);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.gridLayout.addWidget(self.btn_excluir, 2, 0, 1, 1)

        self.btn_alterar = QPushButton(self.frame_buttons)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(50, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 211, 52);\n"
"	\n"
"	border-radius: 15px;\n"
"	\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.gridLayout.addWidget(self.btn_alterar, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_tabela)


        self.verticalLayout.addWidget(self.frame_baixo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Empresas", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00b0", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_nome_empresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_tel_cel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TEL/CEL", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txt_cnpj_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CNPJ aqui.", None))
        self.pesquisa_label.setText(QCoreApplication.translate("MainWindow", u"Pesquisa por CNPJ", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_info_rodape.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Puritoka Zaybatsu 2024", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TEL/CEL", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None));
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Listagem de Empresas", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
    # retranslateUi

