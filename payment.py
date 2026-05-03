def process_payment(amount):
    if amount > 10000:
        return "Limit exceeded"
    return f"Processing payment of {amount}"
