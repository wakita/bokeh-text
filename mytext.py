#!/usr/bin/env python3

from bokeh.core.properties import Int, String, List
from bokeh.layouts import column
from bokeh.models.layouts import Column, HTMLBox
from bokeh.io import show

class MyText(HTMLBox):
    __implementation__ = 'mytext.ts'
    text = List(String)
    color = List(String)
    size = List(Int)

red, green, blue = '#ff0000', '#00ff00', '#0000ff'

show(column(MyText(text=['This', 'is', 'a', 'pen.'],
                   color=[red, green, blue, red],
                   size=[12, 24, 36, 48])))
