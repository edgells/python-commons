

"""
    python 在c10k 问题的解决方案：

    传统多进程实现， 有cpu上下文切换，造成性能消耗。
    多线程， 因为GIL lock 存在， 导致 无法使用多核心并发
    协程：
        用户态线程，绿色线程。
        由程序员在应用级别调度。 减少了cpu context change
        只能单核

    多进程 + 协程：
        由于 单进程内 使用协程可以形成并发。充分利用cpu 哪么多进程下只需要有中间调度， 是不是可以实现多核并发
"""

