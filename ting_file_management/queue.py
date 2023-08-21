from ting_file_management.abstract_queue import AbstractQueue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(AbstractQueue):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def search(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice Inválido ou Inexistente")
        current = self.front
        for _ in range(index):
            current = current.next
        return current.data
