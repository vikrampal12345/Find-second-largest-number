a=[10,3,18,20,1,90,76]

if len(a) == 0:
    print("Empty list")
else:
    second_largest=a[0]

    for nu in a:
        if nu > second_largest:
            second_0largest=nu

        elif nu > second_largest and nu != second_largest:
            second_largest=nu    

    print(f"second_largest number: {second_largest}")      