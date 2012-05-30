#!/usr/bin/env python

import time

class HistoryBuffer(list):
    """Just a simple implementation of a capped list"""
    def __init__(self, size):
        self.size = size
        list.__init__(self)

    def append(self, item):
        list.append(self,item)
        if len(self) > self.size:
            del self[0]


class Watchman(object):
    """Take measurements and trigger callbacks based on whether
    filter functions return True or not.

    `frequency` is how often to run check (in seconds)

    `callbacks` is list of (`filter_func`, `callback`) where `filter_func`
        takes the history list as an argument and returns True when the
        callback should be triggered. `callback` also takes the history
        list as an argument

    `history` is list of (`timestamp`, `value`)

    `end_on_match` determines whether Watchman instance will
        stop evaluating filter functions after one returns True

    `__init__` arg `collector` is a callable that will return a single metric

    """

    # TODO: default/fall-through callback?

    _collector = None
    frequency = 300
    callbacks = []
    history = HistoryBuffer(0)
    end_on_match = False

    def __init__(self, collector, frequency=300, hist_size=10, end_on_match=False):
        self._collector = collector
        self.frequency = frequency
        self.history = HistoryBuffer(hist_size)
        self.end_on_match = end_on_match

    def register_callback(self, filter_func, callback):
        self.callbacks.append( (filter_func, callback) )

    def register_value(self, value):
        self.history.append( (time.time(), value) )

    def measure(self, *args, **kwargs):
        return self._collector(*args, **kwargs)

    def run(self, *args, **kwargs):
        """Begin main loop. Passes `args` and `kwargs` to `self.collector`"""
        while True:
            next_time = time.time() + self.frequency

            # Take measurement
            val = self.measure(*args, **kwargs)
            self.register_value(val)

            # Apply filter_funcs
            for filter_func, callback in self.callbacks:
                status = filter_func(self.history)
                if status:
                    callback(self.history)
                    if self.end_on_match:
                        break

            while time.time() < next_time:
                time.sleep(next_time - time.time())

