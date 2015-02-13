#!/usr/bin/python
import json

def showTree():
  jsonString=json.dumps(data,sort_keys=False, indent=2)
  print(jsonString)

def saveTree():
  #jsonString=json.dumps(data,sort_keys=False, indent=2)
  with open('guess.json','w') as outfile:
    json.dump(data,outfile,sort_keys=False, indent=2)

def loadTree():
  with open('guess.json') as infile:
    data=json.load(infile)
    return data

def playGame():
  if debug:
    showTree()
  currentLeaf=data['root']
  print('Think of an animal and I will try to guess')
  guessedRight=False
  guessedWrong=False
  while not guessedRight and not guessedWrong:
    if currentLeaf['yes'] is None and currentLeaf['no'] is None:
      print("Hmmm.. I'm ready to have a guess. Is it ...")
    print(currentLeaf['question']+' yes/no')
    theirAnswer=raw_input().lower()
    if theirAnswer=='y' or theirAnswer=='yes':
      if currentLeaf['yes'] is None:
        guessedRight=True
        print ('Woohooo I guessed right!!!')
      else:
        currentLeaf=currentLeaf['yes']
    elif theirAnswer=='n' or theirAnswer=='no':
      if currentLeaf['no'] is None:
        guessedWrong=True
        print ('Oh dear, I give up what where you thinking of?')
        newAnimal=raw_input()
        print ('What yes/no question would tell the diference between '+currentLeaf['question']+' and '+newAnimal)
        newQuestion=raw_input()
        newAnswer='jellyface'
        while newAnswer!='yes' and newAnswer!='no' and newAnswer!='y' and newAnswer!='n':
          print ('So what would be the answer for '+newAnimal+' yes, or no?')
          newAnswer=raw_input().lower()
        if newAnswer=='n' or newAnswer=='no':
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
    else:
        print ("I don't understand ["+theirAnswer+"] please answer yes or no")

debug=False
data={'root':{'question':'A Horse','yes':None,'no':None}}
data=loadTree()
playGame()
