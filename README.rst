watchman
========

Author: Charles Hooper <chooper@plumata.com>

Framework to monitor a [generic] value and trigger actions based on that value.

The hope is that a programmer can subclass a generic object and write
their own code to access a given value (could be a redis object, a text file,
whatever) and then register callbacks based on the results of that value.

This is implemented through user/programmer-defined filter functions
and user/programmer-defined callbacks.

Context: Originally written to automatically deploy new EC2 instances 
based on the size of a celery task queue.

