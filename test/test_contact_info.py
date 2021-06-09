from new import New
from random import randrange
import re


def test_contact_info_on_main_page(app):
    if app.contact.count() == 0:
        app.contact.add_contact(
            New(firstname="Svetlana", middlename="Alexeyevna", lastname="Andreeva", nickname="Sveta",
                      title="test", company="2B", address="Saint-Petersburg", homephone="+78120000000",
                       workphone="+78121000000", mobilephone="+79110000000",secondaryphone="1",fax="+78122000000",
                      email="sve@mail.ru", email2="sve2@mail.ru", email3="sve3@mail.ru",
                      homepage="www.andreeva.ru", bday="19", bmonth="September", byear="1987", aday="9", amonth="May",
                      ayear="2000", address2="Moscow", notes="Test"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone,contact.secondaryphone]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))