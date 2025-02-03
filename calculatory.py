#!python
#importujemy elementy do stworzenia klasy głownej i okna apki
from PyQt5.QtWidgets import QApplication, QWidget

#importujemy widżety (etykiety i uklad siatke rozmieszczneia)
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtGui import QIcon

#tworzymy klase kalkulatora jako parametr wybieramy Qwidgets klase wszystkich elementow interfejsu 
class calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.interface()

    def interface(self):
        #ustawienie wielkości okna jego opisu o włączenie wy\swietlania na ekranie
        self.resize(500, 400)
        self.setWindowTitle('Kalkulator')
        
        #dodanie etykiet wrazz opisami
        label1 = QLabel("Liczba 1:", self)
        label2 = QLabel("Liczba 2:", self)
        label3 = QLabel("Wynik:", self)

        #rozmieszczenie w poziomie i 
        # przypisanie etykiet do ukladu tabelarycznego
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)

        #przypisanie ukladu tabelarycznego do okna
        self.setLayout(layout)


        #właczenie widocznosci okna
        self.show()

if __name__ == "__main__":
    import sys
    #Aby uruchomić program, tworzymy obiekt reprezentujący aplikację
    app = QApplication(sys.argv)
    #tworzyymy obiekt reprezentujący okno aplikacji czyli instancje klasy calculator
    window = calculator()
    sys.exit(app.exec_())




        
        