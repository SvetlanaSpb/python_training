from new import New


def test_delete_first_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_new()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts



