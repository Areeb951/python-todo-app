#!/usr/bin/env python3
"""
Test script for the Todo App API
This script demonstrates the basic CRUD operations of the todo app.
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000/api"

def test_api():
    print("🧪 Testing Todo App API...")
    print("=" * 50)
    
    # Test 1: Get all todos (should be empty initially)
    print("\n1. Getting all todos...")
    response = requests.get(f"{BASE_URL}/todos")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test 2: Create a new todo
    print("\n2. Creating a new todo...")
    new_todo = {
        "title": "Buy groceries",
        "description": "Milk, bread, eggs, and vegetables",
        "priority": "high"
    }
    response = requests.post(f"{BASE_URL}/todos", json=new_todo)
    print(f"Status: {response.status_code}")
    created_todo = response.json()
    print(f"Created todo: {json.dumps(created_todo, indent=2)}")
    todo_id = created_todo['id']
    
    # Test 3: Create another todo
    print("\n3. Creating another todo...")
    another_todo = {
        "title": "Complete project documentation",
        "description": "Write comprehensive documentation for the todo app",
        "priority": "medium"
    }
    response = requests.post(f"{BASE_URL}/todos", json=another_todo)
    print(f"Status: {response.status_code}")
    print(f"Created todo: {json.dumps(response.json(), indent=2)}")
    
    # Test 4: Get all todos (should now have 2 todos)
    print("\n4. Getting all todos again...")
    response = requests.get(f"{BASE_URL}/todos")
    print(f"Status: {response.status_code}")
    todos = response.json()
    print(f"Total todos: {len(todos)}")
    for todo in todos:
        print(f"  - {todo['title']} ({todo['priority']}) - {'✓' if todo['completed'] else '○'}")
    
    # Test 5: Toggle the first todo to completed
    print(f"\n5. Toggling todo {todo_id} to completed...")
    response = requests.post(f"{BASE_URL}/todos/{todo_id}/toggle")
    print(f"Status: {response.status_code}")
    updated_todo = response.json()
    print(f"Updated todo: {json.dumps(updated_todo, indent=2)}")
    
    # Test 6: Update a todo
    print(f"\n6. Updating todo {todo_id}...")
    update_data = {
        "title": "Buy groceries (updated)",
        "description": "Milk, bread, eggs, vegetables, and fruits",
        "priority": "low"
    }
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
    print(f"Status: {response.status_code}")
    updated_todo = response.json()
    print(f"Updated todo: {json.dumps(updated_todo, indent=2)}")
    
    # Test 7: Get final state
    print("\n7. Final state of todos...")
    response = requests.get(f"{BASE_URL}/todos")
    todos = response.json()
    print(f"Total todos: {len(todos)}")
    for todo in todos:
        print(f"  - {todo['title']} ({todo['priority']}) - {'✓' if todo['completed'] else '○'}")
    
    # Test 8: Delete the first todo
    print(f"\n8. Deleting todo {todo_id}...")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    print(f"Status: {response.status_code}")
    
    # Test 9: Verify deletion
    print("\n9. Verifying deletion...")
    response = requests.get(f"{BASE_URL}/todos")
    todos = response.json()
    print(f"Remaining todos: {len(todos)}")
    for todo in todos:
        print(f"  - {todo['title']} ({todo['priority']}) - {'✓' if todo['completed'] else '○'}")
    
    print("\n✅ API testing completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API. Make sure the Docker container is running.")
        print("Run: docker run -d -p 5000:5000 --name todo-app python-todo-app")
    except Exception as e:
        print(f"❌ Error: {e}")
