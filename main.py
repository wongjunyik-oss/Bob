import webbrowser
import os
import time

def menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the screen
    print("---------------------------------")
    print("    RAGDOLL BRAWLER - PERSONAL   ")
    print("---------------------------------")
    print("[1] Play Game (Browser)")
    print("[2] Visit My GitHub Profile")
    print("[3] View Controls")
    print("[4] Exit")
    print("---------------------------------")

    choice = input("Select an option: ")
    
    if choice == '1':
        path = os.path.abspath("index.html")
        webbrowser.open(f"file://{path}")
        print("Launching...")
    elif choice == '2':
        webbrowser.open("https://github.com") # Put your link here!
    elif choice == '3':
        print("\nCONTROLS:\nA/D - Move\nW - Jump\nSpace - Punch (Coming Soon)")
        input("\nPress Enter to return...")
        menu()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    menu()
