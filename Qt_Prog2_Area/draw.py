from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.polyg =  QPolygonF()

    def mousePressEvent(self, e):
        #Get coordinates
        x = e.position().x()
        y = e.position().y()

        #Create new point
        p = QPointF(x, y)

        #Add to polygon
        self.polyg.append(p)

        #Repaint screen
        self.repaint()

    def getPolygon(self):
        #Get polygon
        return self.polyg


    def paintEvent(self, e):

        #New object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set color
        qp.setPen(Qt.GlobalColor.red)

        #Draw polygon
        qp.drawPolygon(self.polyg)

        #Stop draw
        qp.end()

    def clear(self):
        self.polyg.clear()