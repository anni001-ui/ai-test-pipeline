import os
import random

def prioritize_tests():
    # Check if the folder exists first
    if not os.path.exists("tests"):
        print("Warning: 'tests' folder not found. Creating empty priority list.")
        with open("priority_list.txt", "w") as f:
            pass # Create empty file
        return

    tests = [f for f in os.listdir("tests") if f.startswith("test_")]
    prioritized = sorted(tests, key=lambda x: random.random(), reverse=True)

    with open("priority_list.txt", "w") as f:
        for test in prioritized:
            f.write(test + "\n")

    print("AI prioritization complete:", prioritized)

if __name__ == "__main__":
    prioritize_tests()
