

def generate_bill():

    menu = {
        "milk": 30,
        "bread": 45,
        "egg": 6,
        "sugar": 40,
        "rice": 60,
        "tea": 25
    }

    print("\n===== lachoo'S SUPERMARKET =====")

    cart = []
    total_bill = 0

    while True:

        item = input("\nEnter item name ('exit' to bill): ").lower()

        if item == "exit":
            break

        if item in menu:

            qty = int(input("Enter quantity: "))

            price = menu[item]
            amount = qty * price

            total_bill += amount

            cart.append([item, qty, price, amount])

            print("Item added!")

        else:
            print("Item not available!")

    if cart:

        gst = total_bill * 0.18
        final_total = total_bill + gst

        print("\n========== BILL ==========")
        print(f"{'Item':<10}{'Qty':<10}{'Total'}")
        print("-" * 30)

        for item in cart:
            print(f"{item[0]:<10}{item[1]:<10}Rs.{item[3]}")

        print("-" * 30)
        print(f"Subtotal : Rs.{total_bill}")
        print(f"GST 18%  : Rs.{gst}")
        print(f"Total    : Rs.{final_total}")

        print("==========================")

    else:
        print("No items purchased.")


generate_bill()