import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the text edit widget for output
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Create the line edit widget for user input
        self.line_edit = QLineEdit(self)

        # Create the submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit)

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.submit_button)

        # Create the central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def submit(self):
        # Get the user input text
        input_text = self.line_edit.text()

        # Clear the line edit widget
        self.line_edit.clear()

        # Append the input text to the text edit widget
        self.text_edit.append(input_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
