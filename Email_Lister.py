import numpy as np
import main
import pandas as pd

def lister():
    # lst=input('Which List:')
    raw = pd.read_csv('200NewYork.csv')
    df = pd.DataFrame(raw)

    # Create 'Domain' column
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
    emlst = []
    companylst = []
    namelst = []
    valid = []
    dict = {'Company': companylst, 'Name': namelst, 'Email': emlst, 'Email Result': valid}

    for i in range(len(df['Founders'])):
        rawIndiv = df['Founders'][i].split(', ')
        for a in rawIndiv:
            templst = []
            space = a.index(' ')
            # First@domain
            em1 = (a[:space] + '@' + df['Domain'][i]).lower()
            templst.append(em1)

            # First.Last
            em2 = (a[:space] + '.' + a[space + 1:] + '@' + df['Domain'][i]).lower()
            templst.append(em2)

            # FirstLast
            em3 = (a[:space] + a[space + 1:] + '@' + df['Domain'][i]).lower()
            templst.append(em3)

            # First[0]Last
            em4 = (a[0] + a[space + 1:] + '@' + df['Domain'][i]).lower()
            templst.append(em4)

            # First[0].Last
            em5 = (a[0] + '.' + a[space + 1:] + '@' + df['Domain'][i]).lower()
            templst.append(em5)

            for z in templst:
                try:
                    result = main.ping_email(z)
                    print(z + ' ' + str(result))
                    if result == 'Success':
                        emlst.append(z)
                        companylst.append(df['Organization Name'][i])
                        namelst.append(a)
                        valid.append(result)
                        break
                except:
                    print('There was an Error')
                    emails = pd.DataFrame(dict)
                    emails.to_csv('TestResults.csv', index=False)


    emails = pd.DataFrame(dict)
    # print(emails.head())
    emails.to_csv('TestResults.csv', index=False)
    return emails

lister()
