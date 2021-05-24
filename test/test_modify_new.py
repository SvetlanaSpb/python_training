from new import New


def test_modify_first_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = New(surname="Lname", name="Fname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)












