import sys
import io
import folium # pip3 install folium
#pip3 install PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip3 install PyQtWebEngine

"""
Folium in PyQt5
"""
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Car rental branches')
        self.window_width, self.window_height = 650, 450
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        #Folium map initialization
        coordinate = (13.746556162678786, 100.53081701876293)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=15,
        	location=coordinate
        )

        #Location marker
        folium.Marker(location=[13.746556162678786, 100.53081701876293],popup="Pathumwan branch",icon=folium.Icon(icon="cloud"),).add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')