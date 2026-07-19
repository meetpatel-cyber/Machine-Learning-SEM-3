# Create Book DataFrame using Pandas

import pandas as pd

books = {'Title':['Book_A','Book_B','Book_C','Book_D','Book_E'],
         'Author':['AAA','BBB','CCC','DDD','EEE'],
         'price':[200,300,400,500,600],
         'Publish':[2001,2002,2003,2004,2005]}

bdf = pd.DataFrame(books)
print(bdf)