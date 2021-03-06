# -*- coding: utf-8 -*-
import pytest
from new import New
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new(app):
    app.login(password="secret", username="admin")
    app.create_group(New(Surname="Lname", name="Fname"))
    app.logout()

def test_add_emptynew(app):
    app.login(password="secret", username="admin")
    app.create_group(New(Surname="", name=""))
    app.logout()





    

    


