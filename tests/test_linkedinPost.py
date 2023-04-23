import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestLinkedinPost:

    def test_linkedinPost(self):
        loginPage = LoginPage()
        homePage = HomePage()

        username = "insira o email aqui"
        password = "insira a senha aqui"

        postText = "Esse post foi feito através de uma automação de testes da página do Linkedin, " \
                   "utilizando Selenium Webdriver e Python.\n" \
                   "Link para o projeto: https://github.com/lucasrosa14/SeleniumPythonLinkedinPost \n" \
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
