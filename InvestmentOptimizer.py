import pandas as pd
import numpy as np


class InvestmentOptimizer:
    def __init__(self, investments):
        self.investments = investments

    @staticmethod
    def _optimize_investment_allocation(expected_returns, risks):
        num_investments = len(expected_returns)
        covariance_matrix = np.eye(num_investments) * risks.values()

        # Solve the optimization problem to find the optimal allocation
        optimal_allocation = np.linalg.solve(covariance_matrix, expected_returns.values())

        return optimal_allocation / sum(optimal_allocation)

    def calculate_optimal_allocation(self):
        df = pd.DataFrame.from_dict(self.investments, orient='index')
        optimal_allocation = self._optimize_investment_allocation(df['Expected Return'], df['Risk'])
        df['Optimal Allocation'] = optimal_allocation

        return df


if __name__ == '__main__':
    # Define the investment options and their corresponding expected returns and risks
    investments = {
        'Stocks': {'Expected Return': 0.1, 'Risk': 0.15},
        'Bonds': {'Expected Return': 0.05, 'Risk': 0.08},
        'Cash': {'Expected Return': 0.02, 'Risk': 0.01}
    }

    # Create an instance of the InvestmentOptimizer class
    optimizer = InvestmentOptimizer(investments)

    # Calculate the optimal allocation
    result_df = optimizer.calculate_optimal_allocation()

    # Display the DataFrame
    print(result_df)
