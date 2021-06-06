import re

def test_phones_on_home_page(app):
#фикстура инициализирует объект типа апликейшен, где есть ссылка на контактхелпер
    contact_from_home_page = app.contact.get_contact_list()[0]
#получаем инфо о контакте из формы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#теперь сравниваем полученные выше 2 объекта
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone