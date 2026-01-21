import os

# ------------------------------
# NODE CLASS (Linked List)
# ------------------------------
class StudentNode:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


# ------------------------------
# LINKED LIST CLASS
# ------------------------------
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, roll, name, marks):
        new_node = StudentNode(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                return temp
            temp = temp.next
        return None

    def delete(self, roll):
        if self.head is None:
            return False

        if self.head.roll == roll:
            self.head = self.head.next
            return True

        prev = None
        temp = self.head
        while temp:
            if temp.roll == roll:
                prev.next = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def display(self):
        if self.head is None:
            print("\nNo records found.")
            return

        temp = self.head
        print("\n--- Student Records (Sequential Display) ---")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

# ------------------------------
# STACK – Recently added students
# ------------------------------
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, student):
        self.stack.append(student)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def display(self):
        print("\nRecent Added Students (Stack - LIFO):")
        for s in reversed(self.stack):
            print(f"Roll: {s.roll}, Name: {s.name}")


# ------------------------------
# QUEUE – Students waiting for verification
# ------------------------------
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, student):
        self.q.append(student)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)

    def display(self):
        print("\nStudents Waiting for Verification (Queue - FIFO):")
        for s in self.q:
            print(f"Roll: {s.roll}, Name: {s.name}")
# ------------------------------
# FILE HANDLING
# ------------------------------
def save_to_file(linked_list):
    f = open("students.txt", "w")
    temp = linked_list.head
    while temp:
        f.write(f"{temp.roll},{temp.name},{temp.marks}\n")
        temp = temp.next
    f.close()
    print("\nData Saved Successfully!")


def load_from_file(linked_list):
    if not os.path.exists("students.txt"):
        return

    f = open("students.txt", "r")
    for line in f:
        data = line.strip().split(",")
        if len(data) == 3:
            linked_list.insert(data[0], data[1], data[2])
    f.close()
# ------------------------------
# MAIN MENU
# ------------------------------
def main():
    linked_list = LinkedList()
    stack = Stack()
    queue = Queue()

    load_from_file(linked_list)

    while True:
        print("\n==============================")
        print(" STUDENT RECORD SYSTEM (DS)")
        print("==============================")
        print("1. Insert New Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Show Recently Added Students (Stack)")
        print("6. Show Verification Queue")
        print("7. Save & Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")

            linked_list.insert(roll, name, marks)
            stack.push(StudentNode(roll, name, marks))
            queue.enqueue(StudentNode(roll, name, marks))
            print("\nStudent Added Successfully!")

        elif choice == "2":
            roll = input("Enter Roll No to Search: ")
            result = linked_list.search(roll)
            if result:
                print(f"\nFOUND → Roll: {result.roll}, Name: {result.name}, Marks: {result.marks}")
            else:
                print("\nRecord Not Found.")

        elif choice == "3":
            roll = input("Enter Roll No to Delete: ")
            if linked_list.delete(roll):
                print("\nRecord Deleted Successfully.")
            else:
                print("\nRecord Not Found.")

        elif choice == "4":
            linked_list.display()

        elif choice == "5":
            stack.display()

        elif choice == "6":
            queue.display()

        elif choice == "7":
            save_to_file(linked_list)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid Choice! Try Again.")
main()
