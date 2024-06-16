import numpy as np
from typing import Callable, Dict, Tuple


def func(option: int, x: np.ndarray) -> np.ndarray:
    """
    Function to integrate based on the selected option.

    Parameters:
    option (int): The selected option.
    x (np.ndarray): Array of values to evaluate the function.

    Returns:
    np.ndarray: Evaluated function values.
    """
    if option == 1:
        return np.exp(x ** 2)
    elif option == 2:
        return np.exp(x) * 4
    elif option == 3:
        return (1 - np.exp(x ** 2)) ** 0.5
    elif option == 4:
        return x * (1 + x ** 2) ** -2
    elif option == 5:
        return np.exp(x + x ** 2)
    elif option == 6:
        return np.exp(-x)
    elif option == 7:
        return (1 - x ** 2) ** 1.5
    else:
        raise ValueError("Invalid option")


def monte_carlo_integration(a: float, b: float, N: int, option: int) -> float:
    """
    Perform Monte Carlo integration.

    Parameters:
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    N (int): Number of samples.
    option (int): The selected option for the function to integrate.

    Returns:
    float: Estimated value of the integral.
    """
    if np.isinf(b):
        # Handle improper integrals with a change of variables
        samples = np.random.exponential(1, N)
        # Adjust the weights for the exponential distribution
        evaluations = func(option, samples) * np.exp(-samples)
        integral = np.mean(evaluations)
    else:
        # Generate N random samples between a and b
        samples = np.random.uniform(a, b, N)
        # Evaluate the function at all sample points
        evaluations = func(option, samples)
        # Calculate the integral
        integral = (b - a) * np.mean(evaluations)
    return integral


def main():
    """
    Main function to execute the integration based on user input.
    """
    # Dictionary of theoretical values and limits
    integration_data = {
        # No simple theoretical value
        1: {"a": 0, "b": 1, "theorycal_value": None},
        2: {"a": -1, "b": 1, "theorycal_value": 4 * (np.e - 1/np.e)},
        # No simple theoretical value
        3: {"a": 0, "b": 1, "theorycal_value": None},
        4: {"a": 0, "b": np.inf, "theorycal_value": 0.5},
        # No simple theoretical value
        5: {"a": 0, "b": 1, "theorycal_value": None},
        6: {"a": 0, "b": np.inf, "theorycal_value": 1},
        7: {"a": 0, "b": 1, "theorycal_value": 0.583164852}
    }

    # Menu options
    print("[ MONTE CARLO METHOD ]")
    print("1. Integral of e(x^2) from 0 to 1")
    print("2. Integral of e(x) * 4 from -1 to 1")
    print("3. Integral of (1 - e(x^2))^0.5 from 0 to 1")
    print("4. Integral of x * (1 + x^2)^-2 from 0 to inf")
    print("5. Integral of e^(x + x^2) from 0 to 1")
    print("6. Integral of e^-x from 0 to inf")
    print("7. Integral of (1 - x^2)^1.5 from 0 to 1")

    # User input for the option
    option = int(input("\n> Your option: "))

    if option not in integration_data:
        print("\n> Invalid option.")
        return

    # Retrieve limits and theoretical value based on the option
    data = integration_data[option]
    a = data["a"]
    b = data["b"]
    theoretical_value = data["theorycal_value"]

    # Number of samples
    N = 1000000

    # Calculate the integral using Monte Carlo integration
    calculated_value = monte_carlo_integration(a, b, N, option)

    # Calculate the percentage error and round to 4 decimal places
    if theoretical_value is not None:
        error = abs((calculated_value - theoretical_value) /
                    theoretical_value) * 100
        error = round(error, 4)
    else:
        error = None

    # Print the results
    print(f'\n> The theoretical value is {theoretical_value}')
    print(
        f'> The value calculated by Monte Carlo integration is {calculated_value}')
    if error is not None:
        print(f'> The error is {error}%\n')
    else:
        print(f'> No theoretical value provided for error calculation.\n')


if __name__ == "__main__":
    main()
