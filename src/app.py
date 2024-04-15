import numpy as np
import pytest


PI = 3.14159265358979323846


def areaRectangle(len,breadth):
    return len*breadth;

def areaSquare(side):
    return side*side

def areaCircle(radius):
    return PI*radius*radius

def areaTriangle(b,h):
    return 0.5*b*h;

def normOfVector(a):
    return np.linalg.norm(a,2);

print("hello world")

if __name__ == "__main__":
    pass;
