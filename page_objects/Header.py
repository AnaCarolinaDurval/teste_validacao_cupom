from playwright.sync_api import expect

class Header:
    def __init__ (self,page):
        self.page = page
        self.header_busca_produto = self.page.locator("#Caminho_102")
        self.input_pesquisa_produto = self.page.locator(".ui-autocomplete-input")
        self.button_buscar_produto = self.page.locator('[aria-label = "Buscar"]')
        self.listagem_produto = self.page.locator(".info-produto a")

    def buscar_produto(self, cod_produto):
        self.header_busca_produto.click()
        self.input_pesquisa_produto.fill(cod_produto)
        self.button_buscar_produto.wait_for(state="visible")
        self.button_buscar_produto.click()

    def acessar_pagina_do_produto(self):
        self.listagem_produto.wait_for(state="visible")
        self.listagem_produto.click()
