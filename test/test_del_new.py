from new import New
from random import randrange


def test_delete_some_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(firstname="Svetlana", middlename="Alexeyevna", lastname="Andreeva", nickname="Sveta",
                      title="test", company="2B", address="Saint-Petersburg", homephone="+78120000000",
                      mobilephone="+79110000000", workphone="+78121000000", fax="+78122000000",
                      email="sve@mail.ru", email2="sve2@mail.ru", email3="sve3@mail.ru",
                      homepage="www.andreeva.ru", bday="19", bmonth="September", byear="1987", aday="9", amonth="May",
                      ayear="2000", address2="Moscow", secondaryphone="1", notes="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange (len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts






