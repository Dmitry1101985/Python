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
        self.ui.pushButton_9.clicked.connect(lambda: get_all_devices_q(self))
        
        
        
        
    def addPg2(self):
        self.ui.n_max_q_2.setText('11.3')
        self.ui.n_min_q_2.setText('0.3')
        
    
    def addPg3(self):
        self.ui.n_max_q_3.setText('11.3')
        self.ui.n_min_q_3.setText('0.3')
        
        
    def addPg4(self):
        self.ui.n_max_q_4.setText('11.3')
        self.ui.n_min_q_4.setText('0.3')
        
        
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
   



def calc_device_q(data: list, rnd):
    n_p = float(data[0].text())
    n_q = float(data[1].text())
    eff_coeff = float(data[2].text())
    
    q = 0
    
    if n_q != 0 and n_p != 0:
        eff_coeff = n_p / n_q
        q = (n_p * 859.8) / (8100 * eff_coeff)
    elif n_p == 0:
        eff_coeff = 1
        q = (n_q * 859.8) / (8100 * eff_coeff)
    else:
        q = (n_p * 859.8) / (8100 * eff_coeff)
    
    return round(q, rnd), round(eff_coeff, 3)




def get_all_devices_q(self):
    y = 0
    for x in 0, 2, 4, 6:
        # first device
        # max
        x_2 = x + y * 5
        q_max, ccd_max = calc_device_q(self.ui.inputs[0 + x_2:3 + x_2], 2)
        q_sum = q_max * float(self.ui.inputs[6 + x_2].text())
        self.ui.outputs[0 + x].setText(str(round(q_sum, 2)))
        self.ui.inputs[2 + x_2].setText(str(ccd_max))
        # min
        q_min, ccd_min = calc_device_q(self.ui.inputs[3 + x_2:6 + x_2], 3)
        self.ui.outputs[1 + x].setText(str(q_min))
        self.ui.inputs[5 + x_2].setText(str(ccd_min))
        y += 1
    
    q_max_sum = self.ui.outputs[8]
    q_min_sum = self.ui.outputs[9]
    sum = 0
    
    for q in 0, 2, 4, 6:
        sum += round(float(self.ui.outputs[q].text()), 2)
    
    q_max_sum.setText(str(round(sum, 2)))
    
    min = 10000
        
    for m in 1, 3, 5, 7:
        current = round(float(self.ui.outputs[m].text()), 3)
        if min > current and current != 0:
            min = current
            
    q_min_sum.setText(str(min))    
    
    
app = QtWidgets.QApplication([])

application = Calc()
application.show()        

sys.exit(app.exec())   