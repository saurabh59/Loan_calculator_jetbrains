#Loan_calculator_jetbrains
Stage 1
Description

Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

Not familiar with these concepts? Don't worry, we will explain them to you in simple terms. The principal is the original amount of money you borrow. The interest is a charge for borrowing that money, usually calculated as a percentage of the principal amount.
Objectives

Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.

Stage 2
Description

If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.

In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

payment=principalmonths=10009=111.11...payment = \dfrac{principal}{months}=\dfrac{1000}{9} =111.11...payment=monthsprincipal​=91000​=111.11...

Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

lastpayment=principal−(periods−1)∗payment=1000−8∗112=104lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104lastpayment=principal−(periods−1)∗payment=1000−8∗112=104

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.
Objectives

The behavior of your program should look like this:

    Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
    To perform further calculations, you'll also have to ask for the required missing value.
    Finally, output the results for the user.
Stage 3
In this stage, you should add new behavior to the calculator:

    First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
    Then, you need to ask them to input the remaining values.
    Finally, compute and output the value that they wanted.

Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.

Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

    The first is the loan principal.
    The second is the monthly payment.
    The next is the number of monthly payments.
    The last is the loan interest.
Stage 4
In this stage, you are going to implement the following features:

    Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
    Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
    Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line and parse the following parameters:

    --type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message. 
    --payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too: 
    --principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
    --periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing: 

You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:
