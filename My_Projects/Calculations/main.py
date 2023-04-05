import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow


class Calc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        
        
    def init_UI(self):
        self.ui.dev_2.hide()
        self.ui.dev_3.hide()
        self.ui.dev_4.hide()
        
        self.ui.label_85.setGeometry(QtCore.QRect(450, 780, 150, 21))
        self.ui.label_85.setText("Powered by Python")
        
        self.ui.btn_add_2.clicked.connect(lambda: self.ui.dev_2.show())
        self.ui.btn_del_2.clicked.connect(lambda: self.dellDev2())
        self.ui.btn_add_3.clicked.connect(lambda: self.ui.dev_3.show())
        self.ui.btn_del_3.clicked.connect(lambda: self.dellDev3())
        self.ui.btn_add_4.clicked.connect(lambda: self.ui.dev_4.show())
        self.ui.btn_del_4.clicked.connect(lambda: self.dellDev4())
        self.ui.btn_add_pg_2.clicked.connect(lambda: self.addPg2())
        self.ui.btn_add_pg_3.clicked.connect(lambda: self.addPg3())
        self.ui.btn_add_pg_4.clicked.connect(lambda: self.addPg4())
        self.inputChange()
        self.ui.pushButton_9.clicked.connect(lambda: test(self))
        
        
        
        
    def addPg2(self):
        self.ui.n_max_q_2.setText('11.3')
        self.ui.n_min_q_2.setText('0.32')
        
    
    def addPg3(self):
        self.ui.n_max_q_3.setText('11.3')
        self.ui.n_min_q_3.setText('0.32')
        
        
    def addPg4(self):
        self.ui.n_max_q_4.setText('11.3')
        self.ui.n_min_q_4.setText('0.32')
        
        
    def dellDev2(self):
        self.ui.n_max_p_2.setText('0')
        self.ui.n_max_q_2.setText('0')
        self.ui.n_min_p_2.setText('0')
        self.ui.n_min_q_2.setText('0')
        self.ui.eff_coef_max_2.setText('1')
        self.ui.eff_coef_min_2.setText('1')
        self.ui.quantity_2.setText('1')
        self.ui.dev_2.hide()
        
    
    def dellDev3(self):
        self.ui.n_max_p_3.setText('0')
        self.ui.n_max_q_3.setText('0')
        self.ui.n_min_p_3.setText('0')
        self.ui.n_min_q_3.setText('0')
        self.ui.eff_coef_max_3.setText('1')
        self.ui.eff_coef_min_3.setText('1')
        self.ui.quantity_3.setText('1')
        self.ui.dev_3.hide()
        
        
    def dellDev4(self):
        self.ui.n_max_p_4.setText('0')
        self.ui.n_max_q_4.setText('0')
        self.ui.n_min_p_4.setText('0')
        self.ui.n_min_q_4.setText('0')
        self.ui.eff_coef_max_4.setText('1')
        self.ui.eff_coef_min_4.setText('1')
        self.ui.quantity_4.setText('1')
        self.ui.dev_4.hide()
        
    
    def inputChange(self):
        for input in self.ui.inputs:
            input.textChanged.connect(lambda: self.ui.label.setText("TRUE"))    
   

def calc_device(n_p, n_q, eff_coeff):
    q = 0
    
    if n_q != 0 and n_p != 0:
        eff_coeff = n_p / n_q
        q = (n_p * 859.8) / (8100 * eff_coeff)
    elif n_p == 0:
        eff_coeff = 1
        q = (n_q * 859.8) / (8100 * eff_coeff)
    else:
        q = (n_p * 859.8) / (8100 * eff_coeff)
    
    return round(q, 2), round(eff_coeff, 2)
    

def test(self):
    
    q, ccd = calc_device(float(self.ui.inputs[0].text()), float(self.ui.inputs[1].text()), float(self.ui.inputs[2].text()))
    self.ui.outputs[0].setText(str(q))
    self.ui.inputs[2].setText(str(ccd))
    
app = QtWidgets.QApplication([])

application = Calc()
application.show()        

sys.exit(app.exec())   