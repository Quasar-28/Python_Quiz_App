import random

print('Welcome to The Quiz Game')
print('-'*40)

topics = [
    {
        "topic": "System Design",
        "data": [
            {
                "question": "What is the primary purpose of a load balancer in a system design?",
                "options": [
                    "To store data",
                    "To distribute incoming traffic across servers",
                    "To handle security authentication",
                    "To replicate databases"
                ],
                "answer": "To distribute incoming traffic across servers"
            },
            {
                "question": "What is a CDN (Content Delivery Network) used for?",
                "options": [
                    "Reducing latency and delivering content faster",
                    "Encrypting user data",
                    "Storing backup files",
                    "Analyzing user behavior"
                ],
                "answer": "Reducing latency and delivering content faster"
            },
            {
                "question": "What is the primary benefit of using caching in system design?",
                "options": [
                    "Improved database schema",
                    "Faster access to frequently used data",
                    "Secure data encryption",
                    "Increased system downtime"
                ],
                "answer": "Faster access to frequently used data"
            },
            {
                "question": "What does horizontal scaling in a system mean?",
                "options": [
                    "Adding more CPU or memory to a single server",
                    "Adding more servers to handle increased load",
                    "Replacing old servers with new ones",
                    "Optimizing server configurations"
                ],
                "answer": "Adding more servers to handle increased load"
            }
        ]
    },
    {
        "topic": "Data Structures",
        "data": [
            {
                "question": "Which data structure is used for breadth-first search (BFS) in a graph?",
                "options": ["Stack", "Queue", "Heap", "Hash Table"],
                "answer": "Queue"
            },
            {
                "question": "What is the time complexity of searching for an element in a balanced binary search tree (BST)?",
                "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
                "answer": "O(log n)"
            },
            {
                "question": "Which data structure is used to perform recursion?",
                "options": ["Queue", "Array", "Stack", "Tree"],
                "answer": "Stack"
            },
            {
                "question": "What is a circular queue?",
                "options": [
                    "A queue where the last position is connected to the first",
                    "A queue with unlimited size",
                    "A queue implemented using a tree",
                    "A queue that uses two stacks"
                ],
                "answer": "A queue where the last position is connected to the first"
            }
        ]
    },
    {
        "topic": "DBMS",
        "data": [
            {
                "question": "What does ACID stand for in database management systems?",
                "options": [
                    "Authentication, Control, Isolation, Distribution",
                    "Atomicity, Consistency, Isolation, Durability",
                    "Accessibility, Capacity, Integration, Dependency",
                    "Accuracy, Completeness, Integration, Data Integrity"
                ],
                "answer": "Atomicity, Consistency, Isolation, Durability"
            },
            {
                "question": "Which type of database is MongoDB?",
                "options": [
                    "Relational Database",
                    "Key-Value Store",
                    "Document-Oriented Database",
                    "Graph Database"
                ],
                "answer": "Document-Oriented Database"
            },
            {
                "question": "What is the main function of an index in a database?",
                "options": [
                    "To provide security",
                    "To speed up data retrieval",
                    "To store backup data",
                    "To enforce data integrity"
                ],
                "answer": "To speed up data retrieval"
            },
            {
                "question": "Which SQL statement is used to remove a table from a database?",
                "options": ["DELETE", "DROP", "TRUNCATE", "ALTER"],
                "answer": "DROP"
            }
        ]
    },
    {
        "topic": "OOPs",
        "data": [
            {
                "question": "What is method overloading in OOP?",
                "options": [
                    "Defining multiple methods with the same name but different parameters",
                    "Overriding a method in a derived class",
                    "Hiding data members of a class",
                    "Inheriting from multiple classes"
                ],
                "answer": "Defining multiple methods with the same name but different parameters"
            },
            {
                "question": "Which of the following represents dynamic binding in OOP?",
                "options": [
                    "Resolving a method call at compile time",
                    "Resolving a method call at runtime",
                    "Using static methods in a class",
                    "Inheriting from a base class"
                ],
                "answer": "Resolving a method call at runtime"
            },
            {
                "question": "What is an abstract class in OOP?",
                "options": [
                    "A class with only private methods",
                    "A class with no methods or properties",
                    "A class that cannot be instantiated directly",
                    "A class that allows multiple inheritances"
                ],
                "answer": "A class that cannot be instantiated directly"
            },
            {
                "question": "What is the main purpose of a constructor in OOP?",
                "options": [
                    "To destroy objects",
                    "To initialize an object’s properties",
                    "To implement polymorphism",
                    "To encapsulate methods"
                ],
                "answer": "To initialize an object’s properties"
            }
        ]
    }
]


users = {}

def startQuiz():
    score = 0
    i = 1
    for topic in topics:
        print(f'Press {i} to choose {topic["topic"]}')
        i += 1
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        startQuiz()
    if (choice < 1 or choice > len(topics)):
        print("Invalid choice")
        startQuiz()
    
    questions = topics[choice - 1]["data"]
    for question in questions:
        print("-"*40)
        print(question["question"])
        for index, option in enumerate(question["options"]):
            print(f'{index + 1}. {option}')
        try:
            answer = int(input("Enter your answer: "))
            if (answer < 1 or answer > len(question["options"])):
                print("Invalid answer")
                continue
            if (question["options"][answer - 1] == question["answer"]):
                score += 1
                print("Correct answer")
            else:
                print("Wrong answer")
                print("Correct answer is", question["answer"])
        except ValueError:
            print("Invalid answer")
            
    print(f'Your score is {score}/{len(questions)}')


def playGame():
    startQuiz()
    playAgain = input("Do you want to play again? (yes/no): ")
    if (playAgain == "yes"):
        startQuiz()
    else:
        print("Thank you for playing")


def signIn():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if type(username) != str or type(password) != str:
        print("Invalid input")
        signIn()
    if (username in users.keys() and users[username] == password):
        print("You have successfully signed in")
        print("-"*40)
        startQuiz()
    else:
        print("Invalid username or password")
        print("Or You need to sign up first")
        main()

def signUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if type(username) != str or type(password) != str:
        print("Invalid input")
        signUp()
    users[username] = password
    print("You have successfully signed up")
    print("-"*40)
    playGame()

def main():
    print("Press 1 to sign in")
    print("Press 2 to sign up")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        main()
    
    if (int(choice) == 1):
        signIn()
    elif (int(choice) == 2):
        signUp()
    else:
        print("Invalid choice")
        main()

main()
