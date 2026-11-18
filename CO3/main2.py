from graphics import rectangle,circle
from graphics.threedgraphics import cuboid,sphere
print("Rectangle area ",rectangle.area(10,5))
print("Rectangle perimeter",rectangle.perimeter(10,5))

print("circle area:",circle.area(6))
print("circle perimeter:",circle.perimeter(6))

print("cuboid area:",cuboid.area(2,3,4))
print("cuboid perimeter:",cuboid.perimeter(4,5,6))

print("sphere area:",sphere.area(2,3,4))
print("sphere volume:",sphere.volume())