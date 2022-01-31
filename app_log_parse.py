#! python3

#open files
#concatenate files
#parse out faults
#count fault instances
#python3
#
import glob

menu = """
================
File Reader v1.3
================

1: Concatenate Files (Run First)
2: Class D Buffer Full
3: 746 Faults
4: Wheel Slide Detected
5: Manual Fault Finder
6: Log Search
7: Exit
"""
done = False

while not done:

    print(menu)
    selection = input("Select what you would like to do: ")
    print()

    if selection == '7': # Exit program
        done = True

    elif selection == '1': # Concatenate Files

        files = []
        files = glob.glob('app.*.log')

        o = open('output.txt', 'w')

        for filename in files:
            with open(filename) as f:
                o.write(f.read())


    elif selection == '2': # Class D Buffer Full faults
        users1 = {}

        with open("output.txt") as text_file:
            for line in text_file:
                if "Class D Buffer" in line:
                    start = line.find("")
                    end = line.find("\n")
                    line = line.strip()
                    line_p = line[ start : end ]
                    if line_p not in users1:
                        users1[line_p] = 1
                    else:
                        users1[line_p] +=1



            with open("ClassD_Fault.txt", "a") as out_file:
                for user,val in users1.items():
                    out_file.writelines('{} logged {} of times.\n'.format(user,val))


    elif selection == '3': # 746 faults
        users1 = {}

        with open("output.txt") as text_file:
            for line in text_file:
                if "0x0746" in line:
                    start = line.find("0x0746")
                    end = line.find("\n")
                    line = line.strip()
                    line_p = line[ start : end ]
                    if line_p not in users1:
                        users1[line_p] = 1
                    else:
                        users1[line_p] +=1



            with open("746_Faults.txt", "a") as out_file:
                for user,val in users1.items():
                    out_file.writelines('{} logged {} of times.\n'.format(user,val))

    elif selection == '4': # Wheel Slide Detected
        users1 = {}

        with open("output.txt") as text_file:
            for line in text_file:
                if "Wheel Slide detected" in line:
                    start = line.find("WARN:")
                    end = line.find("\n")
                    line = line.strip()
                    line_p = line[ start : end ]
                    if line_p not in users1:
                        users1[line_p] = 1
                    else:
                        users1[line_p] +=1



            with open("Wheel_Slide.txt", "a") as out_file:
                for user,val in users1.items():
                    out_file.writelines('{} logged {} of times.\n'.format(user,val))


    elif selection == '5': # fault finder
        users1 = {}
        fault1 = input("""Please enter the fault in question
(i.e. 746): """)

        with open("output.txt") as text_file:
            for line in text_file:
                if "0x0{}".format(fault1) in line:
                    start = line.find()
                    end = line.find("\n")
                    line = line.strip()
                    line_p = line[ start : end ]
                    if line_p not in users1:
                        users1[line_p] = 1
                    else:
                        users1[line_p] +=1



            with open("{}_Faults.txt".format(fault1), "a") as out_file:
                for user,val in users1.items():
                    out_file.writelines('{} logged {} of times.\n'.format(user,val))


    elif selection == '6': # random search
        users1 = {}
        fault1 = input("""Please enter the language you are searching for: """)

        with open("output.txt") as text_file:
            for line in text_file:
                if "{}".format(fault1) in line:
                    start = line.find("")
                    end = line.find("\n")
                    line = line.strip()
                    line_p = line[ start : end ]
                    if line_p not in users1:
                        users1[line_p] = 1
                    else:
                        users1[line_p] +=1

            with open("{}_Search.txt".format(fault1), "a") as out_file:
                for user,val in users1.items():
                    out_file.writelines('{} logged {} of times.\n'.format(user,val))

    else:
        print("{} is not a valid selection.".format(selection))
        print("Please select an avaialable option.")
