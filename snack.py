import sys

def solve():
    try:
        T = int(sys.stdin.readline().strip())
    except ValueError:
        return

    for _ in range(T):
        n, m = map(int, sys.stdin.readline().strip().split())

        prices = {}
        for i in range(n):
            parts = sys.stdin.readline().strip().split()
            item_name = parts[0]
            s_price = int(parts[1])
            m_price = int(parts[2])
            l_price = int(parts[3])
            prices[item_name] = {
                "small": s_price,
                "medium": m_price,
                "large": l_price
            }

        customer_subtotals = {}
        customer_first_appearance = []

        for i in range(m):
            customer, item, size = sys.stdin.readline().strip().split()

            if customer not in customer_subtotals:
                customer_subtotals[customer] = 0
                customer_first_appearance.append(customer)

            item_cost = prices[item][size]
            customer_subtotals[customer] += item_cost

        K = len(customer_subtotals) 
        shipping_fee = 100 // K

        for customer in customer_first_appearance:
            subtotal = customer_subtotals[customer]
            total_bill = subtotal + shipping_fee
            
            final_bill = total_bill
            
            last_digit = total_bill % 10
            
            if last_digit == 1 or last_digit == 6:
                final_bill = total_bill - 1
            elif last_digit == 4 or last_digit == 9:
                final_bill = total_bill + 1
            
            print(f"{customer} {final_bill}")

solve()
