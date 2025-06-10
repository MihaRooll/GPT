# ToonCam

ToonCam is an offline style-transfer video service that processes video locally to apply cartoon-inspired filters. It uses Django and related libraries to provide a self-hosted web interface.

## Quick Start

```bash
# Clone the repository
$ git clone <repo-url>
$ cd GPT

# Install dependencies
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# Start the development server
$ python tooncam/manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to view the app.

## Requirements

- Python 3.8 or newer
- Packages listed in `requirements.txt`

## Development Workflow

1. Create a virtual environment and install dependencies.
2. Develop features inside the `apps` directory.
3. Run the Django server with `python tooncam/manage.py runserver`.
4. Commit your changes and open a pull request.

## Further Documentation

- [Django documentation](https://docs.djangoproject.com/)
- See the source files in `tooncam` and `apps` for implementation details.
