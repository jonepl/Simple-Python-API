import os, pytest

from flask import Flask
from app.routes import router
try:
    from config.creds import api_keys
except(AttributeError, ModuleNotFoundError) as e:
    api_keys = os.environ["api_keys"]

def setup_module(module) :
    
    global api_key
    api_key = api_keys[0] or os.environ["api_keys"]

@pytest.fixture(scope='module')
def client():
    app = Flask(__name__)
    client = app.test_client()
    router.configure_routes(app)
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()

def test_home_route(client):
    response = client.get('/') 

    expectedBody = bytes('<h1>My API</h1><p>Home page</p>', 'utf-8')
    expectedStatusCode = 200
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)

def test_authorized_api_route(client):
    response = client.get('/api', headers={"x-api-key" : api_key}) 

    expectedBody = bytes('<h1>My API</h1><p>Success Api Page</p>', 'utf-8')
    expectedStatusCode = 200
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == response.status_code)

def test_unauthorized_api_route(client):
    response = client.get('/api', headers={"x-api-key" : "Bad-key"}) 

    expectedBody = bytes('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>401 Unauthorized</title>\n<h1>Unauthorized</h1>\n<p>The server could not verify that you are authorized to access the URL requested.  You either supplied the wrong credentials (e.g. a bad password), or your browser doesn\'t understand how to supply the credentials required.</p>\n', 'utf-8')
    expectedStatusCode = 401
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)


def test_slackRoutes_authorized_slackCollection(client):
    
    response = client.get('/api/slack', headers={"x-api-key" : api_key})
    
    expectedBody = bytes('[{"name":"Intro Service","resource":"intro"},{"name":"File Service","resource":"files"}]\n', "utf-8")
    expectedStatusCode = 200
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)

def test_slackRoutes_unauthorized_slackCollection(client):

    response = client.get('/api/slack', headers={"x-api-key" : "Bad-key"})
    
    expectedBody = bytes('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>401 Unauthorized</title>\n<h1>Unauthorized</h1>\n<p>The server could not verify that you are authorized to access the URL requested.  You either supplied the wrong credentials (e.g. a bad password), or your browser doesn\'t understand how to supply the credentials required.</p>\n', 'utf-8')
    expectedStatusCode = 401
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)

def test_slackRoutes_authorized_slackResource(client):

    response = client.get('/api/slack/intro', headers={"x-api-key" : api_key})
    
    expectedBody = bytes('{"content":"The cat is fat","type":"text"}\n', "utf-8")
    expectedStatusCode = 200
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)

def test_slackRoutes_authorized_slackResource_bad_resource(client):
    
    response = client.get('/api/slack/badResourceName', headers={"x-api-key" : api_key})
    
    expectedBody = bytes('{"message":"ERROR: NOT FOUND."}\n', 'utf-8')
    expectedStatusCode = 404
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)    

def test_slackRoutes_unauthorized_slackResource(client):
    
    response = client.get('/api/slack/intro', headers={"x-api-key" : "Bad-key"})
    
    expectedBody = bytes('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>401 Unauthorized</title>\n<h1>Unauthorized</h1>\n<p>The server could not verify that you are authorized to access the URL requested.  You either supplied the wrong credentials (e.g. a bad password), or your browser doesn\'t understand how to supply the credentials required.</p>\n', 'utf-8')
    expectedStatusCode = 401
    actualBody = response.get_data()
    actualStatusCode = response.status_code

    assert(expectedBody == actualBody)
    assert(expectedStatusCode == actualStatusCode)    