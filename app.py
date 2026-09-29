from calculator import add, subtract, multiply, divide


# Simple in-memory task storage
tasks = {}


def delete_task(task_id):
    """
    Delete a task by ID.
    
    Args:
        task_id: The ID of the task to delete
        
    Returns:
        A tuple containing (success: bool, message: str)
    """
    if task_id in tasks:
        del tasks[task_id]
        return True, f"Task {task_id} deleted successfully"
    else:
        return False, f"Task {task_id} not found"


def main():
    print("GitHub Enterprise Cloud Demo")
    print("--------------------------------")

    a = 20
    b = 5

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")


if __name__ == "__main__":
    main()
