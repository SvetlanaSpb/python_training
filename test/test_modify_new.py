from new import New
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = New(surname="Lname", name="Fname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)











