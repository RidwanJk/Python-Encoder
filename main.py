from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

def encode(text):
    lst = []
    for ch in text:
        lst.append(ch)
    for i in range(len(lst)):
        lst[i] = chr(ord(lst[i]) + 1)
    encoded = "".join(lst)
    return encoded
        
def decode(text):
    lst = []
    for ch in text:
        lst.append(ch)
    for i in range(len(lst)):
        lst[i] = chr(ord(lst[i]) - 1)
    decoded = "".join(lst)
    return decoded
    
class Window(QWidget):
    def __init__(self):
        super().__init__()        

        layout = QVBoxLayout()
        self.btnLabel = QLabel("Encode or Decode", self)
        layout.addWidget(self.btnLabel)
        
        self.Encode_or_decode = QLineEdit(self)
        layout.addWidget(self.Encode_or_decode)
        
        self.button_encode = QPushButton("Encode", self)
        self.button_encode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_encode)
        
        self.button_decode = QPushButton("Decode", self)
        self.button_decode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_decode)
        
        self.resultLabel = QLabel("", self)
        layout.addWidget(self.resultLabel)
        
        self.setLayout(layout)        
        self.oldPos = self.pos()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition()
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition() - self.oldPos
            new_x = int(self.x() + delta.x())
            new_y = int(self.y() + delta.y())
            self.move(new_x, new_y)
            self.oldPos = event.globalPosition()
            super().mouseMoveEvent(event)
            
    def on_button_click(self):
        input_text = self.Encode_or_decode.text()
        if self.sender() == self.button_encode:
            result = encode(input_text)
        else:
            result = decode(input_text)
        
        self.resultLabel.setText(result)

def main():
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()
    
if __name__ == "__main__":
    main()
