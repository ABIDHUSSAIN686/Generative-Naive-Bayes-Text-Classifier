#Naive Bayes Text Classifier*

from collections import Counter
import random

def get_Vocabulary(dataset):
  # Finding the Vocabulary
  Positive_Dict={}
  Negative_Dict={}
  Neutral_Dict={}
  vocabulary=[]
  for sentence in dataset:
    for words in sentence.split():
      if words!='+' and words!='-' and words!='0':
        words=words.replace(".", "")
        words=words.replace(",", "")
        if words not in vocabulary:
          vocabulary.append(words)
          Positive_Dict[words]=0
          Negative_Dict[words]=0
          Neutral_Dict[words]=0
  
  return Positive_Dict,Negative_Dict,Neutral_Dict,vocabulary

def word_class_count(Positive_Dict,Negative_Dict,Neutral_Dict,vocabulary,dataset):
  # Creating Positive, Negative and Netural class count
  for sentence in dataset:
    classes=sentence.split()
    for words in sentence.split():
      words=words.replace(".", "")
      words=words.replace(",", "")
      if classes[len(sentence.split())-1]=='+' and words!='+':
        if words not in Positive_Dict:
          Positive_Dict[words]=1
        else:
          Positive_Dict[words]+=1
      elif classes[len(sentence.split())-1]=='-' and words!='-':
        if words not in Negative_Dict:
          Negative_Dict[words]=1
        else:
          Negative_Dict[words]+=1
      elif classes[len(sentence.split())-1]=='0'and words!='0':
        if words not in Neutral_Dict:
          Neutral_Dict[words]=1
        else:
          Neutral_Dict[words]+=1
  return Positive_Dict,Negative_Dict,Neutral_Dict  


def train_Model(Positive_Dict,Negative_Dict,Neutral_Dict,vocabulary,dataset):
  # Calculating Prior Probability of +ive, -ive and neutral class
  Positive_Prior_Probability=0
  Negative_Prior_Probability=0
  Neutral_Prior_Probability=0
  count=0
  for sentence in dataset:
    classes=sentence.split()
    if classes[len(sentence.split())-1]=='+':
      Positive_Prior_Probability+=1
      count+=1
    if classes[len(sentence.split())-1]=='-':
      Negative_Prior_Probability+=1
      count+=1
    if classes[len(sentence.split())-1]=='0':
      Neutral_Prior_Probability+=1
      count+=1

  Positive_Prior_Probability=Positive_Prior_Probability/count
  Negative_Prior_Probability=Negative_Prior_Probability/count
  Neutral_Prior_Probability=Neutral_Prior_Probability/count

  # Likelihood Probability +ive, -ive and neutral class
  Positive_Likelihood_Probability=Positive_Dict.copy()
  Negative_Likelihood_Probability=Negative_Dict.copy()
  Neutral_Likelihood_Probability=Neutral_Dict.copy()
  # +ive class
  for i in Positive_Likelihood_Probability:
    Positive_Likelihood_Probability[i]=(Positive_Likelihood_Probability[i]+1)/(sum(Positive_Dict.values())+len(vocabulary))
  # -ive class
  for i in Negative_Likelihood_Probability:
    Negative_Likelihood_Probability[i]=(Negative_Likelihood_Probability[i]+1)/(sum(Negative_Dict.values())+len(vocabulary))
  # neutral class
  for i in Neutral_Likelihood_Probability:
    Neutral_Likelihood_Probability[i]=(Neutral_Likelihood_Probability[i]+1)/(sum(Neutral_Dict.values())+len(vocabulary))

  Prior_Probability=[]
  Likelihood_Probability=[]
  Prior_Probability.append(Positive_Prior_Probability)
  Prior_Probability.append(Negative_Prior_Probability)
  Prior_Probability.append(Neutral_Prior_Probability)
  Likelihood_Probability.append(Positive_Likelihood_Probability)
  Likelihood_Probability.append(Negative_Likelihood_Probability)
  Likelihood_Probability.append(Neutral_Likelihood_Probability)

  return Prior_Probability,Likelihood_Probability


def predict_Data(sentence,Prior_Probability,Likelihood_Probability):
  dataset1=sentence.split()
  check_negative=1
  check_positive=1
  check_neutral=1
  # print(Likelihood_Probability[0])
  for words in dataset1:
    words=words.replace(".", "")
    words=words.replace(",", "")
    Prior_Probability[0]*=Likelihood_Probability[0][words]
    Prior_Probability[1]*=Likelihood_Probability[1][words]
    Prior_Probability[2]*=Likelihood_Probability[2][words]

  Result={'+':Prior_Probability[0],'-':Prior_Probability[1],'0':Prior_Probability[2]}
  return Result

"""***generative model***"""

def generative_Model(Vocabulary,Prior_Probability,Likelihood_Probability):
  temp1=[]
  word=""
  sentence=[]

  while(1):
    temp1=[]
    word=""
    sentence=[]
    for i in range(4):
      word = random.choices(list(Vocabulary))
      sentence.extend(word)
      sentence.extend(" ")
      res = "".join(map(str, sentence))
    result=predict_Data(res,Prior_Probability,Likelihood_Probability)
    if max(result, key=result.get)=="-" :
      print(res,max(result, key=result.get))
      break

"""***Main Driver***"""

def main():
  # Dataset for designing model
  dataset = [
  'This book is good, very good. +',
  'This book is bad, very bad. -',
  'This novel is good. +',
  'This novel is bad. -',
  'This book is some good and some bad. 0',
  'This novel is little good but little bad. 0 ']
  
  Positive_Dict,Negative_Dict,Neutral_Dict,Vocabulary=get_Vocabulary(dataset)
  Positive_Dict,Negative_Dict,Neutral_Dict=word_class_count(Positive_Dict,Negative_Dict,Neutral_Dict,Vocabulary,dataset)
  Prior_Probability,Likelihood_Probability=train_Model(Positive_Dict,Negative_Dict,Neutral_Dict,Vocabulary,dataset) 
  print("Vocabulary")
  print(Vocabulary)
  print("Positive Class")
  print(Positive_Dict)
  print("Negative Class")
  print(Negative_Dict)
  print("Neutral Class")
  print(Neutral_Dict)
  print("\n\n******Printing Prior Probability*******")
  print("Positive_Probability ",Prior_Probability[0]," \nNegative_Probability ",Prior_Probability[1]," \nNeutral_Probability ",Prior_Probability[2])
  print("\n\n******Printing Likelihood Probability*******")
  print("Positive_Likelihood_Probability ",Likelihood_Probability[0])
  print("Negative_Likelihood_Probability",Likelihood_Probability[1])
  print("Neutral_Likelihood_Probability",Likelihood_Probability[2])


  sentence="very little bad little"
  Result=predict_Data(sentence,Prior_Probability,Likelihood_Probability)
  print("\n\n******Result*******")
  print(sentence,max(Result, key=Result.get))

  print("\n\n******Generative Model*******")
  generative_Model(Vocabulary,Prior_Probability,Likelihood_Probability)
  


if __name__ == "__main__":
    main()
