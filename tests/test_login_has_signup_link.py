import os


def test_login_page_has_signup_link():
    path = os.path.join(os.path.dirname(__file__), os.pardir, 'home.html')
    path = os.path.abspath(path)
    assert os.path.exists(path), 'home.html should exist'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for anchor to signup.html with id for robustness
    assert 'id="signup-link"' in content, 'Expected a signup link with id="signup-link"'
    assert 'href="signup.html"' in content, 'Signup link should navigate to signup.html'
    # Optional: visible text contains "Sign up"
    assert 'Sign up' in content or 'Sign Up' in content, 'Signup link text should be present'

