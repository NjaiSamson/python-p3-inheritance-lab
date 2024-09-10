#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None:
            self.knowledge = []  # Initialize knowledge as an empty list
        else:
            self.knowledge = knowledge

    def learn(self, text):
        if isinstance(text, str):
            self.knowledge.append(text)  # Add the string to the knowledge list
        else:
            raise ValueError("Knowledge must be a string")
