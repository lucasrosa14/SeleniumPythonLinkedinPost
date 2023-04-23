import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestLinkedinPost:

    def test_linkedinPost(self):
        loginPage = LoginPage()
        homePage = HomePage()

        username = "lucassr91@live.com"
        password = "luro0216"

        postText = "Esse post foi feito através de uma automação de testes da página do Linkedin, " \
                   "utilizando Selenium Webdriver e Python.\n" \
                   "Link para o projeto: \n" \
                   "Obs.: nome de usuário e senha foram suprimidos do código fonte do teste para garantir " \
                   "privacidade.\n" \
                   "Deixe seu like para aumentar o engajamento."

        # login
        loginPage.doLogin(username, password)
        homePage.checkLoginSuccess()

        # start post
        homePage.writePost(postText)

        # Publish post
        homePage.sharePost()

        # View post
