# test_form.py
from playwright.sync_api import sync_playwright
import time
import os

def test_form_submission():
    """
    This script:
    1. Opens a demo form
    2. Fills in all fields
    3. Submits
    4. Verifies success
    """
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to form
        print("🌐 Navigating to form...")
        page.goto("https://demoqa.com/automation-practice-form")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(1)
        
        # ---------- PERSONAL INFORMATION ----------
        print("Filling personal information...")
        
        # Name
        page.fill("#firstName", "Michael")
        page.fill("#lastName", "Emmanuel")
        
        # Email
        page.fill("#userEmail", "emmanuelmichaelpk3@gmail.com")
        
        # Gender - Male
        page.check("input[value='Male']")
        
        # Phone
        page.fill("#userNumber", "09056941102")
        
        # ---------- ADDITIONAL FIELDS ----------
        print("Filling additional information...")
        
        # Date of Birth
        page.click("#dateOfBirthInput")
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        page.fill("#dateOfBirthInput", "15 May 1990")
        page.keyboard.press("Enter")
        
        # Subject
        page.fill("#subjectsInput", "python developer")
        page.keyboard.press("Enter")
        
        # ---------- HOBBIES ----------
        print("Selecting hobbies...")
        page.check("input[value='Sports']")
        page.check("input[value='Reading']")
        page.check("input[value='Music']")
        
        # ---------- ADDRESS ----------
        print("Entering address...")
        page.fill("#currentAddress", "123 Lagos Street, Abuja, Nigeria")
        
        # ---------- STATE AND CITY ----------
        print("Selecting state and city...")
        
        # Select State
        page.click("#state")
        time.sleep(0.5)
        page.click("text=Uttar Pradesh")
        time.sleep(0.5)
        
        # Select City
        page.click("#city")
        time.sleep(0.5)
        page.click("text=Agra")
        
        # ---------- SUBMIT FORM ----------
        print("Submitting form...")
        
        # Scroll to submit button
        page.locator("#submit").scroll_into_view_if_needed()
        time.sleep(1)
        
        # Click submit
        page.click("#submit")
        
        # ---------- VERIFICATION ----------
        print("Waiting for response...")
        time.sleep(3)
        
        # Check if modal appears
        success_modal = page.locator(".modal-content")
        
        if success_modal.is_visible():
            print("\n" + "="*50)
            print("SUCCESS: Form submitted successfully!")
            print("="*50)
            
            # Get the submitted data
            modal_text = success_modal.inner_text()
            print(f"\nResponse:\n{modal_text}")
            
            # Close modal
            page.click("#closeLargeModal")
            
            print("\n🎉 Test Passed!")
            time.sleep(2)
            browser.close()
            return True
        else:
            print("\n FAILED: Form not submitted")
            browser.close()
            return False

if __name__ == "__main__":
    test_form_submission()