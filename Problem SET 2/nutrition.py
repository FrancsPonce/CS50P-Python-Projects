

def main():
     User= input("Item : ").lower()
     User_calories = workfunct(User)
     if User_calories is not None:
        print(f"Calories : {User_calories}")
     else:
        ""



def workfunct(x):

        for _ in fruit_calories:
            if x in fruit_calories:
                #print(fruit_calories[x])
                return fruit_calories[x]
            else:
                return None

fruit_calories={"apple":130,"avocado":50,"banana":110,"cantaloupe":50,"grapefruit":60,"grapes":90,"honeydew melon":50,"kiwifruit":90,"lemon":15,"lime":20,"nectarine":60,"orange":80,"peach":60,"pear":100,"pineapple":50,"plums":70,"strawberries":50,"sweet cherries":100,"tangerine":50,"watermelon":80}

main()

