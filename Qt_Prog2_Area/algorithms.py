from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Algorithms:

    def getArea(self, pol : QPolygon):
        #Get area of the polygon by LH formula
        n = len(pol)
        area = 0

        #Process all points
        for i in range(n):
            area += pol[i].x() * (pol[(i+1)%n].y() - pol[(i-1+n)%n].y())

        return 0.5 * abs(area)
