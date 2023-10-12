# create a class to list variables of 
class Axolotl: 
    def __init__(animal, arm_length, leg_length, eye_num, has_tail, has_fur):
        animal.arm_length = arm_length
        animal.leg_length = leg_length
        animal.eye_num = eye_num
        animal.has_tail = has_tail
        animal.has_fur = has_fur

# describe animal's characteristics given the function below, 
# along with stating their data type
    def describe(animal): 
        print()
        print("My favorite animal is an axolotl!")
        print()
        print(f"- Arm Length: {animal.arm_length} cm - (Type: {type(animal.arm_length).__name__})")
        print(f"- Leg Length: {animal.leg_length} cm - (Type: {type(animal.leg_length).__name__})")
        print(f"- Number of Eyes: {animal.eye_num} - (Type: {type(animal.eye_num).__name__})")
        print(f"- Does it have a tail?: {'Yes' if animal.has_tail else 'No'} - (Type: {type(animal.has_tail).__name__})")
        print(f"- Is it furry?: {'Yes' if animal.has_fur else 'No'} - (Type: {type(animal.has_fur).__name__})")
        print()

# use the __init__ function that has the parameters and 
# define my_axolotl function along with the respective information
my_axolotl = Axolotl(2.0, 2.0, 2, True, False) 

my_axolotl.describe()

        
