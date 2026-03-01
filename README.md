# ✅ Todo REST API

A simple and clean RESTful API for managing tasks, built with **Django** and **Django REST Framework**.

---

## 🚀 Features

- Retrieve all tasks or a single task
- Create new tasks
- Update existing tasks
- Delete a single task or all tasks at once

---

## 🛠️ Tech Stack

- **Python**
- **Django**
- **Django REST Framework**

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Todo.git
   cd Todo
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

---

## 📁 Project Structure

```
├── tasks/
│   ├── models.py        # Task model
│   ├── serializers.py   # Task serializer
│   ├── views.py         # API views
│   └── urls.py          # URL endpoints
├── manage.py
└── requirements.txt
```

---

## 🗄️ Data Model

### Task

| Field       | Type        | Description                          |
|-------------|-------------|--------------------------------------|
| `id`        | Integer     | Auto-generated primary key           |
| `title`     | CharField   | Title of the task (max 30 chars)     |
| `completed` | BooleanField| Completion status (default: `False`) |

---

## 🔗 API Endpoints

Base URL: `http://127.0.0.1:8000/api/tasks/`  
*(Adjust base URL according to your project's `urls.py`)*

| Method   | Endpoint              | Description              |
|----------|-----------------------|--------------------------|
| `GET`    | `/`                   | Retrieve all tasks       |
| `GET`    | `/<id>/`              | Retrieve a single task   |
| `POST`   | `/create/`            | Create a new task        |
| `PUT`    | `/<id>/update/`       | Update an existing task  |
| `DELETE` | `/<id>/delete/`       | Delete a single task     |
| `DELETE` | `/delete/`            | Delete all tasks         |

---

## 📬 Example Requests & Responses

### Get All Tasks
```http
GET /api/tasks/
```
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "title": "Read a book",
    "completed": true
  }
]
```

### Get Single Task
```http
GET /api/tasks/1/
```
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

### Create a Task
```http
POST /api/tasks/create/
Content-Type: application/json

{
  "title": "Walk the dog",
  "completed": false
}
```
```json
{
  "id": 3,
  "title": "Walk the dog",
  "completed": false
}
```

### Update a Task
```http
PUT /api/tasks/3/update/
Content-Type: application/json

{
  "title": "Walk the dog",
  "completed": true
}
```
```json
{
  "id": 3,
  "title": "Walk the dog",
  "completed": true
}
```

### Delete a Task
```http
DELETE /api/tasks/3/delete/
```
```
204 No Content
```

### Delete All Tasks
```http
DELETE /api/tasks/delete/
```
```
204 No Content
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
