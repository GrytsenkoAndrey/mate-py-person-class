class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_dict in people:
        person_instances.append(
            Person(person_dict["name"], person_dict["age"])
        )

    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

    return person_instances
