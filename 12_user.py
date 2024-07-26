import re

class User:
    """
    This class represents a User object for our corporate 
    web application. It can be extended into other classes
    such as SuperUsers or Employees
    """
    def __init__(self, name, username, email):
        """
        Constructor has the following arguments:
        name - real-world name for the user
        username - unique string, can contain underscores or numbers
        email - email address for the user
        """
        self.name = name
        self.username = username
        self.email = email

    def validate_email(self):
        """Raises an exception if email is invalid"""
        email_regex = r'^\S+@\S+\.\S+$'
        if not re.match(email_regex, self.email):
            raise Exception('Email address is invalid')
