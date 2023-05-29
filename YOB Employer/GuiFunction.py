from PyQt5 import QtWidgets, QtGui, QtCore
#Cree Button
def buttonF(left,top,lwith,lheigth,style,window,title):
    buttonf = QtWidgets.QPushButton(title,window)
    buttonf.setStyleSheet('font-family:myriad arabic;')
    buttonf.move(left,top)
    buttonf.resize(lwith,lheigth)
    buttonf.setStyleSheet(style)
    return buttonf
#Cree window
def windowF(wwith,wheigth,title,iconPath,PathPixmap):
    windowf = QtWidgets.QWidget()
    windowf.setFixedSize(wwith,wheigth)
    windowf.setWindowTitle(title)
    windowf.setWindowIcon(QtGui.QIcon(iconPath))
    label = QtWidgets.QLabel(windowf)
    pixmap = QtGui.QPixmap(PathPixmap).scaled(wwith,wheigth)
    label.setPixmap(pixmap)
    return  windowf
#cree lael
def labelF(left,top,lwith,lheight,style,window,title):
    labelf = QtWidgets.QLabel(title,window)
    labelf.move(left, top)
    labelf.resize(lwith,lheight)
    labelf.setStyleSheet(style)
    return labelf
#input
def inputF(left,top,iwith,iheight,style,window,placeholder):
    inputf = QtWidgets.QLineEdit(window)
    inputf.setPlaceholderText(placeholder)
    inputf.setStyleSheet(style)
    inputf.move(left,top)
    inputf.resize(iwith,iheight)
    inputf.setAlignment(QtCore.Qt.AlignCenter)
    return inputf
#Cree ComboBox
def comboBoxF(left,top,cwith,cheigth,style,window):
    comboBoxf = QtWidgets.QComboBox(window)
    comboBoxf.move(left, top)
    comboBoxf.resize(cwith, cheigth)
    comboBoxf.setStyleSheet(style)
    return comboBoxf