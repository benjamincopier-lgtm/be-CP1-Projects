# Benjamin copier Shopping List Manager
shopping_list=[]
while True:
    action = input("what would you like to do, 1 would you like to add to your shopping list, 2 would you like to remove, or 3 would you like to exit your code (the three keywords that you can choose from are 1 add, 2 remove, 3 exit.): ")
    if action== "add":
        new_list= input("what would you like to add to your list: ")
        shopping_list.append(new_list)
        print("your shopping list is:")
        print(*shopping_list)
        set(shopping_list)
        list(shopping_list)
    elif action == "remove":
        new_list=input("what would you like to remove: ")
        if new_list in shopping_list:
            shopping_list.remove(new_list)
            set(shopping_list)
            list(shopping_list)
            print("your shopping list is:")
            print(*shopping_list)
        else:
            print("that isn't real try again.")
    elif action == "exit":
        break
