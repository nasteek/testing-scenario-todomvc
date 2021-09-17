from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def test_basic_scenario():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length === 39'))

    # Adding
    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()

    # Editing
    s('#todo-list>li:nth-of-type(3)').double_click()
    s('#todo-list>li.editing .edit').type(' edited').press_enter()

    # Completing and clearing
    s('#todo-list>li:nth-of-type(3) .toggle').click()
    ss('#todo-list>li.completed').should(have.exact_text('c edited'))
    s('#clear-completed').click()
    ss('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'b'))

    # Canceling editing
    s('#todo-list>li:nth-of-type(2)').double_click()
    s('#todo-list>li.editing .edit').type(' to cancel editing').press_escape()

    # Deleting
    s('#todo-list>li:nth-of-type(2)').hover().element('.destroy').click()
    ss('#todo-list>li').should(have.exact_texts('a'))
