from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s

todo_list = ss('#todo-list>li')


def open_app():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(
        True, 'return Object.keys(require.s.contexts._.defined).length === 39'))


def add(*texts):
    for text in texts:
        s('#new-todo').type(text).press_enter()


def assert_todos(*todos):
    todo_list.should(have.exact_texts(*todos))


def start_editing(todo, added_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    return todo_list.element_by(have.css_class('editing')) \
        .element('.edit').type(added_text)


def edit(todo, added_text):
    start_editing(todo, added_text).press_enter()


def complete(edited_todo):
    todo_list.element_by(have.exact_text(edited_todo)). \
        element('.toggle').click()
    #todo_list.element_by(have.exact_text(edited_todo)). \
        #element('completed').should(have.exact_text(edited_todo))


def clear_completed():
    #s('#filters li:nth-child(3)').click()
    s('#clear-completed').click()


#def assert_completed(*todos):
    #todo_list.element_by(have.no.css_class('.completed)').should(have.exact_texts(*todos))


def cancel_editing(todo, added_text):
    start_editing(todo, added_text).press_escape()


def delete(todo):
    todo_list.element_by(have.exact_text(todo)). \
        hover().element('.destroy').click()
