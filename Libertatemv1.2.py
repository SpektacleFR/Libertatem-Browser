from sys import argv

from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(1500, 800)

        # Browser Source
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.duckduckgo.com'))
        self.browser.urlChanged.connect(self.update_AddressBar)
        self.setCentralWidget(self.browser)
        self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.browser.page().fullScreenRequested.connect(self.FullscreenRequest)

        # Set up Navigation Bar
        self.navigation_bar = QToolBar('Navigation Toolbar')
        self.addToolBar(self.navigation_bar)
        self.navigation_bar.setAttribute(Qt.Qt.WA_StyledBackground, True)
        self.navigation_bar.setMinimumSize(0, 75)
        self.navigation_bar.setMovable(False)
        self.navigation_bar.setStyleSheet(
            """
            QToolBar{background-color: #EEEEEE; padding: left 10%; spacing: 10%;}
            QLineEdit{background-color: white; border: 1px solid transparent; border-radius: 10px; padding: 8px; selection-background-color: gray;}
            QPushButton{background-color: white; border: 1px solid transparent; border-radius: 15px; max-width: 50px; max-height: 50px; min-width: 50px; min-height: 50px; padding: 0px;}
            QPushButton:focus:pressed{background-color: #DDDDDD;}
            QPushButton:hover{background-color: #F0F0F0;}
            """)

        # Add the Back Button
        self.back_button = QPushButton("←", self)
        self.back_button.setStatusTip('Go to previous page you visited')
        self.back_button.clicked.connect(self.browser.back)
        self.navigation_bar.addWidget(self.back_button)
        self.back_button.setFont(QFont('', 20))
        self.back_button.setToolTip("Go Back")
        self.back_button.setCheckable(False)

        # Add the Forward Button
        self.next_button = QPushButton("→", self)
        self.next_button.setStatusTip('Go to next page')
        self.next_button.clicked.connect(self.browser.forward)
        self.navigation_bar.addWidget(self.next_button)
        self.next_button.setFont(QFont('', 20))
        self.next_button.setToolTip("Go Forward")
        self.next_button.setCheckable(False)

        # Add the Refresh Button
        self.refresh_button = QPushButton("⟳", self)
        self.refresh_button.setStatusTip('Refresh this page')
        self.refresh_button.clicked.connect(self.browser.reload)
        self.navigation_bar.addWidget(self.refresh_button)
        self.refresh_button.setFont(QFont('', 20))
        self.refresh_button.setToolTip("Refresh")
        self.refresh_button.setCheckable(False)

        # Add the Home Button
        self.home_button = QPushButton("⌂", self)
        self.home_button.setStatusTip('Go to home page (DuckDuckGo)')
        self.home_button.clicked.connect(self.go_to_home)
        self.navigation_bar.addWidget(self.home_button)
        self.home_button.setFont(QFont('', 20))
        self.home_button.setToolTip("Go Home")
        self.home_button.setCheckable(False)

        # Add the URL Bar
        self.URLBar = QLineEdit()
        self.URLBar.returnPressed.connect(
            lambda: self.go_to_URL(QUrl(self.URLBar.text())))  # What to do when Enter is pressed
        self.navigation_bar.addWidget(self.URLBar)
        self.URLBar.setMaximumWidth(5000)
        self.URLBar.setMinimumWidth(0)

        # Anything added after this widget will be right aligned
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.navigation_bar.addWidget(self.spacer)
        self.spacer.setBaseSize(0, 0)
        self.spacer.setMaximumWidth(300)
        self.spacer.setMinimumWidth(0)

        # Add the Search Bar
        self.SearchBar = QLineEdit()
        self.SearchBar.returnPressed.connect(lambda: self.search(QUrl(self.SearchBar.text())))
        self.navigation_bar.addWidget(self.SearchBar)
        self.SearchBar.setContentsMargins(0, 0, 50, 0)
        self.SearchBar.setMaximumWidth(500)
        self.SearchBar.setText("Search")

        self.show()

    def go_to_home(self):
        self.browser.setUrl(QUrl('https://www.duckduckgo.com/'))

    def go_to_URL(self, url: QUrl):
        if url.scheme() == '':
            url.setScheme('http')
        self.browser.setUrl(url)
        self.update_AddressBar(url)

    def update_AddressBar(self, url):
        self.URLBar.setText(url.toString())
        self.URLBar.setCursorPosition(0)

    def search(self, url: QUrl):
        ducky = "http://www.duckduckgo.com/?q="
        barText = self.SearchBar.text()
        searchAddress = ducky + barText
        self.browser.setUrl(QUrl(searchAddress))
        self.update_AddressBar(QUrl(searchAddress))
        print(searchAddress)
        self.SearchBar.setText("Search")

    @QtCore.pyqtSlot("QWebEngineFullScreenRequest")
    def FullscreenRequest(self, request):
        request.accept()
        if request.toggleOn():
            self.browser.setParent(None)
            self.browser.showFullScreen()
        else:
            self.setCentralWidget(self.browser)
            self.browser.showNormal()


app = QApplication(argv)
app.setApplicationName('Libertatem Browser')

window = Window()

app.exec_()
