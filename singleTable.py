import pandas as pd 

category = pd.read_html("http://mnregaweb4.nic.in/netnrega/app_issue.aspx?lflag=eng&fin_year=2017-2018&source=national&labels=labels&Digest=cT/J7ChEq5LOfEr0AmsuAQ") 

category[4].to_csv('table.csv',encoding='utf-8') 
