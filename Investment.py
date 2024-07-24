# This is not a library that comes pre installed in python. You can easily add it by typing `pip install matplotlib` in your command line/ terminal once python is installed.
# This line allows you to use those functions that let me graph.
import matplotlib.pyplot as plt
# This imports all of the code from the Future_Value.py file so I can use anything I built ther in here.
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