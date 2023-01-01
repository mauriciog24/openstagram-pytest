# Tests for OpenStagram

The goal of this project is to automate test cases for the [OpenStagram](https://github.com/mauriciog24/openstagram) project using Python, pytest and Selenium WebDriver.

**Instructions:**

1. You need to have installed Python 3.7+
2. This project supports Chrome, Firefox and Microsoft Edge
3. Download one of the following webdrivers and add it to your path:
   1. Chrome: [chromedriver](https://chromedriver.chromium.org/downloads)
   2. Firefox: [geckodriver](https://github.com/mozilla/geckodriver)
   3. Microsoft Edge: [msedgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
4. Create a virtual environment and activate it

    |          | Windows                | MacOS/Linux             |
    |----------|------------------------|-------------------------|
    | Create   | py -3 -m venv env      | python3 -m venv env     |
    | Activate | .\env\scripts\activate | source env/bin/activate |

5. Install the requirements with `pip3 install -r requirements.txt`
6. Go to the project directory with `cd openstagram`
7. Run the tests with `pytest -v tests --browser=chrome --host=localhost --port=8000`
    1. Other browser options are `--browser=firefox` and `--browser=edge`
    2. If you are running the base project with Docker, change the port variable to `--port=80`

#

<a href="#">
    <img align="left" width="30" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python">
    <img align="left" width="30" src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" alt="pytest">
    <img align="left" width="30" src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" alt="Selenium">
</a>
