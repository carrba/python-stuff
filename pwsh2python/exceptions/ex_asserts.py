#!/usr/bin/python3

def av_grades(grades):
    assert len(grades) > 0, "No grade data"
    av = sum(grades)/len(grades)
    return av