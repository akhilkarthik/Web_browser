import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QAction, QLineEdit, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QHBoxLayout, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.url_input = QLineEdit()

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.load_url)
        


        # Create navigation buttons
        self.refresh_button = QPushButton("R")
        self.back_button = QPushButton("<<")
        self.forward_button = QPushButton(">>")

        # Connect navigation button actions
        self.refresh_button.clicked.connect(self.refresh_page)
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)

        # Create a toolbar for navigation buttons
        self.nav_toolbar = QToolBar()
        self.nav_toolbar.addWidget(self.refresh_button)
        self.nav_toolbar.addWidget(self.back_button)
        self.nav_toolbar.addWidget(self.forward_button)


        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        # Create a horizontal layout for the address bar and Go button
        self.address_layout = QHBoxLayout()
        self.address_layout.addWidget(self.url_input)
        self.address_layout.addWidget(self.go_button)

        self.central_layout.addLayout(self.address_layout)
        self.central_layout.addWidget(self.nav_toolbar)
        self.central_layout.addWidget(self.browser)


        #aesthetics
        self.central_widget.setStyleSheet("background-color: #f0f0f0;")
        self.go_button.setStyleSheet("background-color: #007acc; color: white; border: 1px solid #005bb5;")
        self.url_input.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 5px;")
        self.nav_toolbar.setStyleSheet("background-color: #f0f0f0; border-bottom: 1px solid #ccc;")
        self.url_input.setStyleSheet("font-size: 14px; color: #333;")
        self.refresh_button.setStyleSheet("background-color: #007acc; color: white; border: 1px solid #005bb5;")
        self.back_button.setStyleSheet("background-color: #007acc; color: white; border: 1px solid #005bb5;")
        self.forward_button.setStyleSheet("background-color: #007acc; color: white; border: 1px solid #005bb5;")
        self.go_button.setFixedSize(50, 30)
        self.refresh_button.setFixedSize(30, 30)
        self.back_button.setFixedSize(30, 30)
        self.forward_button.setFixedSize(30, 30)






        

        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PyQt5 Web Browser")

    def load_url(self):
        url = self.url_input.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(QtCore.QUrl(url))

    def refresh_page(self):
        self.browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())