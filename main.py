import sys
import configparser
import plot

def main():
    config = configparser.ConfigParser()

    config.read("setup.cfg")

    mode = config["general"]["mode"]
    n_installments_mode = mode == "installments"
    achieved_sum_mode = mode == "sum"

    varying_investments = list(map(int, config["contributions"]["installment"].split()))
    # The anual interest rate after subtracting inflation
    year_interest_rate = float(config["general"]["interest"])
    month_interest_rate = (1.0+year_interest_rate/100.0)**(1/12) - 1.0
    print("Monthly interest rate: {}".format(month_interest_rate*100.0))
    sum = 0.0
    time = [0]
    sum_list = [sum]
    if n_installments_mode:
        n_years = int(config["general"]["years"])
        print("No. years: {}".format(n_years))        
        for month in range(n_years*12):
            if month//12 < len(varying_investments):
                month_investment = varying_investments[month//12]
            else:
                month_investment = varying_investments[-1]
            sum = sum*(1.0+month_interest_rate) + month_investment
            time.append(month/12)
            sum_list.append(sum)
            # print(f"{month+1:3}. Current sum: {sum:.2f}")

        
    print(f"The savings at the end will be: {sum}")
    plot.plot_xy(time, sum_list)


if __name__ == '__main__':
    main()