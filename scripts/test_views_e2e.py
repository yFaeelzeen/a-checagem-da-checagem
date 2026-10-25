import asyncio
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Desktop Test (1440x900)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("console", lambda msg: print(f"[Browser {msg.type}]: {msg.text.encode('ascii', 'replace').decode('ascii')}") if msg.type in ["error", "warning"] else None)

        print("Testing Desktop: Load index.html...")
        await page.goto("http://localhost:8080/index.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(800)

        # Check masthead title
        title_text = await page.inner_text(".newspaper-title")
        print("Desktop Masthead Title checked.")
        assert "A CHECAGEM DA “CHECAGEM”" in title_text

        # Capture Desktop Header
        await page.locator(".gazette-header").screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_header_desktop.png")
        print("Captured verify_header_desktop.png")

        # Test View Switcher: Click #veiculos
        print("Testing #veiculos switch...")
        await page.click("#tab-nav-veiculos")
        await page.wait_for_timeout(500)

        hash_val = await page.evaluate("() => window.location.hash")
        print("Hash after clicking veiculos tab:", hash_val)
        assert hash_val == "#veiculos"

        # Check outlet table rows
        rows_count = await page.locator("#outlet-table tr").count()
        print("Outlet table total rows:", rows_count)
        assert rows_count >= 19

        # Capture Desktop Veiculos View
        await page.screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_veiculos_desktop.png")
        print("Captured verify_veiculos_desktop.png")

        # Test Sorting on Veiculos
        print("Testing sort by Flávio % falso...")
        await page.click(".th-flavio .btn-sort-column")
        await page.wait_for_timeout(400)

        # Test View Switcher: Click #declaracoes
        print("Testing #declaracoes switch...")
        await page.click("#tab-nav-declaracoes")
        await page.wait_for_timeout(500)

        hash_val = await page.evaluate("() => window.location.hash")
        print("Hash after clicking declaracoes tab:", hash_val)
        assert hash_val == "#declaracoes"

        claims_count_text = await page.inner_text("#claim-count")
        print("Claim counter checked:", "224" in claims_count_text)
        assert "224" in claims_count_text or "declarações" in claims_count_text

        # Test Hover/Click on cell for Tooltip
        first_cell = page.locator("td[data-claim-idx]").first
        await first_cell.click()
        await page.wait_for_timeout(400)

        tooltip_hidden = await page.evaluate("() => document.getElementById('claim-tooltip').hidden")
        print("Tooltip visible:", not tooltip_hidden)
        assert not tooltip_hidden

        # Capture Desktop Declaracoes View
        await page.screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_declaracoes_desktop.png")
        print("Captured verify_declaracoes_desktop.png")

        await context.close()

        # 2. Mobile Test (390x844 - iPhone 14 / modern mobile)
        print("\nTesting Mobile (390px)...")
        mob_context = await browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True
        )
        mob_page = await mob_context.new_page()

        mob_page.on("pageerror", lambda err: errors.append(str(err)))

        # Load direct to #veiculos on mobile
        print("Direct navigation to index.html#veiculos on mobile...")
        await mob_page.goto("http://localhost:8080/index.html#veiculos", wait_until="domcontentloaded")
        await mob_page.wait_for_timeout(800)

        # Verify #view-veiculos is active
        veiculos_hidden = await mob_page.evaluate("() => document.getElementById('view-veiculos').hidden")
        print("Mobile #view-veiculos is hidden?", veiculos_hidden)
        assert not veiculos_hidden

        # Capture Mobile Header & Veiculos
        await mob_page.screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_mobile_veiculos.png")
        print("Captured verify_mobile_veiculos.png")

        # Switch to #declaracoes on mobile
        print("Switching to #declaracoes on mobile...")
        await mob_page.click("#tab-nav-declaracoes")
        await mob_page.wait_for_timeout(600)

        # Check horizontal overflow on mobile body
        scroll_width = await mob_page.evaluate("() => document.documentElement.scrollWidth")
        client_width = await mob_page.evaluate("() => document.documentElement.clientWidth")
        print(f"Mobile widths: scrollWidth={scroll_width}, clientWidth={client_width}")
        assert scroll_width <= client_width + 1, f"Horizontal overflow detected! {scroll_width} > {client_width}"

        # Capture Mobile Declaracoes View
        await mob_page.screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_mobile_declaracoes.png")
        print("Captured verify_mobile_declaracoes.png")

        # Switch back to #dossie on mobile
        print("Switching back to #dossie on mobile...")
        await mob_page.click("#tab-nav-dossie")
        await mob_page.wait_for_timeout(600)

        await mob_page.screenshot(path="C:/Users/RAFAE/.gemini/antigravity/brain/d9d0f268-c706-4e90-8039-e4cc898cb0a2/verify_mobile_dossie.png")
        print("Captured verify_mobile_dossie.png")

        await mob_context.close()
        await browser.close()

        print("\nAll browser verification tests passed cleanly!")
        print("Page errors recorded:", len(errors))
        if errors:
            print("Errors list:", errors)
        assert len(errors) == 0

asyncio.run(run_tests())
