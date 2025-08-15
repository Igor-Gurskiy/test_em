import allure
import pytest
from pages.main_page import MainPage
from pages.services_page import ServicesPage
from pages.projects_page import ProjectsPage
from pages.reviews_page import ReviewsPage
from pages.contacts_page import ContactsPage
from pages.about_page import AboutPage

@allure.feature("Main page navigation")
class TestMainPageNavigation:
    @allure.story("Navigation to About page")
    def test_navigate_to_about_page(self, page):
        main_page = MainPage(page)
        main_page.navigate("https://effective-mobile.ru/")
        main_page.click_about()
        about_page = AboutPage(page)
        assert about_page.get_current_url() == "https://effective-mobile.ru/#about"

    @allure.story("Navigation to Services page")
    def test_navigate_to_services_page(self, page):
        main_page = MainPage(page)
        main_page.navigate("https://effective-mobile.ru/")
        main_page.click_service()
        services_page = ServicesPage(page)
        assert services_page.get_current_url() == "https://effective-mobile.ru/#moreinfo"

    @allure.story("Navigation to Projects page")
    def test_navigate_to_projects_page(self, page):
        main_page = MainPage(page)
        main_page.navigate("https://effective-mobile.ru/")
        main_page.click_projects()
        projects_page = ProjectsPage(page)
        assert projects_page.get_current_url() == "https://effective-mobile.ru/#cases"

    @allure.story("Navigation to Reviews page")
    def test_navigate_to_reviews_page(self, page):
        main_page = MainPage(page)
        main_page.navigate("https://effective-mobile.ru/")
        main_page.click_reviews()
        reviews_page = ReviewsPage(page)
        assert reviews_page.get_current_url() == "https://effective-mobile.ru/#Reviews"

    @allure.story("Navigation to Contacts page")
    def test_navigate_to_contacts_page(self, page):
        main_page = MainPage(page)
        main_page.navigate("https://effective-mobile.ru/")
        main_page.click_contacts()
        contacts_page = ContactsPage(page)
        assert contacts_page.get_current_url() == "https://effective-mobile.ru/#contacts"