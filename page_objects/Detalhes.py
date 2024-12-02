
from playwright.sync_api import expect

class Detalhes():

    def __init__(self, page):
        self.page = page
        self.botao_comprar_detalhes = self.page.locator('.comprar a[class="botao botao-comprar principal grande "]')
        self.titulo_produto = self.page.locator(".nome-produto.titulo.cor-secundaria")

    def detalhes_botao_comprar(self):
        self.titulo_produto.wait_for(state="visible")
        expect(self.titulo_produto).to_be_visible()
        self.botao_comprar_detalhes.wait_for(state="visible")
        self.botao_comprar_detalhes.click()

