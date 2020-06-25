# Pay off your credit card

This is problem set 2 of MITx 600

### Problem 1 - Paying minimum monthly paymnet

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

### Problem 2 - Paying Debt Off in a Year

Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). **The monthly payment must be a multiple of \$10** and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.

### Problem 3 - Using Bisection Search to Make the Program Faster

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? \$0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent (no more multiples of \$10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

The code must run in under 30 seconds


### Developer notes

To be able to solve problem 3 i had to use an epsilon to avoid going into an infinite loop.

I left the notes of the solution to remember how I went about this.

I used the below resources to understand this limit

http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/07/bisection.html

http://www2.hawaii.edu/~jmcfatri/math407/BisectionMethod.html#:~:text=The%20bisection%20method%20is%20a,the%20roots%20of%20a%20function.&text=(i.e.%20the%20function%20will%20cross%20zero%20somewhere%20in%20the%20interval).&text=2.&text=If%20the%20absolute%20value%20f,root%20to%20the%20desired%20precision.

https://www.youtube.com/watch?v=dHDhHtw5B-A

I really liked professor RobBob's explanation.

👾🐍❤️
