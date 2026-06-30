import pytest
from playwright.sync_api import sync_playwright

class TestFormQA:
    
    @pytest.fixture
    def browser_setup(self):
        """Setup browser for tests"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            yield page
            browser.close()
    
    def test_valid_submission(self, browser_setup):
        """Test valid form submission"""
        page = browser_setup
        page.goto("your-form-url")
        # ... fill and submit
        # check for a visible success message on the page
        success = page.locator('.success-message')
        assert success.is_visible()
    
    def test_invalid_email(self, browser_setup):
        """Test invalid email validation"""
        page = browser_setup
        # ... fill with invalid email
        # Should show error
        error = page.locator('.error-message')
        assert error.is_visible()