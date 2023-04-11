import sys
import os
import openpyxl
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTextEdit, QMessageBox
from ui import Ui_MainWindow
from PyQt5.QtPrintSupport import QPrinter
from pass_dialog import PasswordDialog
from pass_change import ChangePassword


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
        
        self.ui.label_85.setGeometry(QtCore.QRect(310, 780, 450, 21))
        self.ui.label_85.setText("Powered by Python. Dmytro Sherstiuk. Ukraine 2033.")
        
        self.ui.btn_add_2.clicked.connect(lambda: self.ui.dev_2.show())
        self.ui.btn_del_2.clicked.connect(lambda: self.dellDev2())
        self.ui.btn_add_3.clicked.connect(lambda: self.ui.dev_3.show())
        self.ui.btn_del_3.clicked.connect(lambda: self.dellDev3())
        self.ui.btn_add_4.clicked.connect(lambda: self.ui.dev_4.show())
        self.ui.btn_del_4.clicked.connect(lambda: self.dellDev4())
        self.ui.btn_add_pg_2.clicked.connect(lambda: self.addPg2())
        self.ui.btn_add_pg_3.clicked.connect(lambda: self.addPg3())
        self.ui.btn_add_pg_4.clicked.connect(lambda: self.addPg4())
        # self.createEditor()
        self.ui.pushButton_8.clicked.connect(lambda: self.print_to_pdf())
        self.ui.pushButton_8.setShortcut("Ctrl+P")
        self.ui.pushButton_7.clicked.connect(lambda: self.write_to_excel())
        self.ui.pushButton_6.clicked.connect(lambda: change_pass(self))
        self.inputChange()
        
        
    
    def print_to_pdf(self):
        # printer = QPrinter(QPrinter.HighResolution)
        # dialog = QPrintDialog(printer, self)
        # if dialog.exec_() == QPrintDialog.Accepted:
        #     self.textEdit.print_(printer)
        
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOrientation(QPrinter.Landscape)
        printer.setOutputFileName(os.path.join(os.path.dirname(__file__), 'screen.pdf'))
        application.render(printer)
        self.show_message_pdf()
       
        
    def write_to_excel(self):
        wb = openpyxl.load_workbook(os.path.join(os.path.dirname(__file__), 'gl_calc.xlsx'))
        sheet = wb['Sheet1']
        sheet['I16'] = self.ui.quantity.text()
        sheet['I17'] = self.ui.quantity_2.text()
        sheet['I18'] = self.ui.quantity_3.text()
        sheet['I19'] = self.ui.quantity_4.text()
        sheet['I20'] = self.get_total_quantity()
        sheet['J16'] = self.get_used_n(float(self.ui.n_max_p.text()), float(self.ui.n_max_q.text()))
        sheet['J17'] = self.get_used_n(float(self.ui.n_max_p_2.text()), float(self.ui.n_max_q_2.text()))
        sheet['J18'] = self.get_used_n(float(self.ui.n_max_p_3.text()), float(self.ui.n_max_q_3.text()))
        sheet['J19'] = self.get_used_n(float(self.ui.n_max_p_4.text()), float(self.ui.n_max_q_4.text()))
        sheet['M16'] = self.get_one_div_q(float(self.ui.q_max_dev.text()), float(self.ui.quantity.text()))
        sheet['M17'] = self.get_one_div_q(float(self.ui.q_max_dev_2.text()), float(self.ui.quantity_2.text()))
        sheet['M18'] = self.get_one_div_q(float(self.ui.q_max_dev_3.text()), float(self.ui.quantity_3.text()))
        sheet['M19'] = self.get_one_div_q(float(self.ui.q_max_dev_4.text()), float(self.ui.quantity_4.text()))
        sheet['N16'] = self.ui.q_max_dev.text()
        sheet['N17'] = self.ui.q_max_dev_2.text()
        sheet['N18'] = self.ui.q_max_dev_3.text()
        sheet['N19'] = self.ui.q_max_dev_4.text()
        sheet['N20'] = self.ui.q_max_sum.text()
        sheet['I21'] = self.ui.q_max_sum.text()
        sheet['H24'] = self.ui.q_min_sum.text()
        sheet['H25'] = self.get_min_n()
        sheet['F27'] = self.get_used_n(float(self.ui.n_max_p.text()), float(self.ui.n_max_q.text()))
        sheet['F28'] = self.get_used_n(float(self.ui.n_max_p_2.text()), float(self.ui.n_max_q_2.text()))
        sheet['F29'] = self.get_used_n(float(self.ui.n_max_p_3.text()), float(self.ui.n_max_q_3.text()))
        sheet['F30'] = self.get_used_n(float(self.ui.n_max_p_4.text()), float(self.ui.n_max_q_4.text()))
        sheet['I27'] = self.ui.eff_coef_max.text()
        sheet['I28'] = self.ui.eff_coef_max_2.text()
        sheet['I29'] = self.ui.eff_coef_max_3.text()
        sheet['I30'] = self.ui.eff_coef_max_4.text()
        sheet['L27'] = self.get_one_div_q(float(self.ui.q_max_dev.text()), float(self.ui.quantity.text()))
        sheet['L28'] = self.get_one_div_q(float(self.ui.q_max_dev_2.text()), float(self.ui.quantity_2.text()))
        sheet['L29'] = self.get_one_div_q(float(self.ui.q_max_dev_3.text()), float(self.ui.quantity_3.text()))
        sheet['L30'] = self.get_one_div_q(float(self.ui.q_max_dev_4.text()), float(self.ui.quantity_4.text()))
        sheet['F32'] = self.get_dev_min(float(self.ui.n_min_p.text()), float(self.ui.n_min_q.text()))
        sheet['F33'] = self.get_dev_min(float(self.ui.n_min_p_2.text()), float(self.ui.n_min_q_2.text()))
        sheet['F34'] = self.get_dev_min(float(self.ui.n_min_p_3.text()), float(self.ui.n_min_q_3.text()))
        sheet['F35'] = self.get_dev_min(float(self.ui.n_min_p_4.text()), float(self.ui.n_min_q_4.text()))
        sheet['L32'] = self.ui.q_min_dev.text()
        sheet['L33'] = self.ui.q_min_dev_2.text()
        sheet['L34'] = self.ui.q_min_dev_3.text()
        sheet['L35'] = self.ui.q_min_dev_4.text()
        sheet['I32'] = self.ui.eff_coef_min.text()
        sheet['I33'] = self.ui.eff_coef_min_2.text()
        sheet['I34'] = self.ui.eff_coef_min_3.text()
        sheet['I35'] = self.ui.eff_coef_min_4.text()
        sheet['F38'] = self.ui.t_max_c.text()
        sheet['F39'] = self.ui.t_min_c.text()
        sheet['H38'] = self.ui.t_max_k.text()
        sheet['H39'] = self.ui.t_min_k.text()
        sheet['C42'] = self.get_max_go_string()
        sheet['C43'] = self.get_min_go_string()
        sheet['C46'] = self.ui.gl_type.text()
        sheet['D48'] = self.ui.gl_max.text()
        sheet['F48'] = self.ui.q_max_go.text()
        sheet['K48'] = self.ui.gl_min.text()
        sheet['N48'] = self.ui.q_min_go.text()
        
        wb.save(os.path.join(os.path.dirname(__file__), 'gl_calc.xlsx'))
        self.show_message_excel() 
    
    
    # def createEditor(self):
    #     self.textEdit = QTextEdit(self)
    #     self.textEdit.hide()
    #     self.textEdit.setText(self.ui.q_max_dev.text())
    
    
    
            
    
    def get_total_quantity(self):
        sum_quant = 0
        for x in 6, 13, 20, 27:
            sum_quant += int(self.ui.inputs[x].text())
        return sum_quant        
  
    
    def get_used_n(self, p, q):
        if q == 0:
            return p
        elif p != 0 and q != 0:
            return p
        else:
            return round(q, 1)  
        
    
    def get_one_div_q(self, q, quant):
        return q / quant
    
    
    def get_min_n(self):
        min = 10.0
        for x in 3, 4, 10, 11, 17, 18, 24, 25:
            p = float(self.ui.inputs[x].text())
            if p != 0:
                if p < min:
                    min = p
        return round(min, 2)
    
    
    def get_dev_min(self, p, q):
        if p != 0:
            return round(p, 2)
        else:
            return round(q, 2)
                
    
    def get_min_go_string(self):
        q_min = self.ui.q_min_sum.text()
        t_min_k = self.ui.t_min_k.text()
        z_min = self.ui.z_min.text()
        p_max = self.ui.p_max_abs.text()
        q_min_qo = self.ui.q_min_go.text()
        
        return f"{q_min} x {t_min_k} x 0.101325 x {z_min} / {p_max} x 293.15 = {q_min_qo}"
    
    
    def get_max_go_string(self):
        q_max = self.ui.q_max_sum.text()
        t_max_k = self.ui.t_max_k.text()
        z_max = self.ui.z_max.text()
        p_min = self.ui.p_min_abs.text()
        q_max_qo = self.ui.q_max_go.text()
        
        return f"{q_max} x {t_max_k} x 0.101325 x {z_max} / {p_min} x 293.15 = {q_max_qo}"
    
        
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
    
    
    def show_message_pdf(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('PDF')
        message.setText(f"PDF-файл збережено за адресою:\n {os.path.join(os.path.dirname(__file__), 'screen.pdf')}")
        message.addButton(QMessageBox.Ok)
        result = message.exec_()    

    
    def show_message_excel(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('Excel')
        message.setText(f"Дані розрахунку збережено в Excel за адресою:\n {os.path.join(os.path.dirname(__file__), 'gl_calc.xlsx')}")
        message.addButton(QMessageBox.Ok)
        result = message.exec_()
    

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
   


def change_pass(self):
    pcd = ChangePassword()
    pcd.exec()
    
    
    
if __name__ == "__main__":    
    app = QtWidgets.QApplication([])
    application = Calc()
    application.setFixedSize(1011, 817)
    application.show()        
    sys.exit(app.exec())