
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("home").click()

    def delete_first_new(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        assert isinstance(wd, object)
        wd.switch_to_alert().accept()

    def modify_first_new(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("Edit name")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()


    def create(self, new):
        wd = self.app.wd
        self.open_home_page()
        # fill new form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new.Surname)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()