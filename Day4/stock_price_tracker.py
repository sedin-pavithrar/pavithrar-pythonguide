# You have a list of stock prices for 30 days, and the program answers three questions:

# When should I buy and sell to make the highest profit?
# What is the average stock price over a fixed number of days?
# Which week had the biggest price fluctuations?

class StockPriceTracker:

    def __init__(self, prices): # runs automatically when a object is created
        self.prices = prices # stores the list prices inside the object 

    def find_max_profit(self):
        min_price = self.prices[0]
        min_day = 0 

        max_profit = 0
        buy_day = 0
        sell_day = 0

        for day in range(1, len(self.prices)):

            profit = self.prices[day] - min_price
#  updating the profit
            if profit > max_profit:
                max_profit = profit
                buy_day = min_day
                sell_day = day
#updating the price 
            if self.prices[day] < min_price:
                min_price = self.prices[day]
                min_day = day

        print(f" Best Buy : Day {buy_day+1} @ Rs.{self.prices[buy_day]} ")
        print(f" Best Sell: Day {sell_day+1} @ Rs.{self.prices[sell_day]} ")
        print(f" Max Profit: Rs.{max_profit}/share")
# finding average price for about some days 
    def moving_average(self, window):

        for i in range(len(self.prices) - window + 1): # 30-6+1 = 25

            avg = sum(self.prices[i:i+window]) / window # sum/6

            print(f"Window {i+1} (Day {i+1}-{i+window}): {avg:.2f}")

    def most_fluctuated_week(self):
        max_swing = -1
        start_day = 0
        for i in range(len(self.prices) - 6):

            week = self.prices[i:i+7]

            high = max(week)
            low = min(week)

            swing = high - low

            if swing > max_swing:
                max_swing = swing
                start_day = i
                best_high = high
                best_low = low

        print(
            f" Week: Days {start_day+1}-{start_day+7} | "
            f" High: {best_high} | Low: {best_low} | "
            f" Swing: {max_swing} "
        )

def main():
    prices = [
        420,425,430,440,435,428,430,
        445,450,448,455,460,458,462,
        470,475,410,420,430,440,450,
        490,470,460,377,390,410,430,
        440,450
    ]

    tracker = StockPriceTracker(prices) 

    print(" === Maximum Profit === ")
    tracker.find_max_profit()

    print("\n === Moving Averages ===")
    tracker.moving_average(7)

    print("\n === Most Volatile Week ===")
    tracker.most_fluctuated_week()


if __name__ == "__main__":
    main()