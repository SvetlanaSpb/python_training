from new import New

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("home").click()

    def delete_first_new(self):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # fill contact form
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()

    def modify_first_new(self, new):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_forms(new)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def create(self, new):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_forms(new)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

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

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(New(name=text, id=id))
        return contacts



