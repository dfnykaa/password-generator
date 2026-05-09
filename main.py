import generator

def run():
    print("Welcome to the Password Generator!")
    
    while True:
        print("\n1. Generate & Save Password")
        print("2. Exit")
        choice = input("Select option: ")
        
        if choice == "1":
            acc = input("Enter account name: ")
            size = input("Enter length (press Enter for 16): ")
            
            size = int(size) if size.isdigit() else 16
            
            pwd = generator.create_password(size)
            generator.save_password(acc, pwd)
            
            print(f"\nDONE! Password for {acc}: {pwd}")
            print("Saved to passwords.txt")
            
        elif choice == "2":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run()