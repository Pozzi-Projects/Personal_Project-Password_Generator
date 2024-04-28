def strength(password_local):
    test = []
    if len(password_local) >= 8:
        test.append(True)
    else:
        test.append(False)

    test.append(False)
    for i in password_local:
        if i.isupper():
            test[1] = True

    test.append(False)
    for i in password_local:
        if i.isdigit():
            test[2] = True

    if all(test):
        return "Strong Password"
    else:
        return "Weak Password"


password = input("enter your password: ")
result = strength(password)

print(result)