# Python Todo App

A modern, beautiful todo application built with Python Flask and Docker. Features a responsive web interface with real-time task management capabilities.

## Features

- ✨ Modern, responsive UI with beautiful gradients
- 📝 Create, read, update, and delete tasks
- 🎯 Priority levels (Low, Medium, High)
- ✅ Mark tasks as complete/incomplete
- 📊 Real-time statistics dashboard
- 🗄️ SQLite database for data persistence
- 🐳 Docker containerization
- 🔄 RESTful API endpoints

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with Font Awesome icons
- **Containerization**: Docker

## Quick Start

### Prerequisites

- Docker installed on your system
- Git (optional, for cloning)

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t python-todo-app .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 5000:5000 --name todo-app python-todo-app
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

### Alternative: Run with Docker Compose

If you prefer using docker-compose, create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  todo-app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

Then run:
```bash
docker-compose up -d
```

## API Endpoints

The application provides a RESTful API for task management:

- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/<id>` - Update a todo
- `DELETE /api/todos/<id>` - Delete a todo
- `POST /api/todos/<id>/toggle` - Toggle todo completion status

### Example API Usage

```bash
# Get all todos
curl http://localhost:5000/api/todos

# Create a new todo
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, bread, eggs", "priority": "high"}'

# Toggle todo completion
curl -X POST http://localhost:5000/api/todos/1/toggle

# Delete a todo
curl -X DELETE http://localhost:5000/api/todos/1
```

## Development

### Running Locally (without Docker)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

### Project Structure

```
python-todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
└── templates/
    └── index.html     # Main HTML template
```

## Database

The application uses SQLite as the database, which is automatically created when the application starts. The database file (`todos.db`) is stored in the application directory.

### Database Schema

```sql
CREATE TABLE todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    priority VARCHAR(20) DEFAULT 'medium'
);
```

## Features in Detail

### Task Management
- **Create Tasks**: Add new tasks with title, description, and priority
- **Edit Tasks**: Update task details through the API
- **Delete Tasks**: Remove tasks with confirmation
- **Complete Tasks**: Toggle task completion status

### Priority System
- **Low Priority**: Blue badge
- **Medium Priority**: Yellow badge (default)
- **High Priority**: Red badge

### Statistics Dashboard
- Total number of tasks
- Number of completed tasks
- Number of pending tasks

### Responsive Design
- Mobile-friendly interface
- Modern gradient backgrounds
- Smooth animations and transitions
- Font Awesome icons for better UX

## Docker Commands

### Useful Docker Commands

```bash
# Build the image
docker build -t python-todo-app .

# Run the container
docker run -d -p 5000:5000 --name todo-app python-todo-app

# Stop the container
docker stop todo-app

# Remove the container
docker rm todo-app

# View logs
docker logs todo-app

# Access container shell
docker exec -it todo-app /bin/bash

# Remove the image
docker rmi python-todo-app
```

### Data Persistence

To persist data between container restarts, you can mount a volume:

```bash
docker run -d -p 5000:5000 -v $(pwd)/data:/app --name todo-app python-todo-app
```

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Check what's using port 5000
   netstat -tulpn | grep :5000
   
   # Use a different port
   docker run -d -p 5001:5000 --name todo-app python-todo-app
   ```

2. **Permission issues:**
   ```bash
   # Run with sudo if needed
   sudo docker build -t python-todo-app .
   ```

3. **Container won't start:**
   ```bash
   # Check container logs
   docker logs todo-app
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
