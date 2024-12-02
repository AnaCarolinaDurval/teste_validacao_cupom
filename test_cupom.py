import pytest
import playwright
from playwright.sync_api import Page, expect
from confteste import setup_test
from page_objects import Header, Detalhes, Carrinho, Login, Checkout

def teste_aplicar_cupom_valido(page: Page, setup_test):
    page = setup_test
    page.goto("const_url")
    page_objects_header = Header.Header(page)
    page_objects_detalhes = Detalhes.Detalhes(page)
    page_objects_carrinho = Carrinho.Carrinho(page)
    page_objects_login = Login.Login(page)
    page_objects_checkout = Checkout.Checkout(page)

    page_objects_header.buscar_produto("CATEGORIA6")
    page_objects_header.acessar_pagina_do_produto()
    page_objects_detalhes.detalhes_botao_comprar()
    page_objects_carrinho.calcular_frete("16013422")
    page_objects_carrinho.adicionar_cupom("30REAIS")
    page_objects_carrinho.acessar_checkout()
    page_objects_login.adicionar_email("anacarolinadurval1+lojaintegrada@gmail.com")
    page_objects_checkout.selecionar_frete()
    page_objects_checkout.cupom_checkout("30REAIS")
    page_objects_checkout.calcular_valores_checkout()

    print(page_objects_checkout.valor_total, page_objects_checkout.valor_esperado)   
    assert abs(page_objects_checkout.valor_total - page_objects_checkout.valor_esperado) < 0.01, \
    f"Erro: O valor do total calculado ({page_objects_checkout.valor_esperado}) não corresponde ao valor encontrado ({page_objects_checkout.valor_total})"  

def teste_cupom_inesistente(page: Page, setup_test):
    page = setup_test
    page.goto("const_url")
    page_objects_header = Header.Header(page)
    page_objects_detalhes = Detalhes.Detalhes(page)
    page_objects_carrinho = Carrinho.Carrinho(page)  

    page_objects_header.buscar_produto("CATEGORIA6")
    page_objects_header.acessar_pagina_do_produto()
    page_objects_detalhes.detalhes_botao_comprar()
    page_objects_carrinho.calcular_frete("16013422")
    page_objects_carrinho.adicionar_cupom("20LIMITADO")
    page.on("domcontentloaded", page_objects_carrinho.mensagem_alerta_cupom("Cupom não encontrado.")) #identifiquei que logo após o clique no butom do cupom a página realiza um load, por isso aguardo o load ocorrer para identificar o elemento

def teste_cupom_vencido(page: Page, setup_test):
    page = setup_test
    page.goto("const_url")
    page_objects_header = Header.Header(page)
    page_objects_detalhes = Detalhes.Detalhes(page)
    page_objects_carrinho = Carrinho.Carrinho(page)  

    page_objects_header.buscar_produto("CATEGORIA6")
    page_objects_header.acessar_pagina_do_produto()
    page_objects_detalhes.detalhes_botao_comprar()
    page_objects_carrinho.calcular_frete("16013422")
    page_objects_carrinho.adicionar_cupom("CUPOMVENCIDO")
    page.on("domcontentloaded", page_objects_carrinho.mensagem_alerta_cupom("O cupom não é válido."))




