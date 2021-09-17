from testing_scenario_todomvc.helpers import app


def test_basic_scenario():
    app.open_app()

    app.add('a', 'b', 'c')
    app.assert_todos('a', 'b', 'c')

    app.edit('c', ' edited')

    app.complete('c edited')
    app.clear_completed()
    app.assert_todos('a', 'b')

    app.cancel_editing('b', ' to cancel editing')

    app.delete('b')
    app.assert_todos('a')
