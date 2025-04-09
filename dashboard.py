from toolkit import BugHuntingToolkit

def main():
    toolkit = BugHuntingToolkit()
    while True:
        print("\nBug Hunting Toolkit Dashboard")
        print("1. List Tools")
        print("2. Run Tool")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            toolkit.list_tools()
            print("\nWould you like to run a tool from the list? (yes/no)")
            run_choice = input("Enter your choice: ").strip().lower()
            if run_choice == "yes":
                print("\nSelect a category:")
                categories = list(toolkit.tools.keys()) + ["plugin"]
                for idx, category in enumerate(categories, start=1):
                    print(f"{idx}. {category.capitalize()}")
                category_choice = input("Enter the number of the category: ")
                if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
                    print("Invalid category choice. Returning to main menu.")
                    continue
                category = categories[int(category_choice) - 1]

                if category == "plugin":
                    tools = list(toolkit.plugins.keys())
                else:
                    tools = toolkit.tools[category]

                if not tools:
                    print(f"No tools found in category '{category}'.")
                    continue

                print("\nSelect a tool:")
                for idx, tool in enumerate(tools, start=1):
                    print(f"{idx}. {tool}")
                tool_choice = input("Enter the number of the tool: ")
                if not tool_choice.isdigit() or int(tool_choice) not in range(1, len(tools) + 1):
                    print("Invalid tool choice. Returning to main menu.")
                    continue
                tool_name = tools[int(tool_choice) - 1]

                print(f"\nAttempting to run tool '{tool_name}' in category '{category}'...")
                toolkit.run_tool(category, tool_name)
        elif choice == "2":
            print("\nSelect a category:")
            categories = list(toolkit.tools.keys()) + ["plugin"]
            for idx, category in enumerate(categories, start=1):
                print(f"{idx}. {category.capitalize()}")
            category_choice = input("Enter the number of the category: ")
            if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
                print("Invalid category choice. Try again.")
                continue
            category = categories[int(category_choice) - 1]

            if category == "plugin":
                tools = list(toolkit.plugins.keys())
            else:
                tools = toolkit.tools[category]

            if not tools:
                print(f"No tools found in category '{category}'.")
                continue

            print("\nSelect a tool:")
            for idx, tool in enumerate(tools, start=1):
                print(f"{idx}. {tool}")
            tool_choice = input("Enter the number of the tool: ")
            if not tool_choice.isdigit() or int(tool_choice) not in range(1, len(tools) + 1):
                print("Invalid tool choice. Try again.")
                continue
            tool_name = tools[int(tool_choice) - 1]

            print(f"\nAttempting to run tool '{tool_name}' in category '{category}'...")
            toolkit.run_tool(category, tool_name)
        elif choice == "3":
            print("Exiting the dashboard. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
