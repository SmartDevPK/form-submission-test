# test_form.py
from playwright.sync_api import sync_playwright
import time
import os

def test_local_form():
    """Test your local form.html"""
    print("\n" + "="*50)
    print("TESTING LOCAL FORM")
    print("="*50)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        html_path = os.path.abspath("form.html")
        file_url = f"file://{html_path}"
        
        page.goto(file_url)
        time.sleep(1)
        
        page.fill("#name", "Michael Emmanuel")
        page.fill("#email", "emmanuelmichaelpk3@gmail.com")
        page.fill("#phone", "09056941102")
        page.select_option("#country", "Nigeria")
        
        page.click("button[type='submit']")
        time.sleep(2)
        
        success = page.locator("#successMessage")
        if success.is_visible():
            print("Local form test PASSED!")
            browser.close()
            return True
        else:
            print("Local form test FAILED!")
            browser.close()
            return False

def test_online_form():
    """Test demoqa.com form"""
    print("\n" + "="*50)
    print("TESTING ONLINE FORM")
    print("="*50)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://demoqa.com/automation-practice-form")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(1)
        
        page.fill("#firstName", "Michael")
        page.fill("#lastName", "Emmanuel")
        page.fill("#userEmail", "emmanuelmichaelpk3@gmail.com")
        page.check("input[value='Male']")
        page.fill("#userNumber", "09056941102")
        
        # Add more fields as needed...
        
        page.click("#submit")
        time.sleep(3)
        
        modal = page.locator(".modal-content")
        if modal.is_visible():
            print("Online form test PASSED!")
            browser.close()
            return True
        else:
            print(" Online form test FAILED!")
            browser.close()
            return False

if __name__ == "__main__":
    # Test local form
    local_result = test_local_form()
    
    # Test online form
    online_result = test_online_form()
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Local Form:  {'PASSED' if local_result else 'FAILED'}")
    print(f"Online Form: {'PASSED' if online_result else 'FAILED'}")