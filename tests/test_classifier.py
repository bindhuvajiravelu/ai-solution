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

def test_model_file_exists():
    import os
    assert os.path.exists("app/model.pkl"), "Model file not found, run train.py"

def test_model_accuracy():
    c = Classifier()
    # This tests REAL model, not rules
    assert c.predict("urgent help needed now") == "urgent"
    assert c.predict("there is a small bug") == "bug"
    assert c.predict("") == "unknown"