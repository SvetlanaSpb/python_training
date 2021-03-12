def test_modify_first_new(app):
    app.session.login(password="secret", username="admin")
    app.contact.modify_first_new()
    app.session.logout()

