import pytest
from flask import jsonify, Flask

from app.controllers.Slack import Slack, Controller

def setup_module(module) :
    
    global slack
    slack = Slack()

def test_SlackController_initConstructor():

    assert(issubclass(Slack, Controller) == True)
    assert(len(slack.resources) > 0)
    assert(len(slack.apiResources) == len(slack.resources))

def test_SlackApp_initConstructorWithBadResources():
    
    with pytest.raises(ValueError) as e:
        slack = Slack({"name" : "Name"})

def test_listResources():

    expected = [
        {
            "name" : "Intro Service",
            "resource" : "intro",
        },
        {
            "name" : "File Service",
            "resource" : "files",
        }
    ]
    actual = slack.listResources()
    assert(expected == actual)

def test_runResources_withCorrectMethod():

    expected = {"content" : "The cat is fat", "type" : "text"}
    
    actual1 = slack.runResource("intro")
    actual2 = slack.runResource("intro")
    assert(expected == actual1)
    assert(expected == actual2)

def test_runResources_withIncorrectMethod():

    expected = { "message" : "ERROR: NOT FOUND." }
    actual = slack.runResource("notMethod")
    assert(expected == actual)

def test_runResources_returning_an_existing_file():

    expected = {"content" : "app/controllers/temp/tokoyami.png", "type" : "file"}
    actual = slack.runResource("files")
    assert(expected == actual)