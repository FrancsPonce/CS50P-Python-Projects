
def main():
       eating_list= {
                        "Baja Taco": 4.25,
                        "Burrito": 7.50,
                        "Bowl": 8.50,
                        "Nachos": 11.00,
                        "Quesadilla": 8.50,
                        "Super Burrito": 8.50,
                        "Super Quesadilla": 9.50,
                        "Taco": 3.00,
                        "Tortilla Salad": 8.00
                                                    }

       buy_list= []
       total_cost = 0.00

       while True:

                try:
                    c= input("Item: ").lower().title()
                    if c in eating_list:
                            buy_list.append(eating_list[c])
                            total_cost += eating_list[c]
                            print(f"Total: ${total_cost:.2f}")
                    else:
                            print ("Invalid")
                except  EOFError:
                    print("")
                    break



main()

