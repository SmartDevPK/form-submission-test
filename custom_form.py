# test_custom_form.py
from playwright.sync_api import sync_playwright
import pytest

class TestFormSubmission:
    
    def test_form_submission(self):
        with sync_playwright() as p:
            # Setup
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Open local form
            page.goto("file:///path/to/your/form.html")
            
            # Fill form
            page.fill("#name", "Michael Emmanuel")
            page.fill("#email", "emmanuelmichaelpk3@gmail.com")
            page.fill("#phone", "09056941102")
            page.select_option("#country", "Nigeria")
            
            # Submit
            page.click("button[type='submit']")
            
            # Assert success message appears
            success_element = page.locator("#successMessage")
            
            # Verify it's visible
            assert success_element.is_visible(), "Success message not shown!"
            
            # Verify text
            assert "successfully" in success_element.inner_text().lower()
            
            print("Test PASSED: Form submitted successfully!")
            
            browser.close()
            return True

if __name__ == "__main__":
    test = TestFormSubmission()
    test.test_form_submission()