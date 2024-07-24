import matplotlib.pyplot as plt
# future value function calculates the future value of an investment over a number of years.
def future_value(Principle_value:float,Percent_Increase:float,Payment_Per_Period:float,Number_Periods:int,Matches_Per_Period:int) -> float:
    # A variable to modify as we move through the years
    Accumulator = Principle_value
    # This loop occurs for the total number of payment periods.
    for i in range(Number_Periods*Matches_Per_Period):
        # Add the amount you would add per payment period
        Accumulator = Accumulator + Payment_Per_Period
        # Apply interest for the interest period
        Accumulator = Accumulator * (1 + (Percent_Increase / (100*Matches_Per_Period)))
    # Return the  future value
    return round(Accumulator,2)

def future_value_list(Principle_value:float,Percent_Increase:float,Payment_Per_Period:float,Number_Periods:int,Matches_Per_Period:int):
    Accumulator = Principle_value
    Val_List = [[],[]]
    Val_List[0].append(0)
    Val_List[1].append(Accumulator)
    for i in range(Number_Periods*Matches_Per_Period):
        # Add the amount you would add per payment period
        Accumulator = Accumulator + Payment_Per_Period
        # Apply interest for the interest period
        Accumulator = Accumulator * (1 + (Percent_Increase / (100*Matches_Per_Period)))
        Val_List[0].append((i+1)/Matches_Per_Period)
        Val_List[1].append(round(Accumulator,2))
    return Val_List

#def Mults_CSV(Principle_value:float,Percent_Increase,Payment_Per_Period:float,Number_Periods:int,Matches_Per_Period:int):
    #for i in Percent_Increase:

def List_to_CSV(List_Thing,File_Name):
    string = ""
    template_string = "{},{}\n"
    for i in range(len(List_Thing[0])):
        string = string + template_string.format(List_Thing[0][i],List_Thing[1][i])

    with open(File_Name,"w") as file:
        file.write(string)


# sumarize_future_value in a clean print function
def summarize_future_value(Principle_value:float,Percent_Increase:float,Payment_Per_Period:float,Number_Periods:int,Matches_Per_Period:int) -> None:
    Future_Value = future_value(Principle_value,Percent_Increase,Payment_Per_Period,Number_Periods,Matches_Per_Period)
    True_Percent = Percent_Increase/100
    string = f"Starting at ${Principle_value} and adding ${Payment_Per_Period} per matching period with a {True_Percent}% increase per year you will have ${Future_Value} after {Number_Periods} years.\n"
    print(string)

def main():
    print("High interest savings:")
    summarize_future_value(100000,5,0,10,4)
    print("Investing:")
    summarize_future_value(100000,8,0,10,4)
    print("High Yield Investing:")
    summarize_future_value(100000,10,0,10,4)
    Num_Years = 35
    Save = future_value_list(890.49,3.95,200,Num_Years,4)
    High_Save = future_value_list(890.49,5,1750,Num_Years,4)
    tInvest = future_value_list(890.49,3.95,1750,Num_Years,4)
    Invest = future_value_list(890.49,8,200,Num_Years,4)
    High_Invest = future_value_list(890.49,8,1750,Num_Years,4)

    #List_to_CSV(Save,"Collect_All.csv")
    #List_to_CSV(Invest,"Invest.csv")
    #List_to_CSV(High_Invest,"High_Invest.csv")

    plt.xlabel("Number of Years")
    plt.ylabel("Dollar Value")
    plt.ticklabel_format(useOffset=False,style="plain")


    plt.plot(tInvest[0],tInvest[1])
    plt.plot(Save[0],Save[1])
    plt.plot(Invest[0],Invest[1])
    plt.plot(High_Invest[0],High_Invest[1])
    plt.plot(High_Save[0],High_Save[1])
    plt.legend(["low_Addition,low_Interest","High_Addition,low_Interest","low_Addition,High_Interest","High_Addition,High_Interest","High_Savings"])
    plt.show()
    input()



main()