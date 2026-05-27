from data_handler import add_data, view_data, update_data
from ml_model import train_model, predict_usage

while True:
    print("\nUTILITY USAGE PREDICTION TOOL")
    print("1. Add Usage Data")
    print("2. View Data")
    print("3. Update Data")
    print("4. Train Model")
    print("5. Predict Usage")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            add_data()

        elif choice == "2":
            view_data()

        elif choice == "3":
            update_data()

        elif choice == "4":
            train_model()

        elif choice == "5":
            predict_usage()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)
