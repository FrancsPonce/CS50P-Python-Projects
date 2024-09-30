
def main():
       eating_list= {}

       while True:

                try:
                    item= input().upper()
                    if item in eating_list:
                        eating_list[item] += 1

                    else:
                        eating_list[item] = 1

                except  EOFError:

                        for item_key in sorted(eating_list.keys()):
                                print(eating_list[item_key], item_key)
                        break

main()

