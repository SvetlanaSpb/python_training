from new import New


def test_modify_first_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    app.contact.modify_first_new(New(surname="Lname", name="Fname"))









