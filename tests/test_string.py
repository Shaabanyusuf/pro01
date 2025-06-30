from src import  str
import pytest

def test_string_tit():
    assert str.tit("text") == "Text"
    


@pytest.mark.FEB_mark
def test_string_upp():
    assert str.upp("text") == "TEXT"
    
@pytest.mark.MAR_mark 
def test_string_low():
    assert str.low("text") == "text"
    

def test_string_spi():
    assert str.spi("this is a spilt test") == ["this", 'is', 'a', 'spilt', 'test']