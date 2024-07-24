

class Future_Value():

    def __init__(self,Principle_value:float,Percent_increase:float,Payment_per_period:float,Number_periods:int,Matches_per_period:int) -> None:
        self.Principle_value = Principle_value
        self.Percent_increase = Percent_increase
        self.Payment_per_period = Payment_per_period
        self.Number_periods = Number_periods
        self.Matches_per_period = Matches_per_period
        self.Time_List = [0]
        self.Values = []
        self._calc_values()
        self.Future_value = self.get_future_value()

    def _calc_values(self):
        accumulator = self.Principle_value
        self.Values.append(accumulator)
        for i in range(self.Number_periods*self.Matches_per_period):
            self.Time_List.append(i/self.Matches_per_period + 1/self.Matches_per_period)
            accumulator = accumulator + self.Payment_per_period
        # Apply interest for the interest period
            accumulator = accumulator * (1 + (self.Percent_increase / (100*self.Matches_per_period)))
            self.Values.append(round(accumulator,2))
        
    
    def get_future_values(self):
        return self.Values
    
    def get_future_value(self):
        return self.Values[-1]
    
    def get_time_range(self):
        return self.Time_List

    def get_summary(self):
        string = f"Starting at ${self.Principle_value} and adding ${self.Payment_per_period} per matching period with a {self.Percent_increase}% increase per year for {self.Number_periods} years you will have ${self.Future_value}."
        return string
    
if __name__ == "__main__":
    Number_of_years = 35

    High_Interest_Savings = Future_Value(895,5,250,Number_of_years,4)

    print(High_Interest_Savings.get_summary())

    print(len(High_Interest_Savings.get_future_values()))
    print(len(High_Interest_Savings.get_time_range()))
    print(High_Interest_Savings.get_time_range())