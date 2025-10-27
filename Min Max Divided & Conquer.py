import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    min_left, max_left = find_min_max(left_half)
    min_right, max_right = find_min_max(right_half)
    
    min_value = min(min_left, min_right)
    max_value = max(max_left, max_right)
    
    return min_value, max_value

class MinMaxFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bilangan terbesar dan terkecil")
        self.setup_ui()
        
    def setup_ui(self):
        self.input_label = QLabel("Masukkan Angka acak (Gunakan koma sebagai pemisah):")
        self.input_entry = QLineEdit()
        
        self.find_button = QPushButton("Cari")
        self.find_button.clicked.connect(self.find)
        
        self.result_label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_entry)
        layout.addWidget(self.find_button)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
    def find(self):
        input_list = [int(x) for x in self.input_entry.text().split(",")]
        if len(input_list) == 0:
            QMessageBox.critical(self, "Error", "Masukkan angka dengan benar!.")
            return
        
        min_val, max_val = find_min_max(input_list)
        self.result_label.setText(f"Angka Terkecil : {min_val}\nAngka Terbesar : {max_val}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MinMaxFinder()
    window.show()
    sys.exit(app.exec_()) 