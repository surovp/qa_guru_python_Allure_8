from steps_for_github.steps_for_finding_issues import open_page, \
    search_repositories,\
    click_for_repositories,\
    finding_issues


def test_with_decorators():
    open_page()
    search_repositories("surovp/qa_guru_python_Allure_8")
    click_for_repositories("surovp/qa_guru_python_Allure_8")
    finding_issues()

