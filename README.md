# Generative-Naive-Bayes-Text-Classifier
Naive Bayes is a learning algorithm commonly applied to text classification. 

# Output

## Vocabulary
['This', 'book', 'is', 'good', 'very', 'bad', 'novel', 'some', 'and', 'little', 'but'] <br>
### Positive Class <br>
{'This': 2, 'book': 1, 'is': 2, 'good': 3, 'very': 1, 'bad': 0, 'novel': 1, 'some': 0, 'and': 0, 'little': 0, 'but': 0} <br>
###  Negative Class <br>
{'This': 2, 'book': 1, 'is': 2, 'good': 0, 'very': 1, 'bad': 3, 'novel': 1, 'some': 0, 'and': 0, 'little': 0, 'but': 0} <br>
###  Neutral Class <br>
{'This': 2, 'book': 1, 'is': 2, 'good': 2, 'very': 0, 'bad': 2, 'novel': 1, 'some': 2, 'and': 1, 'little': 2, 'but': 1} <br>


## Printing Prior Probability <br>
Positive_Probability  0.3333333333333333   <br>
Negative_Probability  0.3333333333333333   <br>
Neutral_Probability  0.3333333333333333 <br>


## Printing Likelihood Probability <br>
#### Positive_Likelihood_Probability <br> 
{'This': 0.14285714285714285, 'book': 0.09523809523809523, 'is': 0.14285714285714285, 'good': 0.19047619047619047, 'very': 0.09523809523809523, 'bad': 0.047619047619047616, 'novel': 0.09523809523809523, 'some': 0.047619047619047616, 'and': 0.047619047619047616, 'little': 0.047619047619047616, 'but': 0.047619047619047616} <br>
#### Negative_Likelihood_Probability <br> 
{'This': 0.14285714285714285, 'book': 0.09523809523809523, 'is': 0.14285714285714285, 'good': 0.047619047619047616, 'very': 0.09523809523809523, 'bad': 0.19047619047619047, 'novel': 0.09523809523809523, 'some': 0.047619047619047616, 'and': 0.047619047619047616, 'little': 0.047619047619047616, 'but': 0.047619047619047616} <br>
#### Neutral_Likelihood_Probability <br> 
{'This': 0.1111111111111111, 'book': 0.07407407407407407, 'is': 0.1111111111111111, 'good': 0.1111111111111111, 'very': 0.037037037037037035, 'bad': 0.1111111111111111, 'novel': 0.07407407407407407, 'some': 0.1111111111111111, 'and': 0.07407407407407407, 'little': 0.1111111111111111, 'but': 0.07407407407407407} <br>


## Result <br>
very little bad little 0 <br>


#  Generative Model Result <br>
book bad and is  - <br>

# Commands to run this code
    - Clone this repository on your machine
      ```
        $ git clone https://github.com/ABIDHUSSAIN686/Generative-Naive-Bayes-Text-Classifier
      ```
    - Open terminal in your current Directory
    - Type command 'python filename'.
      ```
      $ python Naive_Bayes_Classifier.py
      ```
