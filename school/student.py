# student.py


def add_student(name):
    print(f"👩‍🎓 Student {name} added.")


def remove_student(name):
    print(f"❌ Student {name} removed.")


# # Define what should be imported when using *
__all__ = ["add_student"]
