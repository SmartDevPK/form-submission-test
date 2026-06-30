# Form Submission Test Suite

> Automated form testing using Playwright - Created by **Michael Emmanuel**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40.0-green.svg)](https://playwright.dev/)
[![Status](https://img.shields.io/badge/status-passing-brightgreen)]()

---

## 📖 About

This is a simple automated test suite for testing web form submissions using **Playwright**. It tests both local and online forms with complete field coverage.

**Author**: Michael Emmanuel  
**Email**: emmanuelmichaelpk3@gmail.com  

---

## ✨ Features

- ✅ Test local HTML forms
- ✅ Test online DemoQA forms
- ✅ All fields covered (Name, Email, Phone, Country, Hobbies, Address, State, City)
- ✅ Auto-screenshots on failure
- ✅ Easy to run and debug

---

## 🚀 Quick Start

### 1. Clone and Install

```bash
git clone git remote add origin git@github.com:SmartDevPK/form-submission-test.git
cd form-submission-test

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install