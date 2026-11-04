import pytest

from todo import TodoList


def test_add_task():
    todo = TodoList()
    task = todo.add("Estudar Engenharia de Software")
    assert task.id == 1
    assert task.title == "Estudar Engenharia de Software"
    assert task.done is False
    assert len(todo) == 1


def test_add_empty_title_raises():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add("   ")


def test_ids_are_incremental():
    todo = TodoList()
    assert todo.add("a").id == 1
    assert todo.add("b").id == 2


def test_remove_task():
    todo = TodoList()
    task = todo.add("a")
    todo.remove(task.id)
    assert len(todo) == 0


def test_remove_missing_task_raises():
    todo = TodoList()
    with pytest.raises(KeyError):
        todo.remove(42)


def test_complete_task():
    todo = TodoList()
    task = todo.add("a")
    todo.complete(task.id)
    assert todo.list()[0].done is True


def test_complete_missing_task_raises():
    todo = TodoList()
    with pytest.raises(KeyError):
        todo.complete(99)


def test_list_only_pending():
    todo = TodoList()
    a = todo.add("a")
    todo.add("b")
    todo.complete(a.id)
    pending = todo.list(only_pending=True)
    assert [t.title for t in pending] == ["b"]
