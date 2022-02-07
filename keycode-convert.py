address = input('Enter email:')

def getCode(address):
  address = address.upper()
  charList = []
  for n in range(len(address)):
    charList.append(f'Keycode.{address[n]}')
  for i in range(len(charList)):
    if '.@' in charList[i]:
      print('keyboard.send(Keycode.SHIFT, Keycode.TWO)')
      continue
    elif '.0' in charList[i]:
      charList[i] = charList[i].replace('.0', '.ZERO')
    elif '.1' in charList[i]:
      charList[i] = charList[i].replace('.1', '.ONE')
    elif '.2' in charList[i]:
      charList[i] = charList[i].replace('.2', '.TWO')
    elif '.3' in charList[i]:
      charList[i] = charList[i].replace('.3', '.THREE')
    elif '.4' in charList[i]:
      charList[i] = charList[i].replace('.4', '.FOUR')
    elif '.5' in charList[i]:
      charList[i] = charList[i].replace('.5', '.FIVE')
    elif '.6' in charList[i]:
      charList[i] = charList[i].replace('.6', '.sIX')
    elif '.7' in charList[i]:
      charList[i] = charList[i].replace('.7', '.SEVEN')
    elif '.8' in charList[i]:
      charList[i] = charList[i].replace('.8', '.EIGHT')
    elif '.9' in charList[i]:
      charList[i] = charList[i].replace('.9', '.NINE')
    elif '..' in charList[i]:
      charList[i] = charList[i].replace('..', '.PERIOD')
      
    print(f'keyboard.send({charList[i]})')

  return

getCode(address)
