



class Person:
  def __init__(self,  name:str, height:str, age:int, profession: str):
    self.name = name
    self.height = height
    self.age = age
    self.profession = profession


Person = [
  Person("Lucas", 5.9, 15, "student"),
  Person("Manuel", 6, 27, "teacher")
]

# Determine output Directory
myOutputPath = Path(__file__).persons[0]
myOutputFilePath = os.path.join(myOutputPath, 'person.json')

# Serialization
with open(myOutputFilePath, 'w') as outfile:
  # For a single student seen above use: json.dump(s.__dict__, outfile)
  # For loop will include all students in list.
  json.dump([data.__dict__ for data in myDataSet], outfile)

  file = open('ExperimentData.json',)
experimentJson = json.load(file)

myObject = ExperimentData(**experimentJson)