# namedtuple returns a class (that's a child of the built-in class tuple).
# The first argument you pass to namedtuple becomes the name of the class,
# while the list of strings becomes the attributes (data fields).

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
print(color.red)

# color = (55, 155, 255)
# print(color[0])

# color = {'red': 55, 'green': 155, 'blue': 255}
# print(color['red'])
