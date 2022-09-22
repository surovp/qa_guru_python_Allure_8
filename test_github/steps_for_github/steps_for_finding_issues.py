import allure
from selene import by, be
from selene.support.shared import browser


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
