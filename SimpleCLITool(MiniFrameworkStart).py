def menu():
    print("1. Port Scan")
    print("2. DNS Lookup")
    print("3. HTTP Check")

menu()
choice = input("Select: ")

if choice == "1":
    print("Run port scanner script here")
elif choice == "2":
    print("Run DNS script here")
elif choice == "3":
    print("Run HTTP script here")
