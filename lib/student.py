#!/usr/bin/env python

from user import User


class Student(User):
    knowledge = list()

    
    def learn(self, subject):
        return self.knowledge.append(subject)
        pass
Amelia = Student("Amelis", "Maina")
print(Amelia.first_name)
print(Amelia.last_name)