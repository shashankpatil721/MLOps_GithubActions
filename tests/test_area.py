from src.app import *
import pytest



def test_AreaSquare():
    codeResult = areaSquare(5);
    actualResult = 25.0
    val = 'fail'
    if(abs(codeResult - actualResult) < 1e-8 ):
        val = 'pass'
    assert val == 'pass'

def test_AreaCircle():
    codeResult = areaCircle(1);
    actualResult = 3.141592654;
    val = 'fail'
    if(abs(codeResult - actualResult) < 1e-2 ):
        val = 'pass'
    assert val == 'pass'

def test_AreaTriangle():
    codeResult = areaTriangle(1,1);
    actualResult = 0.5;
    val = 'fail'
    if(abs(codeResult - actualResult) < 1e-2 ):
        val = 'pass'
    assert val == 'pass'

def test_Norm():
    codeResult = normOfVector(np.array([1,1]));
    actualResult = np.sqrt(2);
    val = 'fail'
    if(abs(codeResult - actualResult) < 1e-2 ):
        val = 'pass'
    assert val == 'pass'

if __name__ == "__main__":
    test_AreaSquare();
    test_AreaCircle();
    test_AreaTriangle();
    test_Norm();
