import requests

def get_employee_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    done_tasks = [todo for todo in todos if todo["completed"]]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()
    employee_name = employee["name"]

    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

employee_id = int(input("Enter the employee ID: "))
get_employee_todo_list(employee_id)
