from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s

def open_app():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length === 39'))


def add(text):
    s('#new-todo').type(text).press_enter()


def assert_todos(*todos):
    ss('#todo-list>li').should(have.exact_texts(*todos))


def edit(added_text):
    s('#todo-list>li:nth-of-type(3)').double_click()
    s('#todo-list>li.editing .edit').type(added_text).press_enter()


def complete(edited_todo):
    s('#todo-list>li:nth-of-type(3) .toggle').click()
    ss('#todo-list>li.completed').should(have.exact_text(edited_todo))


def clear_completed():
    s('#clear-completed').click()


def assert_completed(*todos):
    ss('#todo-list>li:not(.completed)').should(have.exact_texts(*todos))


def cancel_editing(added_text):
    s('#todo-list>li:nth-of-type(2)').double_click()
    s('#todo-list>li.editing .edit').type(added_text).press_escape()


def delete():
    s('#todo-list>li:nth-of-type(2)').hover().element('.destroy').click()