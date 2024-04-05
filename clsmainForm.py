import os

from PyQt5.QtWidgets import QMainWindow,QMessageBox

from GlobleData import GlobleData
from mainForm import Ui_MainWindow


class clsmainForm(QMainWindow):
    def __init__(self):
        super(clsmainForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.txtProjectPath.setText(GlobleData.projectPath)
        # self.ui.txtProjectPath.setText(r"F:\siddharth_python\ETtestPrproject")



    def btnSMOkClick(self):
        if self.ui.chkSMoverwriteMain.isChecked():
            path = self.ui.txtProjectPath.text()
            filename = 'main.py'
            with open(os.path.join(path, filename), 'w') as temp_file:
                if self.ui.chkSMaddModuleInSeprateFolder.isChecked():
                    temp_file.write(
                        "from PyQt5.QtWidgets import QApplication\nfrom " + self.ui.txtSMmoduleName.text() +"."+self.ui.txtSMclassName.text() + " import " + self.ui.txtSMclassName.text() + "\nimport sys\napp = QApplication([])\nf = "+ self.ui.txtSMclassName.text()+"()\nf.show()\nsys.exit(app.exec_())\n")
                else:
                    temp_file.write("from PyQt5.QtWidgets import QApplication\nfrom "+ self.ui.txtSMclassName.text() +" import "+ self.ui.txtSMclassName.text() +"\nimport sys\napp = QApplication([])\nf = "+self.ui.txtSMclassName.text()+"()\nf.show()\nsys.exit(app.exec_())\n")

        if self.ui.chkSMaddClassFile.isChecked():
            if self.ui.txtSMclassName.text()!="":
                if self.ui.chkSMaddModuleInSeprateFolder.isChecked():
                    path = self.ui.txtProjectPath.text()+"\\"+self.ui.txtSMmoduleName.text()+"_"
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filename = self.ui.txtSMclassName.text() + '.py'
                    with open(os.path.join(path, filename), 'w') as temp_file:
                        temp_file.write("from PyQt5.QtWidgets import QMainWindow \nfrom "+ self.ui.txtSMmoduleName.text()+" import Ui_MainWindow \nclass "+ self.ui.txtSMclassName.text()+"(QMainWindow): \n\tdef __init__(self):\n\t\tsuper("+ self.ui.txtSMclassName.text()+", self).__init__()\n\t\tself.ui = Ui_MainWindow()\n\t\tself.ui.setupUi(self)\n")
                    if self.ui.chkSMaddUIfile.isChecked():
                        filename = self.ui.txtSMmoduleName.text()+ '.ui'
                        with open(os.path.join(path, filename), 'w') as temp_file:
                            temp_file.write("""<?xml version="1.0" encoding="UTF-8"?>
                            <ui version="4.0">
                             <class>MainWindow</class>
                             <widget class="QMainWindow" name="MainWindow">
                              <property name="geometry">
                               <rect>
                                <x>0</x>
                                <y>0</y>
                                <width>800</width>
                                <height>600</height>
                               </rect>
                              </property>
                              <property name="windowTitle">
                               <string>MainWindow</string>
                              </property>
                              <widget class="QWidget" name="centralwidget"/>
                              <widget class="QMenuBar" name="menubar">
                               <property name="geometry">
                                <rect>
                                 <x>0</x>
                                 <y>0</y>
                                 <width>800</width>
                                 <height>26</height>
                                </rect>
                               </property>
                              </widget>
                              <widget class="QStatusBar" name="statusbar"/>
                             </widget>
                             <resources/>
                             <connections/>
                            </ui>""")

                else:
                    path= self.ui.txtProjectPath.text()
                    filename = self.ui.txtSMclassName.text() + '.py'
                    with open(os.path.join(path, filename), 'w') as temp_file:
                        temp_file.write("from PyQt5.QtWidgets import QMainWindow \nfrom "+ self.ui.txtSMmoduleName.text()+" import Ui_MainWindow \nclass "+ self.ui.txtSMclassName.text()+"(QMainWindow): \n\tdef __init__(self):\n\t\tsuper("+ self.ui.txtSMclassName.text()+", self).__init__()\n\t\tself.ui = Ui_MainWindow()\n\t\tself.ui.setupUi(self)\n")
                    if self.ui.chkSMaddUIfile.isChecked():
                        filename = self.ui.txtSMmoduleName.text() + '.ui'
                        with open(os.path.join(path, filename), 'w') as temp_file:
                            temp_file.write("""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>""")
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The Process Has Been Completed Successfully")
        msg.setWindowTitle("Task Completed User")
        retval=msg.exec_()

    def txtSMmoduleNameTextChange(self):
        moduleName= self.ui.txtSMmoduleName.text()
        moduleName=moduleName.replace(" ","")
        self.ui.txtSMmoduleName.setText(moduleName)
        self.ui.txtSMclassName.setText("cls"+moduleName)
