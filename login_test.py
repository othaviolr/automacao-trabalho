from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://ststeste.webfopag.com.br/LoginNew.aspx?ReturnUrl=%2f%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fteste.webfopag.com.br%252f%26wctx%3drm%253d1%2526id%253dpassive%2526ru%253d%25252fDefault.aspx%25253fSessionId%25253dxzmlt0hw2p33tuhqdge4evdi%26wct%3d2025-02-25T15%253a15%253a19Z&wa=wsignin1.0&wtrealm=https%3a%2f%2fteste.webfopag.com.br%2f&wctx=rm%3d1%26id%3dpassive%26ru%3d%252fDefault.aspx%253fSessionId%253dxzmlt0hw2p33tuhqdge4evdi&wct=2025-02-25T15%3a15%3a19Z")

        page.get_by_placeholder("Informe seu Centro Serviço").fill("crasa")
        page.get_by_placeholder("Informe seu usuário").fill("11052558917")
        page.get_by_placeholder("Informe sua senha").fill("qwer1234")


        page.get_by_text("Entrar").click()


        page.wait_for_timeout(3000)

        browser.close()

if __name__ == "__main__":
    run()
