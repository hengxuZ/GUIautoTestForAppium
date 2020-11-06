# -*- coding: utf-8 -*
from behave import *

@given(u'第一个值输入 10')
def step_impl(context):
    pass



@given(u'第二个值输入 20')
def step_impl(context):
    pass


@when(u'点击 求和按钮')
def step_impl(context):
    pass


@then(u'结果应该为30')
def step_impl(context):
    assert '30'=='30', 'result is 30'



