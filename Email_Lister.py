import numpy as np
import main
import pandas as pd

def lister():
    # lst=input('Which List:')
    raw = pd.read_csv('Sample15.csv')
    df = pd.DataFrame(raw)

    # Create 'Domain' and 'Email Valid columns
    df['Domain'] = df['Website']

    # Parse Domain from rest of URL in 'Website' column
    for i in range(len(df['Website'])):
        if 'www.' in df['Website'][i]:
            split = df['Website'][i].index('www.') + 4
            df['Domain'][i] = df['Website'][i][split:]

        else:
            split = df['Website'][i].index('//') + 2
            df['Domain'][i] = df['Website'][i][split:]

    for i in range(len(df['Domain'])):
        if df['Domain'][i][-1] == '/':
            df['Domain'][i] = df['Domain'][i][:-1]

    # Create list of emails from founders
    dict = {}
    emlst = []
    companylst = []
    namelst = []
    for i in range(len(df['Founders'])):
        rawIndiv = df['Founders'][i].split(', ')
        for a in rawIndiv:
            space = a.index(' ')
            # First@domain
            em1 = (a[:space] + '@' + df['Domain'][i]).lower()
            list_build(em1, emlst, companylst, namelst, i, a)

            # First.Last
            em2 = (a[:space] + '.' + a[space + 1:] + '@' + df['Domain'][i]).lower()
            list_build(em2, emlst, companylst, namelst, i, a)

            # FirstLast
            em3 = (a[:space] + a[space + 1:] + '@' + df['Domain'][i]).lower()
            list_build(em3, emlst, companylst, namelst, i, a)

            # First[0]Last
            em4 = (a[0] + a[space + 1:] + '@' + df['Domain'][i]).lower()
            list_build(em4, emlst, companylst, namelst, i, a)

            # First[0].Last
            em5 = (a[0] + '.' + a[space + 1:] + '@' + df['Domain'][i]).lower()
            list_build(em5, emlst, companylst, namelst, i, a)

            dict = {'Company': companylst, 'Name': namelst, 'Email': emlst}

    emails = pd.DataFrame(dict)
    # print(emails.head())
    # emails.to_csv('TestResults.csv', index=False)
    return emails


def list_build(em, emlst, companylst, namelst, i, a):
    emlst.append(em)
    companylst.append(df['Organization Name'][i])
    namelst.append(a)
    return emlst, companylst, namelst


lister()
