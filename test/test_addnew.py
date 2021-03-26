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
    app.contact.create(New(surname="Lname", name="Fname"))



def test_add_emptynew(app):
    app.contact.create(New(surname="", name=""))
