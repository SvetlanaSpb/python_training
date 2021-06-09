# -*- coding: utf-8 -*-
from new import New


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    contact = New(firstname="Svetlana", middlename="Alexeyevna", lastname="Andreeva", nickname="Sveta",
                      title="test", company="2B", address="Saint-Petersburg", homephone="+78120000000",
                      mobilephone="+79110000000", workphone="+78121000000", fax="+78122000000",
                      email="sve@mail.ru", email2="sve2@mail.ru", email3="sve3@mail.ru",
                      homepage="www.andreeva.ru", bday="19", bmonth="September", byear="1987", aday="9", amonth="May",
                      ayear="2000", address2="Moscow", secondaryphone="1", notes="Test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)



#def test_add_emptynew(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = New(surname="", name="")
    #app.contact.create(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)
