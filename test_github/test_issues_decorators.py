import allure
from selene import by, be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "pavels")
@allure.feature("Задачи")
@allure.story("Пользователь может найти конкретный репозиторий")
@allure.link("https://github.com", name="Test")
def test_with_decorators():
    open_page()
    search_repositories("surovp/qa_guru_python_Allure_8")
    click_for_repositories("surovp/qa_guru_python_Allure_8")
    finding_issues()


@allure.step("Открываем github")
def open_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_repositories(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type(repo).press_enter()


@allure.step("Переходим в репозиторий {repo}")
def click_for_repositories(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Находим раздел issues")
def finding_issues():
    browser.element("#issues-tab").should(be.visible)
