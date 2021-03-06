# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './file_analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_project_admin(object):
    def setupUi(self, project_admin):
        project_admin.setObjectName("project_admin")
        project_admin.resize(852, 719)
        self.tabWidget = QtWidgets.QTabWidget(project_admin)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 851, 731))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("font: 75 10pt \"Century Gothic\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.show_admin_info = QtWidgets.QPushButton(self.tab_3)
        self.show_admin_info.setGeometry(QtCore.QRect(10, 10, 831, 31))
        self.show_admin_info.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.show_admin_info.setObjectName("show_admin_info")
        self.toolBox = QtWidgets.QToolBox(self.tab_3)
        self.toolBox.setGeometry(QtCore.QRect(10, 50, 831, 621))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 831, 559))
        self.page.setObjectName("page")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 50, 481, 501))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(0, 20, 811, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(600, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(490, 300, 321, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setGeometry(QtCore.QRect(550, 340, 261, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(490, 340, 131, 31))
        self.label_10.setObjectName("label_10")
        self.show_table_2 = QtWidgets.QPushButton(self.page)
        self.show_table_2.setGeometry(QtCore.QRect(490, 100, 321, 41))
        self.show_table_2.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"")
        self.show_table_2.setObjectName("show_table_2")
        self.select_table_2 = QtWidgets.QComboBox(self.page)
        self.select_table_2.setGeometry(QtCore.QRect(490, 50, 321, 31))
        self.select_table_2.setEditable(False)
        self.select_table_2.setObjectName("select_table_2")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.delete_values_1 = QtWidgets.QPushButton(self.page)
        self.delete_values_1.setGeometry(QtCore.QRect(490, 150, 321, 41))
        self.delete_values_1.setStyleSheet("background-color: rgb(255, 93, 93);\n"
"font: 75 10pt \"Century Gothic\";")
        self.delete_values_1.setObjectName("delete_values_1")
        self.delete_values_3 = QtWidgets.QPushButton(self.page)
        self.delete_values_3.setGeometry(QtCore.QRect(490, 200, 321, 41))
        self.delete_values_3.setStyleSheet("background-color: rgb(255, 110, 110);")
        self.delete_values_3.setObjectName("delete_values_3")
        self.sort_1 = QtWidgets.QPushButton(self.page)
        self.sort_1.setGeometry(QtCore.QRect(490, 520, 321, 31))
        self.sort_1.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.sort_1.setObjectName("sort_1")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 831, 559))
        self.page_2.setObjectName("page_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 50, 481, 511))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 811, 31))
        self.label_4.setObjectName("label_4")
        self.select_table_3 = QtWidgets.QComboBox(self.page_2)
        self.select_table_3.setGeometry(QtCore.QRect(490, 50, 321, 31))
        self.select_table_3.setObjectName("select_table_3")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.update_2 = QtWidgets.QPushButton(self.page_2)
        self.update_2.setGeometry(QtCore.QRect(490, 150, 321, 41))
        self.update_2.setObjectName("update_2")
        self.show_table_3 = QtWidgets.QPushButton(self.page_2)
        self.show_table_3.setGeometry(QtCore.QRect(490, 100, 321, 41))
        self.show_table_3.setObjectName("show_table_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 300, 321, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(490, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(600, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_2.setGeometry(QtCore.QRect(550, 340, 261, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.delete_values_2 = QtWidgets.QPushButton(self.page_2)
        self.delete_values_2.setGeometry(QtCore.QRect(490, 200, 321, 41))
        self.delete_values_2.setObjectName("delete_values_2")
        self.sort_2 = QtWidgets.QPushButton(self.page_2)
        self.sort_2.setGeometry(QtCore.QRect(490, 530, 321, 31))
        self.sort_2.setObjectName("sort_2")
        self.toolBox.addItem(self.page_2, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.show_about = QtWidgets.QPushButton(self.widget)
        self.show_about.setGeometry(QtCore.QRect(10, 10, 831, 31))
        self.show_about.setObjectName("show_about")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 831, 611))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.widget, "")

        self.retranslateUi(project_admin)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(project_admin)

    def retranslateUi(self, project_admin):
        _translate = QtCore.QCoreApplication.translate
        project_admin.setWindowTitle(_translate("project_admin", "Form"))
        self.show_admin_info.setText(_translate("project_admin", "Показать информацию об администраторе"))
        self.label_7.setText(_translate("project_admin", "Выбранная таблица"))
        self.label_8.setText(_translate("project_admin", "Данная таблица о "))
        self.label_9.setText(_translate("project_admin", "Сортировка"))
        self.lineEdit.setPlaceholderText(_translate("project_admin", "Введите имя пользователя"))
        self.label_10.setText(_translate("project_admin", "По ID"))
        self.show_table_2.setText(_translate("project_admin", "Показать таблицу"))
        self.select_table_2.setPlaceholderText(_translate("project_admin", "Выбрать таблицу..."))
        self.select_table_2.setItemText(0, _translate("project_admin", "auth_group"))
        self.select_table_2.setItemText(1, _translate("project_admin", "auth_group_permissions"))
        self.select_table_2.setItemText(2, _translate("project_admin", "auth_permission"))
        self.select_table_2.setItemText(3, _translate("project_admin", "auth_user"))
        self.select_table_2.setItemText(4, _translate("project_admin", "auth_user_groups"))
        self.select_table_2.setItemText(5, _translate("project_admin", "auth_user_user_permissions"))
        self.delete_values_1.setText(_translate("project_admin", "Удалить значения таблицы"))
        self.delete_values_3.setText(_translate("project_admin", "Сбросить фильтры"))
        self.sort_1.setText(_translate("project_admin", "Сортировать"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("project_admin", "auth таблицы"))
        self.label_3.setText(_translate("project_admin", "Выбранная таблица"))
        self.label_4.setText(_translate("project_admin", "Данная таблица о "))
        self.select_table_3.setPlaceholderText(_translate("project_admin", "Выбрать таблицу..."))
        self.select_table_3.setItemText(0, _translate("project_admin", "django_admin_log"))
        self.select_table_3.setItemText(1, _translate("project_admin", "django_content_type"))
        self.select_table_3.setItemText(2, _translate("project_admin", "django_migrations"))
        self.select_table_3.setItemText(3, _translate("project_admin", "django_session"))
        self.update_2.setText(_translate("project_admin", "Сбросить фильтры"))
        self.show_table_3.setText(_translate("project_admin", "Показать таблицу"))
        self.lineEdit_2.setPlaceholderText(_translate("project_admin", "Введите имя пользователя"))
        self.label_12.setText(_translate("project_admin", "По ID"))
        self.label_11.setText(_translate("project_admin", "Сортировка"))
        self.delete_values_2.setText(_translate("project_admin", "Удалить значения таблицы"))
        self.sort_2.setText(_translate("project_admin", "Сортировать"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("project_admin", "django таблицы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("project_admin", "Администратор"))
        self.show_about.setText(_translate("project_admin", "Показать информацию"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("project_admin", "О проекте"))
