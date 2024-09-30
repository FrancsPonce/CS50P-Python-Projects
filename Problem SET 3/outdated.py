
def main():
        dates=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]



        while True:
            try:
                user_input= input("Date: ")
                if "," in user_input:
                    user_convert= user_input.replace(",", "").strip()
                    M, D, Y= user_convert.split(" ")
                    M = dates.index(M) + 1
                    D = D.rstrip()
                    if int(M) <= 12 and int(D) <32:
                        print (f"{Y}-{M:02}-{int(D):02}")
                        return

                elif "/" in user_input:
                    M, D, Y = user_input.split("/")
                    D= D.rstrip()
                    M= M.rstrip()
                    Y= Y.rstrip()
                    if int(M) <= 12 and int(D)<32:
                        print (f"{Y}-{int(M):02}-{int(D):02}")
                        return

            except ValueError:
                 pass




main()
