import allure
from selene import by, be
from selene.support.shared import browser
# команда по запуску allure отчета - allure serve test_github/allure-results


def test_find_issues_selene():
    browser.open("https://github.com")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type("qa_guru_python_allure").press_enter()
    browser.element(by.link_text("surovp/qa_guru_python_Allure_8")).click()
    browser.element("#issues-tab").should(be.visible)


def test_find_issues_steps():

    with allure.step("Открываем github"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").type("qa_guru_python_allure").press_enter()
        browser.element(by.link_text("surovp/qa_guru_python_Allure_8")).click()

    with allure.step("Находим раздел issues"):
        browser.element("#issues-tab").should(be.visible)



