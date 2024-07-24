import matplotlib.pyplot as plt
import Future_Value as fv

def main():

    Number_of_years = 35

    High_Interest_Savings = fv.Future_Value(895,5,250,Number_of_years,4)

    print(High_Interest_Savings.get_summary())

    plt.xlabel("Number of Years")
    plt.ylabel("Dollar Value")
    plt.ticklabel_format(useOffset=False,style="plain")


    plt.plot(High_Interest_Savings.get_time_range(),High_Interest_Savings.get_future_values())
    #plt.legend(["low_Addition,low_Interest","High_Addition,low_Interest","low_Addition,High_Interest","High_Addition,High_Interest","High_Savings"])
    plt.show()
    input()



main()