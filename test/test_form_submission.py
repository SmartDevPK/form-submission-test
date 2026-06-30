# Success verification methods
def verify_success(self, page):
    # Method 1: Check element visible
    assert page.locator(".success").is_visible()
    
    # Method 2: Check network response
    assert "success" in page.content()
    
    # Method 3: Check URL changed
    assert "thank-you" in page.url
    
    # Method 4: Check for specific text
    assert "Submission successful" in page.inner_text()