import pandas as pd
import ast

filename = "data/concursos_2021.05.10"
json_df = pd.read_json(filename + '.json', encoding='UTF-8')
df = json_df

#df_i = df.insolvencias.apply(pd.Series)
df_i = df.concursos.apply(pd.Series)
df_i["Company"] = [ast.literal_eval(str(x).replace("[","").replace("]","")) for x in df_i.company]
df_i_company = df_i.join(df_i.Company.apply(pd.Series))

df_i_c = df_i_company
df_i_c["Announcements"] = [ast.literal_eval(str(x).replace("[","").replace("]","")) for x in df_i_c.announcements]
df_i_c.Announcements.apply(pd.Series)
df_full = df_i_c.join(df_i_c.Announcements.apply(pd.Series))

df_full.to_csv(filename + '.csv')

