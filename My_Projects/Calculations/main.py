import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


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
        get_all_data(self)
        self.ui.dev_2.hide()
        
    
    def dellDev3(self):
        self.ui.n_max_p_3.setText('0')
        self.ui.n_max_q_3.setText('0')
        self.ui.n_min_p_3.setText('0')
        self.ui.n_min_q_3.setText('0')
        self.ui.eff_coef_max_3.setText('1')
        self.ui.eff_coef_min_3.setText('1')
        self.ui.quantity_3.setText('1')
        get_all_data(self)
        self.ui.dev_3.hide()
        
        
    def dellDev4(self):
        self.ui.n_max_p_4.setText('0')
        self.ui.n_max_q_4.setText('0')
        self.ui.n_min_p_4.setText('0')
        self.ui.n_min_q_4.setText('0')
        self.ui.eff_coef_max_4.setText('1')
        self.ui.eff_coef_min_4.setText('1')
        self.ui.quantity_4.setText('1')
        get_all_data(self)
        self.ui.dev_4.hide()
        
    
    def inputChange(self):
        for input in self.ui.inputs:
            input.textChanged.connect(self.chek_data_and_calc)    
            
            
    def chek_data_and_calc(self, text):
        if text.replace(".", "").isdigit() and float(text) > 0:
            get_all_data(self)
        


def calc_device_q(data: list, rnd):
    
    if data[0].text().replace(".", "").isdigit():
        n_p = float(data[0].text())
    else:
        n_p = 0
    
    if data[1].text().replace(".", "").isdigit():
        n_q = float(data[1].text())
    else:
        n_q = 0       
    
    if data[2].text().replace(".", "").isdigit():
        eff_coeff = float(data[2].text())
    else:
        eff_coeff = 1
    
    
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
    
    min = 10
        
    for m in 1, 3, 5, 7:
        current = round(float(self.ui.outputs[m].text()), 3)
        if min > current and current != 0:
            min = current
            
    q_min_sum.setText(str(min))    
    

def calc_metrology(self):
    q_min_sum = round(float(self.ui.outputs[9].text()), 3)
    q_max_sum = round(float(self.ui.outputs[8].text()), 2)
    t_min_c = round(float(self.ui.inputs[29].text()), 2)
    t_max_c = round(float(self.ui.inputs[28].text()), 2)
    p_min_nad = round(float(self.ui.inputs[31].text()), 4)
    p_max_nad = round(float(self.ui.inputs[30].text()), 4)
    p_min_bar = 0.098
    p_max_bar = 0.102
    p_min_abs = p_min_nad + p_min_bar
    p_max_abs = p_max_nad + p_max_bar
    t_min_k = t_min_c + 273.15
    t_max_k = t_max_c + 273.15
    z_min = 1 - ((10.2*(p_max_abs + p_max_nad) - 6) * ((0.00345 * 0.60611) - 0.000446) + 0.015) * (1.3 - 0.0144 * ((t_min_c + 273.15) - 283))
    z_max = 1 - ((10.2*(p_min_abs + p_min_nad) - 6) * ((0.00345 * 0.60611) - 0.000446) + 0.015) * (1.3 - 0.0144 * ((t_max_c + 273.15) - 283))
    q_min_go = q_min_sum * t_min_k * 0.101325 * z_min / (p_max_abs * 293.15)
    q_max_go = q_max_sum * t_max_k * 0.101325 * z_max / (p_min_abs * 293.15)
    self.ui.outputs[10].setText(str(round(t_max_k, 2)))
    self.ui.outputs[11].setText(str(round(t_min_k, 2)))
    self.ui.outputs[12].setText(str(round(p_max_bar, 4)))
    self.ui.outputs[13].setText(str(round(p_min_bar, 4)))
    self.ui.outputs[14].setText(str(round(p_max_abs, 4)))
    self.ui.outputs[15].setText(str(round(p_min_abs, 4)))
    self.ui.outputs[16].setText(str(round(z_max, 5)))
    self.ui.outputs[17].setText(str(round(z_min, 5)))
    self.ui.outputs[18].setText(str(round(q_max_go, 2)))
    self.ui.outputs[19].setText(str(round(q_min_go, 3)))


def calc_gl_type(self):
    q_max_go = float(self.ui.outputs[18].text())
    q_min_go = float(self.ui.outputs[19].text())
    q_max_gl = 2.5
    q_min_gl = 0.016
    gl_type = 'G1.6'
    
    if q_max_go <= 2.5 and q_min_go >= 0.016:
        q_max_gl = 2.5
        q_min_gl = 0.016
        gl_type = 'G1.6'
    elif q_max_go <= 4 and q_max_go > 2.5 and q_min_go >= 0.016:
        q_max_gl = 4.0
        q_min_gl = 0.016
        gl_type = 'G2.5'
    elif q_max_go <= 6 and q_max_go > 4 and q_min_go >= 0.016:
        q_max_gl = 6.0
        q_min_gl = 0.016
        gl_type = 'G4'
    elif q_max_go <= 10 and q_max_go > 6 and q_min_go >= 0.025:
        q_max_gl = 10.0
        q_min_gl = 0.025
        gl_type = 'G6'
    elif q_max_go <= 16 and q_max_go > 10 and q_min_go >= 0.1:
        q_max_gl = 16.0
        q_min_gl = 0.1
        gl_type = 'G10'
    else:
        q_max_gl = 0
        q_min_gl = 0
        gl_type = 'None'
        
    self.ui.outputs[20].setText(str(q_min_gl))
    self.ui.outputs[21].setText(str(q_max_gl))
    self.ui.outputs[22].setText(gl_type)



def get_all_data(self):
    get_all_devices_q(self)
    calc_metrology(self)
    calc_gl_type(self)
    
    
app = QtWidgets.QApplication([])

application = Calc()
application.show()        

sys.exit(app.exec())