from behave import *
from algorithms.search.linear_search import linear_search

array = [1, 2, 3, 4, 5]


@given('an array and a query {query:d}')
def step_impl(context, query: int):
    assert (array == [1, 2, 3, 4, 5])
    assert query is not None


@when('the {query:d} is in the array')
def step_impl(context, query: int):
    assert (linear_search(array, query) != (-1))


@when('the {query:d} is not in the array')
def step_impl(context, query: int):
    assert (linear_search(array, query) == (-1))


@then('became -1 of {query:d}')
def step_impl(context, query: int):
    assert (linear_search(array, query) == (-1))


@then('became {position:d} of {query:d}')
def step_impl(context, position: int, query: int):
    assert (linear_search(array, query) == position)
