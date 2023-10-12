class Axolotl: #create a class to list variables of 
    def __init__(animal, arm_length, leg_length, eye_num, has_tail, has_fur):
        animal.arm_length = arm_length
        animal.leg_length = leg_length
        animal.eye_num = eye_num
        animal.has_tail = has_tail
        animal.has_fur = has_fur

    def describe(animal): #describing animal's characteristics
        print()
        print("My favorite animal is an axolotl!")
        print()
        print("\033[4mAxolotl Description:\033[0m")
        print(f"- Arm Length: {animal.arm_length} cm")
        print(f"- Leg Length: {animal.leg_length} cm")
        print(f"- Number of Eyes: {animal.eye_num}")
        print(f"- Does it have a tail?: {'Yes' if animal.has_tail else 'No'}")
        print(f"- Is it furry?: {'Yes' if animal.has_fur else 'No'}")
        print()

my_axolotl = Axolotl(2, 2, 2, True, False)

my_axolotl.describe()

        
