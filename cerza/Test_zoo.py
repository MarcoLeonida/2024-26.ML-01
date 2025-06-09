import pytest as pt

#scrivere "pytest" in cmd
class zoo():
    def tiger():
        return "Wasaaaaa"
    def cow():
        return "Mooooooooo"
    def hippopotamus():
        return "Moto moto"
        

def test_savana():
    assert zoo.tiger=="Roaaaarrrr"
    assert zoo.cow=="Moooooooo"
    assert zoo.hippopotamus=="Moto moto"