

class Future_Value():

    def __init__(self,Principle_value:float,Percent_increase:float,Payment_per_period:float,Number_periods:int,Matches_per_period:int) -> None:
        self.Principle_value = Principle_value
        self.Percent_increase = Percent_increase
        self.Payment_per_period = Payment_per_period
        self.Number_periods = Number_periods
        self.Matches_per_period = Matches_per_period
        self.Values = self.get_future_value_list()
        pass

    def get_future_value_list(self):
        accumulator = self.Principle_value
        value_list = []
        value_list.append(accumulator)
        for i in range(self.Number_periods*self.Matches_per_period):
            accumulator = accumulator + self.Payment_per_period
        # Apply interest for the interest period
            accumulator = accumulator * (1 + (self.Percent_increase / (100*self.Matches_per_period)))
            value_list.append(accumulator)
        return value_list
