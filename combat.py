#benjamin copier combat
choosing_class=True
while choosing_class == True:
    p_class_chosen= input("choose a class: 1 wizard 2 fighter 3 cleric")
    if p_class_chosen== 1 or "wizard":
        print("your a wizard harry")
    elif p_class_chosen== 2 or "fighter":
        print("Fight!!(er)")
        choosing_class = False
    elif p_class_chosen== 3 or "cleric":
        print("its cler(ic) to me")