import sys
def main():
    if len(sys.argv) < 2:
        print("Please select one mode as parameter")
        return 1
    nInstallmentsMode = False
    achievedSumMode = False
    if sys.argv[1] == "installments":
        nInstallmentsMode = True
    elif sys.argv[1] == "sum":
        achievedSumMode = True
    initialMonthlyInvestment = 1500
    # The anual interest rate after subtracting inflation
    netoInterestRate = 3.0
    monthInterestRate = (1.0+netoInterestRate/100.0)**(1/12) - 1.0
    print("Monthly interest rate: {}".format(monthInterestRate*100.0))
    sum = 0.0
    if nInstallmentsMode:
        print("Insert the number of installments")
        nInstallments = int(input())
        
        for i in range(nInstallments):
            sum = sum*(1.0+monthInterestRate) + initialMonthlyInvestment
        
        print("The savings at the end will be of: {}".format(sum))


if __name__ == '__main__':
    main()