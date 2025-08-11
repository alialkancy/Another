import os
import re


def test_signup_page_exists_and_has_form_fields():
    path = os.path.join(os.path.dirname(__file__), os.pardir, 'signup.html')
    path = os.path.abspath(path)
    assert os.path.exists(path), 'signup.html should exist'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Basic checks for a form and key inputs
    assert '<form' in content and '</form>' in content, 'Signup page should contain a form'
    for field in [
        'name="username"',
        'name="email"',
        'name="password"',
        'name="confirm"',
    ]:
        assert field in content, f'Missing input field {field}'

    # Check there is a submit button with expected text
    assert re.search(r">\s*Create account\s*<", content, re.IGNORECASE), 'Expected a Create account button'

