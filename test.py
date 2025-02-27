from playwright.sync_api import sync_playwright

def process_command(page, command):
    if "Preencha o centro de serviço com" in command:
        value = command.split("com")[-1].strip()
        page.get_by_placeholder("Informe seu Centro Serviço").fill(value)
    elif "Preencha o usuário com" in command and "e a senha com" in command:
        user, password = command.split("e a senha com")
        user = user.split("com")[-1].strip()
        password = password.strip()
        page.get_by_placeholder("Informe seu usuário").fill(user)
        page.get_by_placeholder("Informe sua senha").fill(password)
    elif "Clique no botão Entrar" in command:
        page.get_by_role("button", name="Entrar").click()
    elif "Acesse a página de relatórios" in command:
        page.get_by_title("Relatório [Ctrl+4]").click()
    elif "Pesquise pelo relatório" in command:
        report_name = command.split("por")[-1].strip()
        page.click("#ctl00_cphPrincipal_ComponenteLocalizarPlugin_AutoComplete_BotaoBusca")
        campo_pesquisa = page.wait_for_selector("input[name='ctl00$cphPrincipal$ComponenteLocalizarPlugin$ModalBusca$txtBusca']")
        campo_pesquisa.fill(report_name)
        page.click(".button_padrao_icone.pesquisar")
        page.get_by_text(report_name, exact=True).click()
    elif "Preencha a data inicial com" in command:
        date = command.split("com")[-1].strip()
        page.locator("input[name*='DataPeriodoInicial']").fill(date)
    elif "Preencha a data final com" in command:
        date = command.split("com")[-1].strip()
        page.locator("input[name*='DataPeriodoFinal']").fill(date)
    elif "Exporte o relatório para PDF" in command:
        page.get_by_role("button", name="Exportar PDF").click()
    else:
        print("Comando não reconhecido")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://teste.webfopag.com.br/MenuPrincipal.aspx")
        
        while True:
            command = input("Digite um comando: ")
            if command.lower() == "sair":
                break
            process_command(page, command)

        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    run()
