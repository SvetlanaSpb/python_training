from new import New


def test_delete_first_new(app):
    if app.contact.count() == 0:
        app.contact.create(New(surname="test", name="test"))
    app.contact.delete_first_new()




