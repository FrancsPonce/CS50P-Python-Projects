    # "A very BAD Delfos Oracle"
    #### Video Demo:  https://www.youtube.com/watch?v=scN5MobNt_g
    #### Description:

    # FIRST AND GENERAL

    My project is called "A very BAD Delfos Oracle," which is simple and seeks to have the user interact with the code to receive a particular piece of advice from this mysterious oracle. It can work in either English or Spanish by running a command-line argument, and it can generate up to one hundred sixty thousand different answers.

    ## DATABASE EXPLANATION
    To run our code, we have two databases containing different words. One of the databases is in English and the other in Spanish. Each database is structured with comma-separated values, making it easier for us to read these files with a DictReader. Each column of our dictionary in the databases consists of four indices: index0, index1, index2, and index3.

    Index0: Introduction or suggestion.
    Index1: Action or verb.
    Index2: Object of the action.
    Index3: Context or manner.


    ### Funct ARGV EXPLANATION

    After understanding the databases, we need to understand our function_argv, which asks the user to input the language in which the code will work, allowing them to choose between English or Spanish. If neither language is chosen, a sys.exit will be generated, informing that one of the two languages must be chosen. This function will return a string that could be "EN" for English or "ES" for Spanish.

    ### Funct CSV EXPLANATION

    Next, our function_csv will take the database with the information we have organized in list dictionaries and will decide whether to open the database with words in Spanish or in English, depending on the string value returned by our last function. After checking the language to be used, it will open the file and store our information in four different lists.

    ### Funct RANDOMIZER EXPLANATION

    Last but not least, these lists will be iterated with the random module in the function_randomizer, where it will take each of the lists and randomly select a value from each. With the chosen values, it will generate the return of the string, which would be the random advice from our oracle.

    ### MAIN()

    All this will culminate in our MAIN function, which will check which language was chosen to work the input in Spanish or English and will give us the advice if we say yes. If we say no, the program will close. If we do not give a valid answer, the program will ask again for a yes or no response.
