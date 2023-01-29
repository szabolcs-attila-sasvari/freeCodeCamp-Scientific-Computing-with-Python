<h1 align="center"><string>Probability Calculator</string></h1>

## **Assignment**

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a <code>Hat</code> class in <code>prob_calculator.py</code>. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```
A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a <code>contents</code> instance variable. <code>contents</code> should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is <code>{"red": 2, "blue": 1}</code>, <code>contents</code> should be <code>["red", "red", "blue"]</code>.

The <code>Hat</code> class should have a <code>draw</code> method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from <code>contents</code> and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an <code>experiment</code> function in <code>prob_calculator.py</code> (not inside the <code>Hat</code> class). This function should accept the following arguments:

- <code>hat</code>: A hat object containing balls that should be copied inside the function.
- <code>expected_balls</code>: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set <code>expected_balls</code> to <code>{"blue":2, "red":1}</code>.
- <code>num_balls_drawn</code>: The number of balls to draw out of the hat in each experiment.
- <code>num_experiments</code>: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The <code>experiment</code> function should return a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform <code>N</code> experiments, count how many times <code>M</code> you get at least two red balls and one green ball, and estimate the probability as <code>M/N</code>. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the <code>experiment</code> function based on the example above with 2000 experiments:
```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```
Since this is based on random draws, the probability will be slightly different each time the code is run.

*Hint: Consider using the modules that are already imported at the top of <code>prob_calculator.py</code>. Do not initialize random seed within <code>prob_calculator.py</code>.*

## **Development**
Write your code in <code>prob_calculator.py</code>. For development, you can use <code>main.py</code> to test your code. Click the "run" button and <code>main.py</code> will run.

The boilerplate includes <code>import</code> statements for the <code>copy</code> and <code>random</code> modules. Consider using those in your project.

## **Testing**
The unit tests for this project are in <code>test_module.py</code>. We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.

## **Submitting**
Copy your project's URL and submit it to freeCodeCamp.
