import subprocess
from example_plugin import ExamplePlugin

class BugHuntingToolkit:
    def __init__(self):
        self.tools = {
            "static_analysis": ["SonarQube", "ESLint", "Bandit"],
            "dynamic_analysis": ["Valgrind", "GDB"],
            "fuzzing": ["AFL", "LibFuzzer"],
            "monitoring": ["Sentry", "ELK Stack"],
            "api_testing": ["Postman", "Insomnia"]
        }
        self.plugins = {"example_plugin": ExamplePlugin()}

    def run_tool(self, category, tool_name):
        if tool_name in self.plugins:
            print(f"Running plugin: {tool_name}...")
            self.plugins[tool_name].run()
            return

        if tool_name not in self.tools.get(category, []):
            print(f"Tool {tool_name} not found in category {category}.")
            return

        print(f"Running {tool_name} from category {category}...")
        try:
            # Placeholder logic for running tools
            if category == "static_analysis":
                if tool_name == "SonarQube":
                    subprocess.run(["echo", "Running SonarQube analysis..."])
                elif tool_name == "ESLint":
                    subprocess.run(["echo", "Running ESLint..."])
                elif tool_name == "Bandit":
                    subprocess.run(["echo", "Running Bandit for Python security analysis..."])
            elif category == "dynamic_analysis":
                if tool_name == "Valgrind":
                    subprocess.run(["echo", "Running Valgrind..."])
                elif tool_name == "GDB":
                    subprocess.run(["echo", "Running GDB debugger..."])
            elif category == "fuzzing":
                if tool_name == "AFL":
                    subprocess.run(["echo", "Running AFL fuzzing tool..."])
                elif tool_name == "LibFuzzer":
                    subprocess.run(["echo", "Running LibFuzzer..."])
            elif category == "monitoring":
                if tool_name == "Sentry":
                    subprocess.run(["echo", "Monitoring with Sentry..."])
                elif tool_name == "ELK Stack":
                    subprocess.run(["echo", "Monitoring with ELK Stack..."])
            elif category == "api_testing":
                if tool_name == "Postman":
                    subprocess.run(["echo", "Testing APIs with Postman..."])
                elif tool_name == "Insomnia":
                    subprocess.run(["echo", "Testing APIs with Insomnia..."])
            else:
                print(f"No execution logic defined for tool {tool_name} in category {category}.")
        except Exception as e:
            print(f"An error occurred while running {tool_name}: {e}")

    def list_tools(self):
        for category, tools in self.tools.items():
            print(f"{category.capitalize()}: {', '.join(tools)}")
        print("Plugins: " + ", ".join(self.plugins.keys()))
