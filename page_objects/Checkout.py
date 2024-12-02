from playwright.sync_api import expect
import re

class Checkout():
    def __init__(self, page):
        self.page = page
        self.opcao_frete = self.page.locator("#envio12015-retirar_pessoalmente label input[id='formaEnvio12015-retirar_pessoalmente']")
        self.cupom_aplicado = self.page.locator(".cupom-codigo")
        self.subtotal = self.page.locator(".subtotal .titulo.cor-principal")
        self.cupom = self.page.locator("#cupomResultado .titulo.cor-principal")
        self.total = self.page.locator(".total .titulo.cor-principal")
    
    def selecionar_frete(self):
        self.opcao_frete.wait_for(state="visible")
        self.opcao_frete.click()

    def cupom_checkout(self, cupom):
        self.cupom_aplicado.wait_for(state="visible")
        expect(self.cupom_aplicado).to_contain_text(cupom)

    def calcular_valores_checkout(self):
        text_subtotal = self.subtotal.inner_text()
        self.valor_subtotal = float(re.sub(r'[^\d.-]', '', text_subtotal))   
        print(text_subtotal)
        text_cupom = self.cupom.inner_text()
        print(text_cupom)
        self.valor_cupom = float(re.sub(r'[^\d.-]', '', text_cupom)) 

        self.valor_esperado =  self.valor_subtotal - self.valor_cupom  

        text_total = self.total.inner_text()
        self.valor_total = float(re.sub(r'[^\d.-]', '', text_total))    
    