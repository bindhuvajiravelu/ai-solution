from app.classifier import Classifier

def test_urgent():
    c = Classifier()
    assert c.predict("This is urgent")=="urgent"

def test_bug():
    c = Classifier()
    assert c.predict("There is a bug error") == "bug"

def test_empty():
    c = Classifier()
    assert c.predict("")=="unknown"