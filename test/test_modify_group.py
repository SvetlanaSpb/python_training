def test_modify_first_group(app):
    app.session.login(password="secret", username="admin")
    app.group.modify_first_group()
    app.session.logout()