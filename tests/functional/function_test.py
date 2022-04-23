def test_index_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200

def test_estimate_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200

def test_result_functionality(app, client):
    print("-- /result 'totalcost' POST test")
    with app.test_client() as test_client:
        cost = {'radius':'200','height':'400'}
        res = test_client.post('/result', data=cost)
        assert res.status_code == 200
