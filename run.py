# -*- coding: UTF-8 -*-

ioloop = None
t = None


def start():
    global ioloop, t
    import controller
    from threading import Thread
    from tornado.ioloop import IOLoop
    from src import messages

    messages.starting()

    ioloop = IOLoop.instance()
    t = Thread(target=lambda: ioloop.start())
    t.start()

    messages.welcome()


def stop():
    from src import messages

    # @coroutine
    def callback():
        """Stop application

        Here you can stop other services, like a database ;).
        Uncomment ``@coroutine`` if you want to yield futures
        in this function.
        """
        ioloop.stop()

    ioloop.add_callback(callback)
    t.join()

    messages.stopped()

if __name__ == "__main__":
    from src.utils import run_inside
    
    start()

    def q():
        from sys import exit
        stop()
        exit()

    def h():
        from sys import modules
        help(modules[__name__])

    def make(goal):
        from os import system
        system('make %s' % goal)
    
    @run_inside(ioloop.add_callback)
    def clients():
        from controller import MSGHandler
        total = MSGHandler.client_count
        current = len(MSGHandler.clients)
        print('Connected clients: %d' % current)
        print('Total connections opened: %d' % total)
        print(
            'Total connections closed: %d' % (total-current)
        )

    @run_inside(ioloop.add_callback)
    def bcast(message):
        from controller import MSGHandler
        MSGHandler.broadcast(message)
