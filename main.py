mortgage

import pandas as pd
mortgage = "2017 Richey May Data_VB.xlsx"
xl = pd.ExcelFile(mortgage) <- read xlsx
df = xl.parse("Master Data") <- convert sheet to dataframe
