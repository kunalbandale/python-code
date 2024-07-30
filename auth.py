user1 = {
  'name': 'Sorna',
  'valid': False  
}

def authenticated(fn):
  def wrapper(user):
      if user.get('valid'):
          return fn(user)
      else:
          print('User is not authenticated.')
  return wrapper

@authenticated
def message_friends(user):
  print('message has been sent')

message_friends(user1)