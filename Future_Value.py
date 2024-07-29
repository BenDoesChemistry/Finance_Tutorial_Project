
# This is a class I built to help conceptualize all of the data and operations to be performed on it here
class Future_Value():
    # This is a function that you use to set up an object
    def __init__(self,Principle_value:float,Percent_increase:float,Payment_per_period:float,Number_periods:int,Matches_per_period:int) -> None:
        self.Principle_value = Principle_value
        self.Percent_increase = Percent_increase
        self.Payment_per_period = Payment_per_period
        self.Number_periods = Number_periods
        self.Matches_per_period = Matches_per_period
        self.Total_contribution = Matches_per_period * Number_periods * Payment_per_period
        self.Time_List = [0]
        self.Future_value_list = []
        self._calc_values()
        self.Future_value = self.get_future_value()


    # Not to be used outside of the class. This is what creates the Future_value_list and Time_List lists
    def _calc_values(self):
        accumulator = self.Principle_value
        self.Future_value_list.append(accumulator)
        for i in range(self.Number_periods*self.Matches_per_period):
            self.Time_List.append(i/self.Matches_per_period + 1/self.Matches_per_period)
            accumulator = accumulator + self.Payment_per_period
        # Apply interest for the interest period
            accumulator = accumulator * (1 + (self.Percent_increase / (100*self.Matches_per_period)))
            self.Future_value_list.append(round(accumulator,2))
        
    # Returns a list of value for graphing
    def get_future_values(self):
        return self.Future_value_list
    # Returns a single value at the end of the time period
    def get_future_value(self):
        return self.Future_value_list[-1]
    # Returns a list of time values that correspond to the values list.
    def get_time_range(self):
        return self.Time_List
    # Returns a string with the needed information. This string format is called an f-string
    def get_summary(self):
        string = f"Starting at ${self.Principle_value} and adding ${self.Payment_per_period} per matching period with a {self.Percent_increase}% increase per year for {self.Number_periods} years you will have ${self.Future_value}."
        return string
    

    # This section will only run if this file is being run directly, not if it is imported somewhere.
if __name__ == "__main__":
    Number_of_years = 35

    High_Interest_Savings = Future_Value(895,5,250,Number_of_years,4)

    print(High_Interest_Savings.get_summary())

    print(len(High_Interest_Savings.get_future_values()))
    print(len(High_Interest_Savings.get_time_range()))
    print(High_Interest_Savings.get_time_range())



class Debt_Payoff:
    # Note that the owed ammount should be passed in as a positive float and it is converted to a negative float later to indicate debt
    def __init__(self,Owed_amount:float,Percent_interest:float,Payment_per_period:float,Matches_per_period:int):
        self.Owed_amount = Owed_amount * -1
        self.Values = [Owed_amount * -1]
        self.Time_List = [0]
        self.Percent_interest = Percent_interest
        self.Payment_per_period = Payment_per_period
        self.Matches_per_period = Matches_per_period
        self.Periods = 0.0
        self.Total_contribution = 0.0

        self._calc_debt()

    def _calc_debt(self):
        Owed_accumulator = self.Owed_amount
        rate_of_increase = 1 + (self.Percent_interest * .01) / self.Matches_per_period
        rate_of_time = 1 / self.Matches_per_period
        Time_Stamp = 0

        # This handles the case where the ammount owed will not go down or will stay constant.
        if rate_of_increase * self.Owed_amount  >= self.Payment_per_period:
            print("This will never be paid off. Increase the Payed ammount.")
            return None

        while Owed_accumulator < 0:
            Owed_accumulator = Owed_accumulator + self.Payment_per_period
            Owed_accumulator = Owed_accumulator * rate_of_increase
            Time_Stamp = Time_Stamp + rate_of_time
            self.Time_List.append(Time_Stamp)
            self.Values.append(Owed_accumulator)
            self.Total_contribution = self.Total_contribution + self.Payment_per_period
            self.Periods = self.Periods + rate_of_increase
