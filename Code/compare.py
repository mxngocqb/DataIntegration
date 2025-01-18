import math

def compare(docA, docB):
    bowA = docA.split(" ")
    bowB = docB.split(" ")
    
    wordSet = set(bowA).union(set(bowB))
    
    wordDictA = dict.fromkeys(wordSet, 0) 
    wordDictB = dict.fromkeys(wordSet, 0) 
    
    for word in bowA:
        wordDictA[word]+=1
    
    for word in bowB:
        wordDictB[word]+=1
        
    tfBowA = computeTF(wordDictA, bowA)
    tfBowB = computeTF(wordDictB, bowB)
    idfs = computeIDF([wordDictA, wordDictB])
    tfidfBowA = computeTFIDF(tfBowA, idfs)
    tfidfBowB = computeTFIDF(tfBowB, idfs)
    return calculate(tfidfBowA, tfidfBowB)

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = N / float(val)
        
    return idfDict 

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

def calculate(tfidfBowA, tfidfBowB):
    
    tmp = tfidfBowA if (len(tfidfBowA.keys()) > len(tfidfBowB.keys())) else tfidfBowB
    
    tu = 0
    mauA = 0
    mauB = 0
    
    for word, val in tmp.items():
        
        if tfidfBowA[word] is None:
            tfidfBowA[word] = 0
            
        if tfidfBowB[word] is None:
            tfidfBowB[word] = 0
              
        tu += tfidfBowA[word] * tfidfBowB[word]
        mauA += tfidfBowA[word] ** 2
        mauB += tfidfBowB[word] ** 2
    
    return tu / (math.sqrt(mauA) * math.sqrt(mauB))

    
    print(len(tfidfBowA.keys()) != len(tfidfBowB.keys()))    
    
    
    