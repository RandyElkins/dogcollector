# Add the Dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Aggie', 'Dachshund', 'foul little demon', 14),
  Dog('Bailey', 'Pug', 'cute, but dumb', 11),
  Dog('Cake', 'Mutt: Aussie Shepherd Mix', 'LOVING, and smart', 3),
  Dog('Fake', 'Pomeranian', 'Fluffball. Really I am just testing the age conditional statement.', 0),
]
