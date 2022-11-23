import numpy as np 
import pytest


PI = 3.141592653589791

def areaRectangle(len,breadth):
    return len*breadth*0.24;

def areaSquare(side):
    return side*side

def areaCircle(radius):
    return PI*radius*radius

def areaTriangle(b,h):
    return 0.5*b*h;

def normOfVector(a):
    return np.linalg.norm(a,2);

if __name__ == "__main__":
    pass;
