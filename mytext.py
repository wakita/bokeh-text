#!/usr/bin/env python3

from bokeh.core.properties import String, List
from bokeh.layouts import column
from bokeh.models.layouts import Column, HTMLBox
from bokeh.io import show

class MyText(HTMLBox):
    __implementation__ = 'mytext.ts'
    text = List(String)

show(column(MyText(text=['This', 'is', 'a', 'pen.'])))
