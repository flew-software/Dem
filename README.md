![https://pypi.org/project/Dem](https://img.shields.io/pypi/v/dem.svg)
![https://pypi.org/project/Dem](https://pypip.in/license/blackhole/badge.svg)

## Download

`pip install Dem`

## What is Dem

Dem is a python library to make using list more easy

## What dose it contain

Dem currently contains utilities to work with 2D lists(get_row, get_column, replace, find), convert 2d lists to 1d lists

## example

```python

import _2D
import convert._3D.to._1D

print(_2D.Replace([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 3, 4))
print(_2D.Find([[1, 2, 3], [3, 2, 1], [3, 4, 5]], 2))
print(convert._3D.to._1D.RowMajor([[1, 2, 3], [3, 2, 1], [3, 4, 5]]))


```
