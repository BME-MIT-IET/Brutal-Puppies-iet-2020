from behave import *
from algorithms.matrix.matrix_inversion import get_determinant, invert_matrix, array_is_matrix

matrixD = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
arrayA = [[1, 2, 3, 4, 5, 6], [1]]
matrixS = [[1]]
matrixNS = [[1, 2], [1, 2], [1, 2]]


@given('a matrix {matrix}')
def step_impl(context, matrix):
    assert True


@given('a array {array}')
def step_impl(context, array):
    assert True


@when('the determinant is 0')
def step_impl(context):
    assert (get_determinant(matrixD) == 0)


@when('the matrix is not square')
def step_impl(context):
    assert len(matrixNS) != len(matrixNS[0])


@when('the array is not matrix')
def step_impl(context):
    assert array_is_matrix(arrayA) is False


@when('the matrix is too small')
def step_impl(context):
    assert len(matrixS) < 2


@then('the result is -1')
def step_impl(context):
    assert (invert_matrix(arrayA) == [[-1]])


@then('the result is -2')
def step_impl(context):
    assert (invert_matrix(matrixNS) == [[-2]])


@then('the result is -3')
def step_impl(context):
    assert (invert_matrix(matrixS) == [[-3]])


@then('the result is -4')
def step_impl(context):
    assert (invert_matrix(matrixD) == [[-4]])
