from BST_job_schedule import Node, BST
from datetime import datetime


def print_menu():
    print('Please choose an option from the list blow:')
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to add a job to today's schedule")
    print("Press 3 to remove a job from the schedule")
    print("Press 4 to quit")


def choice():
    while True:
        print_menu()
        try:
            num = int(input("Enter your choice-> "))
        except ValueError:
            print('')
            print("Please re-enter.")
            print('')
        else:
            if 1 <= num <= 4:
                return num
            else:
                print('')
                print("Out of range.")
                print('')


def separation_line():
    print('-'*50)


def get_time():
    while True:
        time_str = input("Enter the time in hh:mm format, example 18:30 or 6:30-> ")
        try:
            time_input = datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print('')
            print("Incorrect time format, should be hh:mm")
        else:
            return time_input.time()


def get_duration():
    while True:
        try:
            duration = int(input("Enter the duration of the job in minutes, example 60-> "))
        except ValueError:
            print("Incorrect format.")
        else:
            return duration


def get_task_name():
    task_name = input("Please enter the name of the task-> ")
    if task_name:
        return task_name


def check_time_exist():
    while True:
        time_ask = get_time()
        node_found = tree.find_val(time_ask)
        if node_found:
            return node_found
        else:
            print('')
            print('Time not found, please enter again.')


def delete_line_in_file(file_name, data):
    with open(file_name,mode="r") as file:
        lines = file.readlines()
    with open(file_name, mode="w") as file:
        for single_line in lines:
            if single_line.split(',')[0] != data.strftime('%-H:%M'):
                file.write(single_line)


if __name__ == "__main__":
    tree = BST()

    with open("data.txt") as myfile:
        for line in myfile:
            tree.insert(line)

    while True:
        num = choice()
        if num == 1:
            print("This is today's scheduled jobs in sorted order:")
            separation_line()
            tree.in_order()
            separation_line()
            go_on = input("Press any key to continue...")
        elif num == 2:
            add_time = get_time().strftime('%-H:%M')
            add_duration = str(get_duration())
            add_task_name = get_task_name()
            key = ','.join([add_time, add_duration, add_task_name])
            tree.insert(key)
            with open('data.txt', mode='a') as f:
                f.write(key)
                f.write('\n')
            go_on = input("Press any key to continue...")
        elif num == 3:
            node_delete = check_time_exist()
            duration_delete = get_duration()
            name_delete = get_task_name()
            if node_delete.name_of_job == name_delete and node_delete.duration == duration_delete:
                print("Deleting completed:")
                print(node_delete)
                delete_line_in_file("data.txt", node_delete.data)
                tree.delete_val(node_delete.data)
                tree.size -= 1
            else:
                print('')
                print('The name and/or duration of job did not match, delete failed')
            go_on = input("Press any key to continue...")
        else:
            print("Exiting program...")
            break





