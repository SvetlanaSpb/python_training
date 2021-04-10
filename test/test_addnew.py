# -*- coding: utf-8 -*-
from new import New


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(New(surname="Lname", name="Fname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



def test_add_emptynew(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(New(surname="", name=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
