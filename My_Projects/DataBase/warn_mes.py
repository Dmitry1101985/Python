from PyQt5 import QtWidgets
import sys
from warn_mes_ui import Ui_WarningMessage

class WM(QtWidgets.QDialog):
    def __init__(self):
        super(WM, self).__init__()
        self.ui = Ui_WarningMessage()
        self.ui.setupUi(self)
        self.init_Ui()
        
        
        
    def init_Ui(self ):
        self.ui.btnOk.clicked.connect(lambda: self.close())
        pass
    
    
    def set_text(self, mess, ex):
        self.ui.label_3.setText(ex)
        self.ui.message.setText(mess)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = WM()
    application.setFixedSize(475, 220)
    application.show()
    sys.exit(app.exec())