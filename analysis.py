
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Загрузка данных из JSON
df = pd.read_json("events.json")

# Проверка загруженных данных
print("Первые пять записей:")
print(df.head())

print("\nИнформация о наборе данных:")
df.info()

# Анализ распределения событий по типам
event_counts = df["signature"].value_counts()

print("\nРаспределение событий по типам:")
print(event_counts)

# Построение графика
plt.figure(figsize=(12, 6))

sns.countplot(
    data=df,
    y="signature",
    order=event_counts.index
)

plt.title("Распределение событий информационной безопасности")
plt.xlabel("Количество событий")
plt.ylabel("Тип события")

plt.tight_layout()

# Сохранение графика
plt.savefig("events_distribution.png", dpi=300)

# Отображение графика
plt.show()
