## CryptoPulse
```markdown


CryptoPulse is a real-time cryptocurrency price tracking web application. It allows users to check the current prices of cryptocurrencies in multiple currencies, including USD and INR, and provides a user-friendly interface to view real-time data.

## Features

- **Real-Time Price Tracking**: View the real-time price of various cryptocurrencies like Bitcoin, Ethereum, and others.
- **Multi-Currency Support**: Check cryptocurrency prices in multiple currencies like USD and INR.
- **Interactive and Responsive Design**: Modern and attractive design with a smooth, interactive user experience.
- **No Config File Required**: The app doesn't require a config file for setup, simplifying deployment.

## Technologies Used

- **Python**: Backend development using Flask, a micro web framework for Python.
- **Flask**: For web server routing and rendering HTML templates.
- **HTML/CSS**: For creating the structure and styling of web pages.
- **JavaScript**: For creating interactive elements and fetching real-time data.
- **Requests**: For making HTTP requests to external APIs to get cryptocurrency data.
- **Flask Templates (Jinja2)**: For rendering dynamic HTML content.
- **GitHub**: For version control and project collaboration.

## Project Structure

```plaintext
CryptoPulse/
│
├── app/
│   ├── __init__.py              # Initialize the Flask app
│   ├── routes.py                # Application routes (views)
│   ├── utils.py                 # Utility functions (e.g., for fetching crypto prices)
│   └── templates/               # HTML templates for rendering dynamic content
│       ├── index.html           # The main index page for the app
│       └── result.html          # Page to display the price of a specific cryptocurrency
│   └── static/                  # Static files like CSS and images
│       └── css/
│           └── styles.css       # CSS for the app
│
├── venv/                        # Virtual environment for Python packages
│
├── run.py                       # Main file to run the Flask app
├── .gitignore                   # Specifies files and directories to ignore in Git
├── requirements.txt             # List of required Python packages
└── README.md                    # This file (documentation)
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/the-subham-techpro17/CryptoPulse.git
```

### 2. Set up a virtual environment

Navigate to the project folder and create a virtual environment:

```bash
cd CryptoPulse
python -m venv venv
```

### 3. Install dependencies

Activate the virtual environment and install the required dependencies:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

Then install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Once all dependencies are installed, run the application:

```bash
python run.py
```

The app should now be running on `http://127.0.0.1:5000/` by default.

### 5. Access the Application

Open your browser and navigate to `http://127.0.0.1:5000/` to start using the app.

## Contributing

Feel free to fork the project and submit pull requests. Make sure to follow the code style and write meaningful commit messages.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes with clear and descriptive messages.
5. Push your changes to your forked repository.
6. Open a pull request.




