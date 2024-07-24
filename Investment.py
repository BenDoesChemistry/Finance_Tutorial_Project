import matplotlib.pyplot as plt
import Future_Value as fv

def main():
    Principle = 6000
    Number_of_years = 30
    Investment_Percent = 10
    Added_per_quarter = 800

    Investment = fv.Future_Value(Principle,Investment_Percent,Added_per_quarter,Number_of_years,4)
    High_Interest_Savings = fv.Future_Value(Principle,5,Added_per_quarter,Number_of_years,4)

    print(High_Interest_Savings.get_summary())
    print(Investment.get_summary())

    plt.xlabel("Number of Years")
    plt.ylabel("Dollar Value")
    plt.ticklabel_format(useOffset=False,style="plain")


    plt.plot(High_Interest_Savings.get_time_range(),High_Interest_Savings.get_future_values())
    plt.plot(Investment.get_time_range(),Investment.get_future_values())
    plt.legend(["High Interest Savings", "Investment " + str(Investment_Percent)+ "%"])
    plt.show()
    input()



main()