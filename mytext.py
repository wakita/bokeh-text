#!/usr/bin/env python3

from bokeh.core.properties import String, List
from bokeh.layouts import column
from bokeh.models.layouts import Column, HTMLBox
from bokeh.io import show

class MyText(HTMLBox):
    __implementation__ = 'mytext.ts'
    text = String(default='')

show(column(MyText(text='This is a pen.'),
            MyText(text='Is this a pen?'),
            MyText(text='This is an apple.'),
            MyText(text='I like oranges.')))
