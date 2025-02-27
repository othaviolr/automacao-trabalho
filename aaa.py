from playwright.sync_api import sync_playwright

def process_command(page, command):
    command = command.lower()
    
    if "preencha o centro de serviço com" in command:
        value = command.split("com")[-1].strip()
        page.get_by_placeholder("Informe seu Centro Serviço").fill(value)
        print(f"Centro de serviço preenchido com: {value}")

    elif "preencha o usuário com" in command and "senha com" in command:
        parts = command.split("e a senha com")
        usuario = parts[0].split("com")[-1].strip()
        senha = parts[1].strip()
        page.get_by_placeholder("Informe seu usuário").fill(usuario)
        page.get_by_placeholder("Informe sua senha").fill(senha)
        print(f"Usuário: {usuario} e senha preenchidos")

    elif "clique no botão" in command and "entrar" in command:
        page.get_by_text("Entrar").click()
        print("Botão 'Entrar' clicado")

    elif "acessar relatórios" in command:
        page.get_by_title("Relatório [Ctrl+4]").click()
        print("Acessando a tela de relatórios")

    elif "abrir campo de pesquisa" in command:
        page.locator("input[name='ctl00$cphPrincipal$ComponenteLocalizarPlugin$AutoComplete$BotaoBusca']").click()
        print("Campo de pesquisa aberto")

    elif "pesquisar relatório" in command:
        relatorio_nome = command.split("com")[-1].strip()
        campo_pesquisa = page.locator("input[name='ctl00$cphPrincipal$ComponenteLocalizarPlugin$ModalBusca$txtBusca']")
        campo_pesquisa.wait_for(state="visible")
        campo_pesquisa.fill(relatorio_nome)
        campo_pesquisa.press("Enter")
        print(f"Pesquisando pelo relatório: {relatorio_nome}")

    elif "selecionar relatório" in command:
        relatorio_nome = command.split("com")[-1].strip()
        page.wait_for_selector(f"text={relatorio_nome}").click()
        print(f"Relatório selecionado: {relatorio_nome}")

    elif "preencher período inicial com" in command:
        data_inicial = command.split("com")[-1].strip()
        page.locator("input[name*='DataPeriodoInicial']").fill(data_inicial)
        print(f"Período inicial preenchido com: {data_inicial}")

    elif "preencher período final com" in command:
        data_final = command.split("com")[-1].strip()
        campo_data_final = page.locator("input[name*='DataPeriodoFinal']")
        campo_data_final.wait_for(state="visible")  
        campo_data_final.fill(data_final)
        campo_data_final.press("Tab")
        print(f"Período final preenchido com: {data_final}")

    elif "exportar relatório para pdf" in command:
        page.get_by_role("button", name="Exportar PDF").click()
        print("Relatório exportado para PDF")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://teste.webfopag.com.br/MenuPrincipal.aspx")

        print("Digite os comandos (ou 'sair' para finalizar):")
        while True:
            command = input("> ")
            if command.lower() == "sair":
                break
            process_command(page, command)

        browser.close()

if __name__ == "__main__":
    run()

# Preencha o centro de serviço com crasa
# Preencha o usuário com 11052558917 e a senha com qwer1234
# Clique no botão Entrar
# Acessar relatórios
# Abrir campo de pesquisa
# Pesquisar relatório com Relatório de Empregados Ativos
# Selecionar relatório com Relatório de Empregados Ativos
# Preencher período inicial com 01/01/2024
# Preencher período final com 31/01/2024
# Exportar relatório para PDF