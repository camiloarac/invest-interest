import sys
import configparser
def main():
    config = configparser.ConfigParser()

    config.read("setup.cfg")
    mode = config["general"]["mode"]
    nInstallmentsMode = False
    achievedSumMode = False
    if mode == "installments":
        nInstallmentsMode = True
    elif mode == "sum":
        achievedSumMode = True
    varyingInvestments = list(map(int, config["contributions"]["wage"].split()))
    # The anual interest rate after subtracting inflation
    netoInterestRate = float(config["general"]["interest"])
    monthInterestRate = (1.0+netoInterestRate/100.0)**(1/12) - 1.0
    print("Monthly interest rate: {}".format(monthInterestRate*100.0))
    sum = 0.0
    if nInstallmentsMode:
        nYears = int(config["general"]["years"])
        print("No. years: {}".format(nYears))        
        for i in range(nYears*12):
            if i//12 < len(varyingInvestments):
                monthlyInvestment = varyingInvestments[i//12]
            else:
                monthlyInvestment = varyingInvestments[-1]
            sum = sum*(1.0+monthInterestRate) + monthlyInvestment
            print("{}. Current sum: {}".format(i+1, sum))

        
        print("The savings at the end will be of: {}".format(sum))


if __name__ == '__main__':
    main()