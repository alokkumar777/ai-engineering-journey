def resolution_streak(days):
    for day in days:
        if day[0] < 10000 or day[1] > 120 or day[2] < 5:
            return "Resolution failed on day X: N day streak."
        return "Resolution on track: N day streak."

print(resolution_streak([[10500, 75, 15], [11000, 900, 10], [10650, 10, 9]]))