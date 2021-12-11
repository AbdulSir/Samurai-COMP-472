import gensim.downloader as api
from gensim.models import Word2Vec
from gensim.similarities import Similarity

import inspect

def main():
    wv = api.load('word2vec-google-news-300')

    # loading a file with open()
    myfile = open('synonyms.txt')
    list_of_words = []
    list_of_similarity_score = []
    possible_answers = ['a','b','c','d']

    # reading each line of the file and printing to the console
    for line in myfile:
        temp = line.split('\t')
        if len(temp) > 1:
            #question + 4 options
            print(temp[1].split('\n')[0])
            list_of_words.append(temp[1].split('\n')[0])
        else:
            #Actual answer
            answer = temp[0].split('\n')[0]
            for i in range(len(list_of_words)):
                if i>0: #start at index 1
                    try:
                        #Compare similarity of the words and push the score into a list
                        list_of_similarity_score.append(wv.similarity(list_of_words[0], list_of_words[i]))
                    except KeyError:
                        #Need to handle an exception in case word was not found in Word2Vec model
                        print("a word did not appear in this model")
            #Find the most probable synonym
            if len(list_of_similarity_score) == 4:           
                answer_by_model = max(list_of_similarity_score)
                if list_of_similarity_score.index(answer_by_model) == possible_answers.index(answer):
                    print("Our model predicted the right answer")
                else:
                    print("Our model DID NOT predict the right answer")
                print("The question: " + list_of_words[0] + '\tThe predicted answer: ' + list_of_words[list_of_similarity_score.index(answer_by_model) + 1] + '\tThe actual answer: ' + list_of_words[possible_answers.index(answer) + 1])

            #When an answer is found, reset the list_of_words array and start filling it for the new question
            list_of_words = []
            list_of_similarity_score = []

# Push all the 5 words into an array
# iterate thru the array, compare arr[0] with arr[0+i]
# Store the values of similarity in an array, call max(arr_of_similiar) len(arr) = 4 > 0,1,2,3
# find the index of the of the value which max returned > e.g. 2
# compare that to the [a,b,c,d] array. 

# store the 
    # pairs = [
    # ('car', 'minivan'),   # a minivan is a kind of car
    # ('car', 'bicycle'),   # still a wheeled vehicle
    # ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    # ('car', 'cereal'),    # ... and so on
    # ('car', 'communism'),
    # ]
    # for w1, w2 in pairs:
    #     print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))

if __name__ == "__main__":
    main()