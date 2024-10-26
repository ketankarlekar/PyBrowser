from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
    def __init__(self):
        super(MyWebBrowser, self).__init__()

        self.setWindowTitle("PyBrowser")

        self.window = QWidget()
        self.setCentralWidget(self.window)  # Set the central widget

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # Use QLineEdit for the URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setMinimumWidth(400)  # Set minimum width for better visibility

        self.go_btn = QPushButton("GO")
        self.backward_btn = QPushButton("<")
        self.forward_btn = QPushButton(">")

        # Set button colors using stylesheets
        self.go_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;"
                                  " border-radius: 10px; padding: 5px; border: none; ")
        self.backward_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;"
                                        " border-radius: 10px; padding: 5px; border: none; ")
        self.forward_btn.setStyleSheet("background-color: #2196F3; color: white; font-weight: bold;"
                                       " border-radius: 10px; padding: 5px; border: none; ")

        # Set minimum height and width for buttons
        for btn in [self.go_btn, self.backward_btn, self.forward_btn]:
            btn.setMinimumHeight(30)
            btn.setMinimumWidth(100)

        # Adding buttons and URL bar to horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.backward_btn)
        self.horizontal.addWidget(self.forward_btn)

        # Initialize the browser
        self.browser = QWebEngineView()  # Create an instance of QWebEngineView
        self.browser.setUrl(QUrl("http://google.com"))  # Load Google on startup

        # Connect buttons to functions
        self.go_btn.clicked.connect(lambda : self.navigate(self.url_bar.text()))
        self.backward_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        # Adding layouts to the main layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # Set the layout for the window
        self.window.setLayout(self.layout)

    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://" + url
            self.url_bar.setText(url)

        if url.startswith("http://") or url.startswith("https://"):
            self.browser.setUrl(QUrl(url))
            self.url_bar.clear()  # Clear the URL bar after navigation
        else:
            QMessageBox.warning(self, "Invalid URL", "Please enter a valid URL.")

# Application initialization
if __name__ == "__main__":
    app = QApplication([])
    window = MyWebBrowser()
    window.show()  # Show the main window
    app.exec_()