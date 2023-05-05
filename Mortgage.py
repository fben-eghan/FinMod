class Mortgage:
    def __init__(self, principal, interest_rate, term, amortization, down_payment):
        self.principal = principal - down_payment
        self.interest_rate = interest_rate
        self.term = term
        self.amortization = amortization
        self.monthly_interest_rate = interest_rate / 12
        self.months = term * 12
        self.monthly_payment = self.calculate_monthly_payment()
    
    def calculate_monthly_payment(self):
        r = self.monthly_interest_rate
        n = self.months
        p = self.principal
        monthly_payment = (r * p) / (1 - (1 + r)**(-n))
        return monthly_payment
    
    def total_interest(self):
        total_interest = (self.monthly_payment * self.months) - self.principal
        return total_interest

class BuyToLetMortgage(Mortgage):
    def __init__(self, property_value, deposit_percent, mortgage_rate, rental_income, extra_payment=0):
        deposit_amount = property_value * deposit_percent
        mortgage_amount = property_value - deposit_amount
        super().__init__(mortgage_amount, mortgage_rate, 25, 25, 0)
        self.rental_income = rental_income
        self.extra_payment = extra_payment
    
    @property
    def property_value(self):
        return self.principal / 0.8
    
    @property
    def deposit_amount(self):
        return self.property_value * 0.2
    
    @property
    def mortgage_amount(self):
        return self.principal
    
    @property
    def monthly_mortgage_payment(self):
        return self.monthly_payment
    
    @property
    def monthly_rental_income(self):
        return self.rental_income
    
    @property
    def monthly_net_cash_flow(self):
        return [self.rental_income - self.monthly_payment - self.extra_payment for _ in range(self.term * 12)]
    
    @property
    def annual_return_on_investment(self):
        total_income = sum(self.monthly_net_cash_flow) * 12
        property_value_increase = self.property_value * 0.02 * self.term
        total_investment = self.deposit_amount
        return (total_income + property_value_increase - total_investment) / total_investment

if __name__ == '__main__':
    # create a BuyToLet instance
    bt = BuyToLetMortgage(property_value=500000, deposit_percent=0.2, mortgage_rate=0.03, rental_income=3000)

    # print out the results
    print("Property value:", bt.property_value)
    print("Deposit amount:", bt.deposit_amount)
    print("Mortgage amount:", bt.mortgage_amount)
    print("Monthly mortgage payment:", bt.monthly_mortgage_payment)
   
