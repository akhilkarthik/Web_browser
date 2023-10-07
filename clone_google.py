import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class ColorfulBrowser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a web view widget
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Create navigation buttons
        self.back_button = self.create_button("Back", self.webview.back)
        self.forward_button = self.create_button("Forward", self.webview.forward)
        self.refresh_button = self.create_button("Refresh", self.webview.reload)
        self.home_button = self.create_button("Home", self.navigate_home)

        # Create a search bar
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Search or enter URL")
        self.search_bar.returnPressed.connect(self.load_url)

        # Create layout for navigation buttons and search bar
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.search_bar)

        # Create main layout
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.webview)

        self.setLayout(layout)

        # Initialize the web view
        self.webview.setUrl(QtCore.QUrl("https://www.google.com"))

    def create_button(self, text, action):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(action)
        button.setStyleSheet("background-color: #4285F4; color: white; border: none;")
        return button

    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.webview.setUrl(QtCore.QUrl(url))

    def navigate_home(self):
        self.webview.setUrl(QtCore.QUrl("https://www.google.com"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    browser = ColorfulBrowser()
    browser.setWindowTitle("Colorful Web Browser")
    browser.setGeometry(100, 100, 1024, 768)
    browser.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class ColorfulBrowser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a web view widget
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Create navigation buttons
        self.back_button = self.create_button("Back", self.webview.back)
        self.forward_button = self.create_button("Forward", self.webview.forward)
        self.refresh_button = self.create_button("Refresh", self.webview.reload)
        self.home_button = self.create_button("Home", self.navigate_home)

        # Create a search bar
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Search or enter URL")
        self.search_bar.returnPressed.connect(self.load_url)

        # Create layout for navigation buttons and search bar
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.search_bar)

        # Create main layout
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.webview)

        self.setLayout(layout)

        # Initialize the web view
        self.webview.setUrl(QtCore.QUrl("https://www.google.com"))

    def create_button(self, text, action):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(action)
        button.setStyleSheet("background-color: #4285F4; color: white; border: none;")
        return button

    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.webview.setUrl(QtCore.QUrl(url))

    def navigate_home(self):
        self.webview.setUrl(QtCore.QUrl("https://www.google.com"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    browser = ColorfulBrowser()
    browser.setWindowTitle("Colorful Web Browser")
    browser.setGeometry(100, 100, 1024, 768)
    browser.show()
    sys.exit(app.exec_())
