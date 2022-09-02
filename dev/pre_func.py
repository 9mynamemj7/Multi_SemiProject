import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
import joblib

def kor_senti(pipe : any, cvect : any, nb, series):
    '''
    모델은 joblib으로 불러온 파이프라인 입력

    시리즈는 분석하고자 하는 데이터프레임의 시리즈 입력

    긍정, 부정 튜플 리턴
    '''
    series = series
    series = series.str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣]', ' ').str.strip()
    series = series.dropna()

    positive = 0
    negative = 0
    
    if pipe != "":
        model = pipe
        

        for i in series:
            score = model.predict([i])
            score = score.astype(int)

            if score == 1:
                positive += 1
            else:
                negative += 1
        # 그래프 그리기
        plt.figure(linewidth=2)    
        plt.bar(np.arange(2), [positive, negative])
        plt.xticks(np.arange(2), ['positive', 'negative'])
        plt.savefig("kor_sent.png",edgecolor='blue')
        
        return (positive, negative)

    else:

        for i in series:
            review_cv = cvect.transform([i])
            score = nb.predict(review_cv)
            if score == 1:
                positive += 1
            else:
                negative += 1

        # 그래프 그리기
        plt.figure(linewidth=2)    
        plt.bar(np.arange(2), [positive, negative])
        plt.xticks(np.arange(2), ['positive', 'negative'])
        plt.savefig("kor_sent.png",edgecolor='blue')
        
        return (positive, negative)


def eng_senti(pipe, cvect, nb, series):
    series = series
    series = series.str.replace('[^A-Za-z]',' ').str.strip()
    series = series.dropna()

    positive = 0
    negative = 0

    if pipe != "":
        model = pipe

        for i in series:
            score = model.predict([i])
            score = score.astype(int)

            if score == 1:
                positive += 1
            else:
                negative += 1
        # 그래프 그리기
        plt.figure(linewidth=2)    
        plt.bar(np.arange(2), [positive, negative])
        plt.xticks(np.arange(2), ['positive', 'negative'])
        plt.savefig("eng_sent.png",edgecolor='blue')

        return (positive, negative)
    
    else:

        for i in series:
            review_cv = cvect.transform([i])
            score = nb.predict(review_cv)
            if score == 1:
                positive += 1
            else:
                negative += 1
        # 그래프 그리기
        plt.figure(linewidth=2)    
        plt.bar(np.arange(2), [positive, negative])
        plt.xticks(np.arange(2), ['positive', 'negative'])
        plt.savefig("eng_sent.png",edgecolor='blue')

        return (positive, negative)

    
    