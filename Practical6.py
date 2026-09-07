# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(weights, profits, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # Item cannot be included
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]

            # Choose maximum profit
            else:
                exclude = dp[i - 1][w]
                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                dp[i][w] = max(exclude, include)

    # Find selected items
    selected_items = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):

        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:

            selected_items.append(i - 1)
            remaining_capacity -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


# Item details
weights = [2, 3, 4, 5, 1]
profits = [30, 50, 60, 80, 20]
capacity = 7


# Function call
maximum_profit, selected = knapsack(weights, profits, capacity)


# Display result
print("Maximum Profit:", maximum_profit)
print("Selected Item Indexes:", selected)
