# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:36:55 2018

@author: Fei
"""

import sys
import os
try:
    from PyQt5.QtWidgets import (QMainWindow, QApplication,QAction,QFileDialog,\
                                 QTextEdit,QTableWidgetItem,QDialog)
    from PyQt5.QtGui import (QIcon,QKeySequence)
    from PyQt5.QtCore import Qt
    PYQT = 5
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    PYQT = 4
from GUI import GUI


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.table = GUI()
        self.ManuBar()
        self.setCentralWidget(self.table) 
        self.StatusBar()
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Elastic properties')

    def CreateAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            getattr(action, signal).connect(slot)
#            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action        

    """
    This part is about the ManuBar
    """
    def ManuBarFile(self):
        self.fileNewAction = self.CreateAction(text="&New", slot=self.fileNew,
                                          shortcut=QKeySequence.New,
                                          icon=os.path.join(os.getcwd(), 'image', 'new-file.png'),
                                          tip ="Create an new file")
        self.fileLoadAction = self.CreateAction(text="&Load", slot=self.fileLoad,
                                          shortcut=QKeySequence.Open,
                                          icon=os.path.join(os.getcwd(), 'image', 'open-file.png'),
                                          tip ="Load file")  
        self.fileSaveAction = self.CreateAction(text="&Save", slot=self.fileSave,
                                          shortcut=QKeySequence.Save,
                                          icon=os.path.join(os.getcwd(), 'image', 'save-file.png'),
                                          tip ="Save file")          
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.fileNewAction)
        self.fileMenu.addAction(self.fileLoadAction)
        self.fileMenu.addAction(self.fileSaveAction)
        
    def ManuBar(self):
        self.ManuBarFile()
        
    def fileNew(self):
        for i in range(6):
            for j in range(6):
                self.table.table.setItem(i,j, QTableWidgetItem("0(0)"))
        self.table.text.setText(' ')
        
    def fileLoad(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle('Load File')
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_() == QDialog.Accepted:        
            fileName = dialog.selectedFiles()[0]
        c = [[],[],[],[],[],[]]
        for row in range(6):
            for col in range(6):
                c[row].append(self.table.table.item(row,col).text())    
        if fileName:
            file1 = open(fileName,'r')
        for row,line in enumerate(file1):
            line = line.split(' ')
            for col, num in enumerate(line):
                self.table.table.setItem(row,col, QTableWidgetItem(num))
        file1.close()
        self.table.text.setText(' ')
        print ('loaded')
            
    def fileSave(self): 
        options = QFileDialog.Options()
        fileName = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;", options=options)
        fileName = fileName[0]
        c = [[],[],[],[],[],[]]
        for row in range(6):
            for col in range(6):
                c[row].append(self.table.table.item(row,col).text())      
        if fileName:
            if fileName[-4:] != '.txt':
                file1 = open(fileName+'.txt','w')
            else:
                file1 = open(fileName,'w')
        for row in range(6):
            for col in range(6):
                file1.write((c[col][row]))
                file1.write(' ')
            file1.write('\n')
        file1.close()         
            
    '''
    This part is status bar
    '''   
    def StatusBar(self):
        self.status = self.statusBar()
        self.status.showMessage('Message in statusbar.')

            
if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance() 
    Gui = MainWindow()
    Gui.show()
    app.exec_()