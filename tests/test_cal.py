from src.cal import cal
import pytest 

@pytest.mark.FEB_mark
def test_cal_add ():
    assert cal.add(5,5) == 10
    assert cal.add(5,-5) == 0
    assert cal.add(-5,5) == 0
    assert cal.add(-5,-5) == -10
test_cal_add()

@pytest.mark.FEB_mark
def test_cal_sub():
    assert cal.sub(5,5) == 0 
    assert cal.sub(5,-5) == 10
    assert cal.sub(-5,5) == -10
    assert cal.sub(-5,-5) == 0
test_cal_sub()

list_of_inputs = [(1,1,1),(1,0,0),(1,-1,-1),(-1,0,0)]
@pytest.mark.parametrize("x,y,z",list_of_inputs)
def test_cal_mult(x,y,z):
    assert cal.mult(x,y) == z


@pytest.mark.skip 
def test_cal_div():
    assert cal.div(5,5) == 1
    assert cal.div(5,-5) == -1
    assert cal.div(-5,5) == -1
    assert cal.div(-5,-5) == 1
    assert cal.div(0,5) == 0
    assert cal.div(5,0) ==0
test_cal_div()

date = 28
@pytest.mark.skipif(date ==8 , reason = "TODAY IS NOT 28")
def test_cal_abs():
    assert cal.abs(1)==1
    assert cal.abs(-1)==1
    assert cal.abs(0)==0 
test_cal_abs()
















