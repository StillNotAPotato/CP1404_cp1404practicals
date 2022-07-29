def main():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928

    print("Electricity bill estimator 2.0")
    tariff = "Which tariff? 11 or 31: "
    tariff_choice = int(input(tariff))
    daily_use_in_kwh = float(input("Enter daily use: "))
    number_of_billing_days = int(input("Enter number of billing days: "))

    if tariff_choice == 11:
        bill = (TARIFF_11 * daily_use_in_kwh * number_of_billing_days)

    elif tariff_choice == 31:
        bill = (TARIFF_31 * daily_use_in_kwh * number_of_billing_days)

    # outputs
    # bill = (cents_per_kwh * daily_use_in_kwh * number_of_billing_days) / 100
    print("Estimated bill: ${:.2f}".format(bill))


main()
