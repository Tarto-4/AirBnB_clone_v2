# AirBnB_clone_v2 - web_flask

This directory contains Flask web applications demonstrating routes.

**Requirements:**

* Python 3 (tested with 3.4.3)
* Flask framework

**Files:**

* `0-hello_route.py`: Flask application with a route displaying "Hello HBNB!"
* `1-hbnb_route.py`: Flask application with routes displaying "Hello HBNB!" and "HBNB"
* `2-c_route.py`: Flask application with routes for greetings and text processing
* `__init__.py` (Optional): Empty file to mark the directory as a package (for future expansion)

**Instructions:**

1. Save the code snippets above in the corresponding files (`0-hello_route.py`, `1-hbnb_route.py`, `2-c_route.py`, optional `__init__.py`).
2. Open a terminal in the `web_flask` directory.
3. Run the application with routes: `python3 2-c_route.py`
4. Access the applications in your browser:
    * http://localhost:5000/ (Displays "Hello HBNB!")
    * http://localhost:5000/hbnb (Displays "HBNB")
    * http://localhost:5000/c/your_text (Replace "your_text" with your desired text)

**Additional Notes:**

* The application listens on all interfaces (0.0.0.0) on port 5000.
* The route definitions use `strict_slashes=False` to handle trailing slashes consistently.

This example demonstrates capturing dynamic data from URLs and processing it within Flask routes.  
