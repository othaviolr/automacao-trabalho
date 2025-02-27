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
