# this program creates a Bumblebee class.

import insecta

def main():
    # Create an object from the Bumblebee class.
    working_bumblebee = insecta.Bumblebee('Worker', 'nectar', 'multiple')
    meadow_grasshopper = insecta.Grasshopper('Meadow', 'ants', 30)

    # Display the bumblebee's data.
    print('Type: ', working_bumblebee.get_type())
    print('Eat: ', working_bumblebee.get_eat())
    print('Sting: ', working_bumblebee.get_sting())
    print()
    # Display the grasshopper's data.
    print('Type: ', meadow_grasshopper.get_type())
    print('Eat: ', meadow_grasshopper.get_eat())
    print(f'Jump: {meadow_grasshopper.get_jump()} inches')

main()