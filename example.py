#!/usr/bin/env python

"""This example triggers a callback whenever randint(0,5) returns 2. The
callback simply prints the metric history to the screen.
"""

if __name__ == '__main__':
    import sys
    from random import randint
    from watchman import Watchman

    collector = randint

    def filter_func(history):
        """Return true if last metric == 2"""
        return history[-1][1] == 2

    def callback(history):
        """Print history to stdout"""
        sys.stdout.write(repr(history)+"\n")
        sys.stdout.flush()

    # Instantiate Watchman class with 1 second measurement intervals
    w = Watchman(collector, frequency=1)
    w.register_callback(filter_func, callback)

    try:
        w.run(0,5)
    except KeyboardInterrupt():
        quit()
                    
