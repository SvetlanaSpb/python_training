from new import New
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(New(firstname="Svetlana", middlename="Alexeyevna", lastname="Andreeva", nickname="Sveta",
                      title="test", company="2B", address="Saint-Petersburg", homephone="+78120000000",
                      mobilephone="+79110000000", workphone="+78121000000", fax="+78122000000",
                      email="sve@mail.ru", email2="sve2@mail.ru", email3="sve3@mail.ru",
                      homepage="www.andreeva.ru", bday="19", bmonth="September", byear="1987", aday="9", amonth="May",
                      ayear="2000", address2="Moscow", secondaryphone="1", notes="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = New(firstname="Svetlana", middlename="Alexeyevna", lastname="Andreeva", nickname="Sveta",
                      title="test", company="2B", address="Saint-Petersburg", homephone="+78120000000",
                      mobilephone="+79110000000", workphone="+78121000000", fax="+78122000000",
                      email="sve@mail.ru", email2="sve2@mail.ru", email3="sve3@mail.ru",
                      homepage="www.andreeva.ru", bday="19", bmonth="September", byear="1987", aday="9", amonth="May",
                      ayear="2000", address2="Moscow", secondaryphone="1", notes="Test")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)











