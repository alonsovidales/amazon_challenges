#!/usr/bin/env python
# -*- coding: utf-8 -*- 

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class MeetingSchedules:
    """
    """
    __debug = True

    def resolve(self, time):
        slots = []
        in_slot = False
        for minutePos in self.__hours:
            if not minutePos:
                if in_slot:
                    

        if self.__debug:
            print self.__hours
        return ''

    def add_slot(self, time_slot):
        from_min = time_slot[0] * 60 + time_slot[1]
        to_min = time_slot[2] * 60 + time_slot[3]

        for minute in range(from_min, to_min):
            self.__hours[minute] = True

        if self.__debug:
            print "From: %d To: %d" % (from_min, to_min)

    def __init__(self):
        self.__hours = [False] * 24 * 60

if __name__ == "__main__":
    [slots, time] = map(int, raw_input().split())

    print "Slots: %d Time: %d" % (slots, time)

    schedule = MeetingSchedules()
    for slot in range(slots):
        schedule.add_slot(map(int, raw_input().split()))

    print schedule.resolve(time)
