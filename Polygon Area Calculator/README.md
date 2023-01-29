<h1 align="center"><string>Polygon Area Calculator</string></h1>

## **Assignment**

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

## **Rectangle class**
When a Rectangle object is created, it should be initialized with <code>width</code> and <height>height</code> attributes. The class should also contain the following methods:

- <code>set_width</code>
- <code>set_height</code>
- <code>get_area</code>: Returns area (<code>width * height</code>)
- <code>get_perimeter</code>: Returns perimeter (<code>2 * width + 2 * height</code>)
- <code>get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5</code>)
- <code>get_picture</code>: Returns a string that represents the shape using lines of "\*". The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width. There should be a new line (<code>\n</code>) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
- <code>get_amount_inside</code>: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: <code>Rectangle(width=5, height=10)</code>

## **Square class**
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The <code>\_\_init\_\_</code> method should store the side length in both the <code>width</code> and <code>height</code> attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a <code>set_side</code> method. If an instance of a Square is represented as a string, it should look like: <code>Square(side=9)</code>

Additionally, the <code>set_width</code> and <code>set_height</code> methods on the Square class should set both the width and height.

## **Usage example**
```python
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:
```python
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
The unit tests for this project are in <code>test_module.py</code>.

## **Development**
Write your code in <code>shape_calculator.py</code>. For development, you can use <code>main.py</code> to test your <code>shape_calculator()</code> function. Click the "run" button and <code>main.py</code> will run.

## **Testing**
We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.

## **Submitting**
Copy your project's URL and submit it to freeCodeCamp.
