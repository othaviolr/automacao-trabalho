from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://teste.webfopag.com.br/MenuPrincipal.aspx")
    page.get_by_placeholder("Informe seu Centro Serviço").fill("crasa")
    page.get_by_placeholder("Informe seu usuário").fill("11052558917")
    page.get_by_placeholder("Informe sua senha").fill("qwer1234")
    page.get_by_role("button", name="Entrar").click()

    page.get_by_title("Relatório [Ctrl+4]").click()

    page.click("#ctl00_cphPrincipal_ComponenteLocalizarPlugin_AutoComplete_BotaoBusca")

   # aguarda o campo de pesquisa ficar disponível após abrir a lupa
    campo_pesquisa = page.wait_for_selector("input[name='ctl00$cphPrincipal$ComponenteLocalizarPlugin$ModalBusca$txtBusca']")

# preenche o campo de pesquisa com o nome do relatório
    campo_pesquisa.fill("Relatório de Empregados Ativos")

    page.click(".button_padrao_icone.pesquisar")

    page.get_by_text("Relatório de Empregados Ativos", exact=True).click()

    page.wait_for_timeout(1000)

# pressiona tab para confirmar o preenchimento
    page.locator("input[name*='DataPeriodoInicial']").fill("01/01/2024")
    page.locator("input[name*='DataPeriodoFinal']").click()

    page.wait_for_timeout(1000)

    page.locator("input[name*='DataPeriodoFinal']").fill("31/01/2024")

    page.wait_for_timeout(1000)

    page.get_by_role("button", name="Exportar PDF").click()

    page.wait_for_timeout(5000)
    browser.close()
