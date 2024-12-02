from playwright.sync_api import expect

class Carrinho():
    def __init__(self, page):
        self.page = page
        self.campo_calcular_frete = self.page.locator("#calcularFrete")
        self.botao_calcular_frete = self.page.locator("#btn-frete")
        self.input_cupom = self.page.locator("#usarCupom")
        self.botao_usar_cupom = self.page.locator("#btn-cupom")
        self.botao_finalizar_compra = self.page.locator(".botao.principal.grande")
        self.info_produtos = self.page.locator(".produto-info")
        self.mensagem_cupom = self.page.locator(".alert.alert-danger.alert-geral")

    def calcular_frete(self, cod_cep):
        self.campo_calcular_frete.wait_for(state="visible")
        self.campo_calcular_frete.fill(cod_cep)
        self.botao_calcular_frete.wait_for(state="visible")
        self.botao_calcular_frete.click()

    def adicionar_cupom(self, cupom):
        self.input_cupom.wait_for(state="visible")
        self.input_cupom.fill(cupom)
        self.botao_usar_cupom.click()

    def mensagem_alerta_cupom(self, mensagem):
        self.mensagem_cupom.wait_for(state="visible")
        self.text_alerta = self.mensagem_cupom.get_by_text(mensagem, exact=False)
        self.text_alerta.wait_for(state="visible")
        expect(self.text_alerta).to_be_visible()

    def acessar_checkout(self):
        self.botao_finalizar_compra.wait_for(state="visible")
        self.botao_finalizar_compra.click()
        self.info_produtos.wait_for(state="visible")
        expect(self.info_produtos).to_be_visible()  
