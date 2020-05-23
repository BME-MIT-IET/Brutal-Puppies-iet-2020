from behave import *
from algorithms.backtrack.pattern_match import pattern_match


@given('a {pattern} and a {word}')
def step_impl(context, pattern: str, word: str):
    assert pattern is not None
    assert word is not None


@when('the {pattern} is in the {word}')
def step_impl(context, pattern: str, word: str):
    assert pattern_match(pattern, word) is True


@when('the {pattern} is not in the {word}')
def step_impl(context, pattern: str, word: str):
    assert pattern_match(pattern, word) is False


@then('the pattern searching is successful')
def step_impl(context):
    assert True is not False


@then('the pattern searching is a failure')
def step_impl(context):
    assert False is not True
