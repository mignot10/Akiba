def calculate_tier_charges(units: float):

    tier1_cost = min(units, 50) * 0.50
    tier2_cost = min(max((units - 50), 0), 100) * 0.75
    tier3_cost = max(units - 150, 0) * 1.20

    return {
        "first_50": tier1_cost,
        "next_100":tier2_cost,
        "above_150":tier3_cost
    }

def calculate_total(units, service_fee=0):

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)
    total = sum(charges.values()) + service_fee

    return total

def generate_summary(units, service_fee=0):
    charges = calculate_tier_charges(units)
    total = calculate_total(units, service_fee)

    return {
        "units_consumed": units,
        "first_50_units_charge": charges["first_50"],
        "next_100_units_charge": charges["next_100"],
        "above_150_units_charge": charges["above_150"],
        "service_fee": service_fee,
        "total_bill": total
    }

units = float(input("Enter units consumed: "))

print(generate_summary(units))