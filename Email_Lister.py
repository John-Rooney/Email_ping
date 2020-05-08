def lister():

    import pandas as pd
    lst=input('Which List:')
    raw = pd.read_csv(lst)
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


    #Create list of emails from founders
    space = 0
    dict = {}
    emlst = []
    companylst = []
    namelst = []
    for i in range(len(df['Founders'])):
        rawIndiv = df['Founders'][i].split(', ')
        for a in rawIndiv:
            space = a.index(' ')
            #First@domain
            emlst.append((a[:space]+'@'+df['Domain'][i]).lower())
            companylst.append(df['Organization Name'][i])
            namelst.append(a)
            #First.Last
            emlst.append((a[:space]+'.'+a[space+1:]+'@'+df['Domain'][i]).lower())
            companylst.append(df['Organization Name'][i])
            namelst.append(a)
            #FirstLast
            emlst.append((a[:space]+a[space + 1:]+'@'+df['Domain'][i]).lower())
            companylst.append(df['Organization Name'][i])
            namelst.append(a)
            #First[0]Last
            emlst.append((a[0]+a[space + 1:]+'@'+df['Domain'][i]).lower())
            companylst.append(df['Organization Name'][i])
            namelst.append(a)
            #First[0].Last
            emlst.append((a[0] + '.' + a[space + 1:] + '@' + df['Domain'][i]).lower())
            companylst.append(df['Organization Name'][i])
            namelst.append(a)
            dict = {'Company':companylst, 'Name':namelst, 'Email':emlst}

    emails = pd.DataFrame(dict)
    #print(emails.head())
    #emails.to_csv('TestResults.csv', index=False)

    return emails