from playwright.sync_api import expect

class Login:
    def __init__ (self,page):
        self.page = page
        self.input_email_login = self.page.locator("#id_email_login")
        self.botao_continuar_login = self.page.locator('.submit-email.botao.principal.grande')

    def adicionar_email(self, email):
        self.input_email_login.wait_for(state="visible")
        self.input_email_login.fill(email)
        self.botao_continuar_login.click()