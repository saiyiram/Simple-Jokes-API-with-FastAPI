# Simple Jokes API with FastAPI

Welcome to the Simple Jokes API repository! This project demonstrates how to create a RESTful API using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- **FastAPI**: Utilizes FastAPI for rapid API development.
- **Simple Jokes**: Offers a collection of jokes accessible via the API.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

### Installation

1. Clone the repository: \
<code>git clone https://github.com/saiyiram/Simple-Jokes-API-with-FastAPI.git</code>

2. Navigate to the project directory: \
<code>cd Simple-Jokes-API-with-FastAPI</code>

3. Install the required packages: \
<code>pip install -r requirements.txt</code>

4. Run the application: \
<code>uvicorn main:app --reload</code>


## Usage

After starting the application, access the API at `http://localhost:8000`. The API provides a single endpoint to fetch a random joke:

- **GET /joke**: Returns a random joke.

## Copyright Notice

Please note that the jokes provided by this API are copyrighted to their respective owners. This API is intended for educational and entertainment purposes only.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for bugs or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI for its high performance and ease of use.
- The community for their support and contributions.
