# -*- coding: utf-8 -*-
import pytest
from model.new import New
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new(app):
    app.session.login(password="secret", username="admin")
    app.create_group(New(Surname="Lname", name="Fname"))
    app.session.logout()

def test_add_emptynew(app):
    app.session.login(password="secret", username="admin")
    app.create_group(New(Surname="", name=""))
    app.session.logout()





    

    


