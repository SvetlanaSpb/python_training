# -*- coding: utf-8 -*-
from new import New
import pytest
import random
import string

#делаем генератор тестовых случайных данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [New(firstname="", lastname="", nickname="",title="", company="", address="",homephone="", mobilephone="", workphone="",
                fax="", email="", email2="",email3="", homepage="", address2="",secondaryphone="", notes="")] + [
    New(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname",10),
        title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
        homephone=random_string("9", 10), mobilephone=random_string("98", 10), workphone=random_string("97", 10),
        fax=random_string("96", 10), email=random_string("@", 10), email2=random_string("email", 10),
        email3=random_string("em@mail3.ru", 10), homepage=random_string("www.myhomepage.ru", 10), address2=random_string("address2", 10),
        secondaryphone=random_string("+7", 10), notes=random_string("notes", 10))
    for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=New.id_or_max) == sorted(new_contacts, key=New.id_or_max)




