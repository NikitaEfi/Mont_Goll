from app import app

client = app.test_client()

def test_keep_about_33():
    at = 100_000
    r = client.post("/play/", json={"choose_option": "keep", "attempts": at})
    data = r.get_json()
    assert data["wins"] + data["loose"] == at
    rate = data["wins"] / at
    assert 0.31 <= rate <= 0.35

def test_change_about_66():
    at = 100_000
    r = client.post("/play/", json={"choose_option": "change", "attempts": at})
    data = r.get_json()
    assert data["wins"] + data["loose"] == at
    rate = data["wins"] / at
    assert 0.65 <= rate <= 0.69
