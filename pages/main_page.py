from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.about_link = '//a[@class="tn-atom" and contains(text(), "О нас")]'
        self.service_link = '//a[@class="tn-atom" and contains(text(), "Услуги")]'
        self.projects_link = '//a[@class="tn-atom" and contains(text(), "Проекты")]'
        self.reviews_link = '//a[@class="tn-atom" and contains(text(), "Отзывы")]'
        self.contacts_link = '//a[@class="tn-atom" and contains(text(), "Контакты")]'

    def click_about(self):
        self.page.click(self.about_link)

    def click_service(self):
        self.page.click(self.service_link)

    def click_projects(self):
        self.page.click(self.projects_link)

    def click_reviews(self):
        self.page.click(self.reviews_link)

    def click_contacts(self):
        self.page.click(self.contacts_link)