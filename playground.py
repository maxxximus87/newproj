tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': 'Create chatbot',
        'description': 'Build chatbot from Flask framework',
        'done': False
    }
]

blabla=[task for task in tasks if task['id'] == 1]
print(blabla)

for task in tasks:
    if task['id'] == 1:
        blabla2 = [task]

print(blabla2)