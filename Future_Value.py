
# This is a class I built to help conceptualize all of the data and operations to be performed on it here
class Future_Value():
    # This is a function that you use to set up an object
    def __init__(self,Principle_value:float,Percent_increase:float,Payment_per_period:float,Number_periods:int,Matches_per_period:int) -> None:
        self.Principle_value = Principle_value
        self.Percent_increase = Percent_increase
        self.Payment_per_period = Payment_per_period
        self.Number_periods = Number_periods
        self.Matches_per_period = Matches_per_period
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