import _2D
import convert._3D.to._1D

print(_2D.Replace([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 3, 4))
print(_2D.Find([[1, 2, 3], [3, 2, 1], [3, 4, 5]], 2))
print(convert._3D.to._1D.RowMajor([[1, 2, 3], [3, 2, 1], [3, 4, 5]]))
