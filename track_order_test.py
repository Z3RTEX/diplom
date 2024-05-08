import sender_stand_request


def test_track_order():
    new_order = sender_stand_request.create_order()
    track = new_order.json()["track"]
    res = sender_stand_request.track_order(track)
    assert res.status_code == 200
