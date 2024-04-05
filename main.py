from PyQt5.QtWidgets import QApplication
from clsmainForm import clsmainForm
from GlobleData import GlobleData
import sys
if len(sys.argv)>1:
    GlobleData.projectPath= sys.argv[1]
app = QApplication([])
f = clsmainForm()
f.show()
sys.exit(app.exec_())