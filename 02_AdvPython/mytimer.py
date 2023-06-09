#!/usr/local/bin/python3
"""
This user written module contains a simple mechanism for
timing operations from Python.  It contains two functions,
start_timer(), which must be called first to initialise the
present time, and end_timer() which calculates the elapsed
CPU time and displays it.

"""
import os
start_time = None

# TODO: Append Mytimer class here

class MyTimer:
    
    _report_msg: str

    def __init__(self, report_msg: str = "Timer has ended."):
        self._report_msg = report_msg
            
    def __start_timer():
        """
        The start_timer() function marks the start of 
        a timed interval, to be completed by end_timer().
        This function requires no parameters.
        """
        global start_time
        utime, stime = os.times()[0:2]
        start_time = utime + stime

    def __end_timer(txt: str = _report_msg):
        """
        The end_timer() function completes a timed interval
        started by start_timer.  It prints an optional text
        message (default 'End time') followed by the CPU time
        used in seconds.
        This function has one optional parameter, the text to 
        be displayed.
        """
        global start_time
        if start_time is None:
            raise SystemError(
                "end_timer() called without a start_timer()")
        utime, stime = os.times()[0:2]
        end_time = utime + stime
        print("{0:<12}: {1:01.3f} seconds".
            format(txt, end_time-start_time))
            
        start_time = None
    
    def __enter__(self):
        self.__start_timer()
        return self
    
    def __exit__(self):
        self.__end_timer(self._report_msg)
        return self
    