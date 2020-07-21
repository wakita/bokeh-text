#!/usr/bin/env python3

from bokeh.core.properties import String, List
from bokeh.models.layouts import Panel, HTMLBox
from bokeh.io import show

class MyText(HTMLBox):
    __implementation__ = 'text.ts'
    # text = List(String, default = ['a', 'b', 'c'])
    pass

text = MyText()
show(text)
