"""Lista de tarefas simples."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TodoList:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("O título não pode ser vazio")
        task = Task(self._next_id, title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def remove(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"Tarefa {task_id} não encontrada")
        del self._tasks[task_id]

    def complete(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise KeyError(f"Tarefa {task_id} não encontrada")
        task = self._tasks[task_id]
        task.done = True
        return task

    def list(self, only_pending: bool = False) -> list[Task]:
        tasks = list(self._tasks.values())
        if only_pending:
            tasks = [t for t in tasks if not t.done]
        return tasks

    def __len__(self) -> int:
        return len(self._tasks)
