
def cashback(amount):
    percent = 0.05
    result = percent * amount
    limit = 3_000
    if result > limit:
        return limit
    return result





