# RESTful API Exercises

This directory contains exercises on consuming and processing data from RESTful APIs using Python.

## Tasks

- `task_02_requests.py`: Fetches posts from [JSONPlaceholder](https://jsonplaceholder.typicode.com/) and:
  - Prints all post titles with status code
  - Saves posts to `posts.csv` with columns: `id`, `title`, `body`

## Dependencies

- `requests` library (install with `pip3 install requests`)
- Python 3 standard library (`csv`, `json`)

## Usage

```python
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()   # Prints status code and titles
fetch_and_save_posts()    # Creates posts.csv
cat > ~/holbertonschool-higher_level_programming/restful-api/README.md << 'EOF'
# RESTful API Exercises

This directory contains exercises on consuming and processing data from RESTful APIs using Python.

## Tasks

- `task_02_requests.py`: Fetches posts from [JSONPlaceholder](https://jsonplaceholder.typicode.com/) and:
  - Prints all post titles with status code
  - Saves posts to `posts.csv` with columns: `id`, `title`, `body`

## Dependencies

- `requests` library (install with `pip3 install requests`)
- Python 3 standard library (`csv`, `json`)

## Usage

```python
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()   # Prints status code and titles
fetch_and_save_posts()    # Creates posts.csv
# 1. Go to your project root
cd ~/holbertonschool-higher_level_programming

# 2. Create README.md in restful-api folder
cat > restful-api/README.md << 'EOF'
# RESTful API Exercises

This directory contains Python scripts that interact with RESTful APIs.

- `task_02_requests.py`: Fetches posts from JSONPlaceholder and saves them to a CSV file.
