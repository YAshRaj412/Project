import random

subjects = ["Narendra Modi", "Virat Kohli", "Priyanka Chopra", "Donald Trump", "Nirmala Sitharaman"]
actions = ["found eating gobar", "dancing on", "caught sleeping at", "launches new app for", "arguing with"]
objects = ["the moon", "the Parliament", "a rabbit", "students in Delhi", "a robot"]

def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    
    return f"{subject} {action} {obj}!"

def main():
    print("=============================")
    print(" FAKE NEWS HEADLINES ")
    print("=============================")

    while True:
        try:
            count_input = input("\nHow many headlines do you want to generate? (Enter a number): ")
            
            if not count_input:
                print("Please enter a number.")
                continue 

            count = int(count_input)

            if count <= 0:
                print("Please enter a positive number.")
                continue

            print("\nGenerating Headlines...\n")
            
            for i in range(count):
                print(f"{i+1}. {generate_headline()}")
            
            again = input("\nDo you want to generate more? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("\nThanks for using Fake News Headline Generator!")
                break 

        except ValueError:
            print(f"Error: '{count_input}' is not a valid number. Please enter a number.")

if __name__ == "__main__":
    main()



