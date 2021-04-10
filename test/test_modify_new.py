from new import New


def test_modify_first_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_new(New(surname="Lname", name="Fname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)











