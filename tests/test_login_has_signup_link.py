import os


def test_login_page_has_signup_link():
    path = os.path.join(os.path.dirname(__file__), os.pardir, 'login.html')
    path = os.path.abspath(path)
    assert os.path.exists(path), 'login.html should exist'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for anchor to signup.html with id for robustness
    assert 'id="signup-link"' in content, 'Expected a signup link with id="signup-link"'
    assert 'href="signup.html"' in content, 'Signup link should navigate to signup.html'
    # Optional: visible text contains "Sign up"
    assert any(text in content for text in ('Sign up', 'Sign Up', 'Create one')), (
        'Signup link text should be present'
    )
    # Login form should capture identifier, password and remember-me checkbox
    assert 'id="login-identifier"' in content, 'Login page should have an identifier input'
    assert 'name="identifier"' in content, 'Identifier input should use name="identifier"'
    assert 'id="login-password"' in content, 'Login page should have a password input'
    assert 'name="password"' in content, 'Password input should use name="password"'
    assert 'method="post"' in content.lower(), 'Login form should submit via POST'
    assert 'id="remember-me"' in content, 'Login page should have a remember me checkbox'
    assert 'id="forgot-password-link"' in content, 'Expected a forgot password link'
