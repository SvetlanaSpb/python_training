# -*- coding: utf-8 -*-
from new import New
from sys import maxsize

def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    contact = New(surname="Lname", name="Fname")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max)


#def test_add_emptynew(app):
#    old_contacts = app.contact.get_contact_list()
 #   contact = New(surname="", name="")
  #  app.contact.create(contact)
   # new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
