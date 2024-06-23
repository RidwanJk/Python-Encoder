import base64
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel

# Encode and decode functions
def encode(text):
    return ''.join(chr(ord(ch) + 1) for ch in text)

def decode(text):
    return ''.join(chr(ord(ch) - 1) for ch in text)

def base64_encode(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def base64_decode(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

def caesar_cipher_encode(text, shift=3):
    result = ""
    for ch in text:
        if ch.isalpha():
            shift_base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - shift_base + shift) % 26 + shift_base)
        else:
            result += ch
    return result

def caesar_cipher_decode(text, shift=3):
    return caesar_cipher_encode(text, -shift)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def morse_encode(text):
    return ' '.join(MORSE_CODE_DICT[ch.upper()] if ch.upper() in MORSE_CODE_DICT else ch for ch in text)

def morse_decode(text):
    morse_dict_reversed = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(morse_dict_reversed[ch] if ch in morse_dict_reversed else ch for ch in text.split())

# PyQt6 Window class
class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.btnLabel = QLabel("Encode or Decode", self)
        layout.addWidget(self.btnLabel, 0, 0, 1, 2)

        self.Encode_or_decode = QLineEdit(self)
        layout.addWidget(self.Encode_or_decode, 1, 0, 1, 2)

        self.button_encode = QPushButton("Encode", self)
        self.button_encode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_encode, 2, 0)

        self.button_decode = QPushButton("Decode", self)
        self.button_decode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_decode, 2, 1)

        self.button_base64_encode = QPushButton("Base64 Encode", self)
        self.button_base64_encode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_base64_encode, 3, 0)

        self.button_base64_decode = QPushButton("Base64 Decode", self)
        self.button_base64_decode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_base64_decode, 3, 1)

        self.button_caesar_encode = QPushButton("Caesar Encode", self)
        self.button_caesar_encode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_caesar_encode, 4, 0)

        self.button_caesar_decode = QPushButton("Caesar Decode", self)
        self.button_caesar_decode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_caesar_decode, 4, 1)

        self.button_morse_encode = QPushButton("Morse Encode", self)
        self.button_morse_encode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_morse_encode, 5, 0)

        self.button_morse_decode = QPushButton("Morse Decode", self)
        self.button_morse_decode.clicked.connect(self.on_button_click)
        layout.addWidget(self.button_morse_decode, 5, 1)

        self.resultLabel = QLabel("", self)
        layout.addWidget(self.resultLabel, 6, 0, 1, 2)

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
        elif self.sender() == self.button_decode:
            result = decode(input_text)
        elif self.sender() == self.button_base64_encode:
            result = base64_encode(input_text)
        elif self.sender() == self.button_base64_decode:
            result = base64_decode(input_text)
        elif self.sender() == self.button_caesar_encode:
            result = caesar_cipher_encode(input_text)
        elif self.sender() == self.button_caesar_decode:
            result = caesar_cipher_decode(input_text)
        elif self.sender() == self.button_morse_encode:
            result = morse_encode(input_text)
        elif self.sender() == self.button_morse_decode:
            result = morse_decode(input_text)

        self.resultLabel.setText(result)

def main():
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()

if __name__ == "__main__":
    main()
