
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._member = [
            {
                "first_name": "Jimmy",
                "id": 1,
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            },
            {
                "first_name": "Jane",
                "id": 2,
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "first_name": "John",
                "id": 3,
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]    
            }
        ] 
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
     member["id"] = member.get("id", self._generateId())
     member["last_name"] = self.last_name
     member["lucky_numbers"] = member.get("lucky_numbers", [])
     self._member.append(member)
     return member 

    def get_member(self, id):
        for member in self._member:
            if member["id"] == (id):
                return member
            
    def delete_member(self, id):
        for position in range(len(self._member)):
            if self._member[position]["id"] == id:
                self._member.pop(position)
                return None
            
        
    def get_all_members(self):
        return self._member

        if (not(member["id"])):
         member['id'] = self._generate_id()