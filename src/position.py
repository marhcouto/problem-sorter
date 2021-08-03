#import tkinter as tk
from tkinter import CENTER, NE, N, NW, SE, S, SW, W, E


class Position:

    MODE_RELATIVE = "relative"
    MODE_ABSOLUTE = "absolute"

    def __init__(self, x, y, mode, anchor):
        self.mode = mode
        self.anchor = anchor
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, newX):
        if self.mode == Position.MODE_RELATIVE:
            self.__x = newX if newX < 1.0 and newX > 0.0 else 0.5
        else: 
            self.__x = newX

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, newY):
        if self.mode == Position.MODE_RELATIVE:
            self.__y = newY if newY < 1.0 and newY > 0.0 else 0.5
        else: 
            self.__y = newY

    @property
    def mode(self):
        return self.__mode
    
    @mode.setter
    def mode(self, newMode):
        self.__mode = newMode if newMode == Position.MODE_RELATIVE or newMode == Position.MODE_ABSOLUTE else Position.MODE_RELATIVE

    @property
    def anchor(self):
        return self.__anchor
    
    @anchor.setter
    def anchor(self, newAnchor):
        self.__anchor = newAnchor if newAnchor in [CENTER, NE, SE, NW, SW, S, N, E, W] else CENTER
