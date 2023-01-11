# Удаляет архивные по условию
def del_arch(name_df):
    name_df.drop(name_df[name_df['status'] == '-'].index, inplace=True)
    return name_df