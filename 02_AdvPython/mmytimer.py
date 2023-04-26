#!/usr/local/bin/python3
"""
This user written module contains a simple mechanism for
timing operations from Python.  It contains two functions,
start_timer(), which must be called first to initialise the
present time, and end_timer() which calculates the elapsed
CPU time and displays it.

"""
import os

# TODO: Append Mytimer class here

class MyTimer:
    
    _start_time: float
    _report_msg: str

    def __init__(self, report_msg):
        self._report_msg = report_msg
            
    def __start_timer(self):
        """
        The start_timer() function marks the start of 
        a timed interval, to be completed by end_timer().
        This function requires no parameters.
        """
        utime, stime = os.times()[0:2]
        self._start_time = utime + stime

    def __end_timer(self, txt: str):
        """
        The end_timer() function completes a timed interval
        started by start_timer.  It prints a text
        message followed by the CPU time
        used in seconds.
        This function has one parameter, the text to 
        be displayed.
        """
        utime, stime = os.times()[0:2]
        end_time = utime + stime

        print("{0:<12}: {1:01.3f} seconds".
            format(txt, end_time - self._start_time))
            
        self._start_time = None
    
    def __enter__(self):
        self.__start_timer()
    
    def __exit__(self, a = None, b = None, c = None):
        self.__end_timer(self._report_msg)
