# -*- coding: utf-8 -*-
from new import New


def test_add_new(app):
    app.contact.create(New(surname="Lname", name="Fname"))


def test_add_emptynew(app):
    app.contact.create(New(surname="", name=""))
