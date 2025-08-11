import os
import re


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def abspath_from_tests(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, filename))


def test_signup_has_login_link_with_id():
    path = abspath_from_tests('signup.html')
    assert os.path.exists(path)
    content = read(path)
    assert 'id="login-link"' in content, 'Expected a Log in link with id="login-link"'
    assert 'href="home.html"' in content, 'Log in link should navigate to home.html'


def test_both_forms_use_post_method():
    login = read(abspath_from_tests('home.html'))
    signup = read(abspath_from_tests('signup.html'))
    assert re.search(r"<form[^>]*method=\"post\"", login, re.IGNORECASE), 'home.html form should use method="post"'
    assert re.search(r"<form[^>]*method=\"post\"", signup, re.IGNORECASE), 'signup.html form should use method="post"'


def test_signup_labels_match_input_ids():
    content = read(abspath_from_tests('signup.html'))
    # For each expected input id, there should be a matching label with for="..."
    ids = ['su-username', 'su-email', 'su-password', 'su-confirm']
    for _id in ids:
        assert f'id="{_id}"' in content, f'Missing input with id { _id }'
        assert f'for="{_id}"' in content, f'Missing label with for="{ _id }"'


def test_signup_required_attributes_present():
    content = read(abspath_from_tests('signup.html'))
    # Check required attribute on critical fields
    for _id in ['su-username', 'su-email', 'su-password', 'su-confirm']:
        pattern = rf"<input[^>]*id=\"{_id}\"[^>]*required"
        assert re.search(pattern, content, re.IGNORECASE), f'Expected required attribute on input #{_id}'

