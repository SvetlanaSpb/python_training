from new import New

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("home").click()

    def delete_first_new(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact deletion
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # fill contact form
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_new(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def modify_first_new(self):
        # один метод реализуется через другой
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index,new):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_forms(new)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def create(self, new):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_forms(new)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_forms(self, new):
        wd = self.app.wd
        # fill new form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new.surname)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.get("http://localhost/addressbook/")


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
        # строим объект с информацией о контакте contacts = []
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
            # получаем данные из ячеек
                name = cells[2].text
                surname = cells[1].text
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            # параметры для конструирования нового объекта contacts
                self.contact_cache.append(New(id=contact_id, surname=surname, name=name))
        return list(self.contact_cache)










