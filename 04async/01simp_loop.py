
"""
    手动实现一个 event loop

"""
from queue import Queue


class Task:
    TASK_ID = 0
    def __init__(self, coro):
        self._coro = coro
        Task.TASK_ID += 1
        self.tid =Task.TASK_ID
        self.sendval = None

    def run(self):
        return self._coro.send(self.sendval)


class Scheduer:

    def __init__(self):
        self._queue = Queue()  # 线程安全的队列
        self.task_map = dict()

    def new(self, coro):
        new_task = Task(coro)
        self.task_map[new_task.tid] = new_task
        self.scheduler(new_task)
        return new_task.tid

    def scheduler(self, task):
        self._queue.put(task)

    def main_loop(self):
        while self.task_map:
            task = self._queue.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.scheduler(task)

    def exit(self, task):
        print("Task %d terminated" % task.tid)
        del self.task_map[task.tid]


def foo():
    for n in range(10):
        print("I m foo")
        yield


def bar():
    for n in range(10):
        print("I m bar")
        yield


if __name__ == '__main__':
    schedu = Scheduer()
    schedu.new(foo())
    schedu.new(bar())
    schedu.main_loop()
