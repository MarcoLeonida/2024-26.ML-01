from sanviti import libreria_esercizi
import pytest

def test_E1_Triangoli_classifier():
    assert libreria_esercizi.E1_Triangoli_classifier([7, 7, 10]) == 'ISOSCELE'
    assert libreria_esercizi.E1_Triangoli_classifier([10, 10, 100]) == 'N/A'
    assert libreria_esercizi.E1_Triangoli_classifier([7, 2, 10]) == 'N/A'
    assert libreria_esercizi.E1_Triangoli_classifier([15, 7, 10]) == 'SCALENO'
    assert libreria_esercizi.E1_Triangoli_classifier([7, 7, 10]) == 'ISOSCELE'
    assert libreria_esercizi.E1_Triangoli_classifier([7, 7, 7]) == 'EQUILATERO'

def test_E1_Triangoli_area():
    assert libreria_esercizi.E1_Triangoli_area([7, 7, 10]) == 24.49
    # TODO assert su presenza di 'math domain error'
    with pytest.raises(ValueError, match=r"math domain error"):
        assert libreria_esercizi.E1_Triangoli_area([10, 10, 100])
    with pytest.raises(ValueError, match=r"math domain error"):
        assert libreria_esercizi.E1_Triangoli_area([7, 2, 10])
    assert libreria_esercizi.E1_Triangoli_area([15, 7, 10]) == 29.39
    assert libreria_esercizi.E1_Triangoli_area([7, 7, 10]) == 24.49
    assert libreria_esercizi.E1_Triangoli_area([7, 7, 7]) == 21.22

def test_E1_Triangoli_perimetro():
    assert libreria_esercizi.E1_Triangoli_perimetro([7, 7, 10]) == 24
    assert libreria_esercizi.E1_Triangoli_perimetro([10, 10, 100]) == 120
    assert libreria_esercizi.E1_Triangoli_perimetro([7, 2, 10]) == 19
    assert libreria_esercizi.E1_Triangoli_perimetro([15, 7, 10]) == 32
    assert libreria_esercizi.E1_Triangoli_perimetro([7, 7, 10]) == 24
    assert libreria_esercizi.E1_Triangoli_perimetro([7, 7, 7]) == 21
