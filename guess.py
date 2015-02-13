#!/usr/bin/python
import json,glob

def showTree():
  jsonString=json.dumps(data,sort_keys=False, indent=2)
  print(jsonString)

def saveTree():
  global gamefile
  #jsonString=json.dumps(data,sort_keys=False, indent=2)
  with open(gamefile,'w') as outfile:
    json.dump(data,outfile,sort_keys=False, indent=2)

def loadTree():
  global gamefile
  data={'root':{'question':'A Horse','yes':None,'no':None},'question':'Think of an animal and I will try to guess it.'}
  try:
    with open(gamefile) as infile:
      data=json.load(infile)
  except EnvironmentError:
      print('Oops problem loading my brain!')
  return data


def yesOrNo(question=''):
  answered=False
  while not answered:
    if question!='':  
      print (question)
    answer=raw_input().lower()
    if answer!='yes' and answer!='no' and answer!='y' and answer!='n':
      print ("Sorry, I don't understand '"+answer+"' please answer yes or no or y or n.")
    else:
      answered=True
  if answer=='n' or answer=='no':
    return False
  return True

def playGame():
  global gamefile
  if debug:
    showTree()
  currentLeaf=data['root']
  print(data['question'])
  guessedRight=False
  guessedWrong=False
  while not guessedRight and not guessedWrong:
    if currentLeaf['yes'] is None and currentLeaf['no'] is None:
      print("Hmmm.. I'm ready to have a guess. Is it ...")
    theirAnswer=yesOrNo(currentLeaf['question']+' yes/no')
    if theirAnswer:
      if currentLeaf['yes'] is None:
        guessedRight=True
        print ('Woohooo I guessed right!!!')
      else:
        currentLeaf=currentLeaf['yes']
    else:
      if currentLeaf['no'] is None:
        guessedWrong=True
        print ('Oh dear, I give up what where you thinking of?')
        newAnimal=raw_input()
        print ('What yes/no question would tell the diference between '+currentLeaf['question']+' and '+newAnimal)
        newQuestion=raw_input()
        newAnswer=yesOrNo('So what would be the answer for '+newAnimal+' yes, or no?')
        if not newAnswer:
          currentLeaf['no']={'question':newAnimal,'no':None,'yes':None}
          currentLeaf['yes']={'question':currentLeaf['question'],'no':None,'yes':None}
        else:
          currentLeaf['yes']={'question':newAnimal,'no':None,'yes':None}
          currentLeaf['no']={'question':currentLeaf['question'],'no':None,'yes':None}
        currentLeaf['question']=newQuestion
        saveTree()
        print ("Thanks for teaching me, I'll do much better next time now.")
        if debug:
          showTree()
      else:
        currentLeaf=currentLeaf['no']

gamefile='guess.json'
games=glob.glob('*.json')
if (len(games)<=1):
  gamefile=games[0]
debug=False
data=loadTree()
keepPlaying=True
while keepPlaying:
  playGame()
  keepPlaying=yesOrNo('Play again? Yes or No.')
print('Bye, and thanks for playing.')
