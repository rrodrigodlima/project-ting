from ting_file_management.priority_queue import PriorityQueue
import pytest


@pytest.fixture
def priority_queue():
    return PriorityQueue()


def test_basic_priority_queueing(priority_queue):
    priority_file = {
        "nome_do_arquivo": "teste",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }

    no_priority_file = {
        "nome_do_arquivo": "teste",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }

    no_priority_file_2 = {
        "nome_do_arquivo": "teste",
        "qtd_linhas": 8,
        "linhas_do_arquivo": [],
    }

    priority_queue.enqueue(priority_file)
    priority_queue.enqueue(no_priority_file)
    priority_queue.enqueue(no_priority_file_2)

    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue) == 3

    assert priority_queue.high_priority.search(0) == priority_file
    assert priority_queue.regular_priority.search(0) == no_priority_file
    assert priority_queue.regular_priority.search(1) == no_priority_file_2
    assert priority_queue.search(0) == priority_file
    assert priority_queue.search(1) == no_priority_file
    assert priority_queue.search(2) == no_priority_file_2

    assert priority_queue.dequeue() == priority_file
    assert priority_queue.dequeue() == no_priority_file
    assert priority_queue.dequeue() == no_priority_file_2

    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0
    assert len(priority_queue) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(15)
