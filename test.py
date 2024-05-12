import polars as pl

# Создание первого DataFrame
df1 = pl.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Создание второго DataFrame
df2 = pl.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

# Добавление данных из второго DataFrame в первый
df1 = df1.vstack(df2)

print(df1)
