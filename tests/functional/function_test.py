def test_index_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_route(app, client):
    with app.testclient as test_client:
        res= test_client.get('/about')
        assert res.status_code == 200

def test_estimate_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200

