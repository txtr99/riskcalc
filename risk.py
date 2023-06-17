# Import necessary modules
from termcolor import colored


def main():
    """Main function to gather user input and perform calculations."""

    # Starting off with getting all the necessary inputs.
    entry_price = float(input(colored('Enter the entry price: ', 'cyan')))
    stoploss_price = float(input(colored('Enter the stoploss price: ', 'cyan')))
    direction = input(colored('Enter the direction (Long/Short): ', 'cyan'))
    account_balance = float(
        input(colored('Enter Account Balance in $ (default 100,000): ', 'cyan')) or 100000
    )
    risk_percent = float(
        input(colored('Enter % of balance to RISK for the trade (default 0.5%): ', 'cyan')) or 0.5
    )
    fee_percent = 0.03  # fee percent on each end (entry and exit)

    # Let's check how many TP targets the user wants
    num_tp_targets = int(input(colored('Enter number of TP targets (1-3): ', 'cyan')))

    # Initialize the TP prices and percentages
    tp_prices = []
    tp_percents = []

    # Ask the user for each TP target's price and percent
    for i in range(num_tp_targets):
        tp_price = float(input(colored(f'Enter TP{i+1} price (default {i+1}R): ', 'cyan')) or i+1)
        tp_percent = float(
            input(colored(f'Enter TP{i+1} % of position (default {50 if i==0 else 25}%): ', 'cyan')) or (50 if i==0 else 25)
        )
        tp_prices.append(tp_price)
        tp_percents.append(tp_percent)

    # Alright, time for some math. Let's first calculate the risk in dollars.
    risk_in_dollars = account_balance * risk_percent / 100

    # 'r' is our risk in terms of price movement.
    r = abs(entry_price - stoploss_price)

    # The size of our position is simply the risk in dollars divided by 'r'.
    position_size = risk_in_dollars / r

    # Our maximum loss is just the risk in dollars.
    max_loss_dollars = risk_in_dollars

    # The maximum position size is just the position size we calculated earlier.
    max_position_size = position_size

    # Now let's calculate the maximum gain if all TP's are hit and the corresponding R values.
    max_gain_dollars = 0
    expected_pnls = []
    r_values = []
    for i in range(num_tp_targets):
        pnl = position_size * (tp_prices[i] - entry_price) * (tp_percents[i] / 100)
        # Subtract the fees
        pnl = pnl * (1 - fee_percent / 100) ** 2
        max_gain_dollars += pnl
        expected_pnls.append(pnl)
        r_values.append(abs((tp_prices[i] - entry_price) / r))

    # If the trade direction is short, we should invert the gain.
    if direction.lower() == "short":
        max_gain_dollars *= -1

    # Time to print out all the results!
    print(colored('\nMaximum Loss in $: ', 'green'), max_loss_dollars, " and ", (max_loss_dollars / account_balance * 100), "% of account")
    print(colored('Max Position Size allowed: ', 'green'), max_position_size)
    print(colored('Maximum Gain in $ if all TP\'s are hit: ', 'green'), max_gain_dollars)
    for i in range(num_tp_targets):
        print(colored(f'TP{i+1} R value (times risk profit): ', 'green'), r_values[i])
        print(colored(f'Expected PNL for TP{i+1}: ', 'green'), expected_pnls[i])


# Call the main function
if __name__ == "__main__":
    main()
