class PlayerCharcter:
  def __init__(self,name,age):
      self.name = name
      self.age = age


  def run():
      print("Running")
      return "Done"

player1 = PlayerCharcter('kunal',23)
print(player1.name)
print(player1.age)