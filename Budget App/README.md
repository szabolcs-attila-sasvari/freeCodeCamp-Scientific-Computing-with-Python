Complete the <code>Category</code> class in <code>budget.py</code>. It should be able to instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class should have an instance variable called <code>ledger</code> that is a list. The class should also contain the following methods:

- A <code>deposit</code> method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of <code>{"amount": amount, "description": description}</code>.
- A <code>withdraw</code> method that is similar to the <code>deposit</code> method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return <code>True</code> if the withdrawal took place, and <code>False</code> otherwise.
- A <code>get_balance</code> method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A <code>transfer</code> method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return <code>True</code> if the transfer took place, and <code>False</code> otherwise.
- A <code>check_funds</code> method that accepts an amount as an argument. It returns <code>False</code> if the amount is greater than the balance of the budget category and returns <code>True</code> otherwise. This method should be used by both the <code>withdraw</code> method and <code>transfer</code> method.

When the budget object is printed it should display:

- A title line of 30 characters where the name of the category is centered in a line of <code>*</code> characters.
- A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
- A line displaying the category total.

Here is an example of the output:
```python
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
Besides the <code>Category</code> class, create a function (outside of the class) called <code>create_spend_chart</code> that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.
```python
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
The unit tests for this project are in <code>test_module.py</code>.

## **Development**
Write your code in <code>budget.py</code>. For development, you can use <code>main.py</code> to test your <code>Category</code> class. Click the "run" button and <code>main.py</code> will run.

## **Testing**
We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.

## **Submitting**
Copy your project's URL and submit it to freeCodeCamp.
