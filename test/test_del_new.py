
def test_delete_first_new(app):
    app.session.login(password="secret", username="admin")
    app.contact.delete_first_new()
    app.session.logout()