import pandas as pd

raw = pd.read_csv('Florida Test.csv')
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

emails = pd.DataFrame(columns=['Company', 'Name', 'email'])

#Create list of emails from founders
space = 0
for i in range(len(df['Founders'])):
    rawIndiv = df['Founders'][i].split(', ')
    emlst = []
    companylst = []
    namelst = []
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
        temp = pd.DataFrame(dict)
        emails = pd.concat(temp, emails)


#print(emails.head())
# print(df['Founders'].head())