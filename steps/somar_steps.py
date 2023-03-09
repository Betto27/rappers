from behave import *
from nose.tools import assert_equal
from time import sleep


@given(u'que acesso uma calculadora')
def step_impl(context):
    pass


@when(u'insiro os valores {n1} e {n2}')
def step_impl(context, n1, n2):
    context.total = int(n1) + int(n2)


@then(u'o resultado é {result}')
def step_impl(context, result):
    assert_equal(context.total, int(result))
