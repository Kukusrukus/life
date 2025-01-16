import streamlit as st
import matplotlib.pyplot as plt
import numpy as np  # Добавьте этот импорт

# Функция расчёта продолжительности жизни
def calculate_life_expectancy(age, bmi, smoking, alcohol, steps, stress):
    max_life_expectancy = 120  # Максимальный возможный возраст
    base_life_expectancy = 85  # Базовая продолжительность жизни

    # Начальное значение
    life_expectancy = base_life_expectancy - (age - 40) * 0.5  # Возраст снижает базу

    # Факторы
    if bmi > 30:
        life_expectancy -= (bmi - 30) * 0.5  # Ожирение снижает
    elif bmi < 18.5:
        life_expectancy -= (18.5 - bmi) * 0.3  # Недостаток веса
    if smoking == "Да":
        life_expectancy -= 10  # Курение — большой минус
    if alcohol == "Да":
        life_expectancy -= 5  # Алкоголь снижает
    if steps < 5000:
        life_expectancy -= 3  # Малоподвижный образ жизни
    elif 8000 <= steps <= 12000:
        life_expectancy += 2  # Активность повышает
    if stress > 7:
        life_expectancy -= (stress - 7) * 2  # Высокий стресс сильно снижает

    # Ограничиваем результат
    life_expectancy = max(0, min(max_life_expectancy, life_expectancy))

    return round(life_expectancy, 1)

# Streamlit интерфейс
st.title("Прогноз продолжительности жизни")

# Ввод данных пользователем
age = st.slider("Ваш возраст", 18, 100, 30)
bmi = st.slider("Ваш индекс массы тела (BMI)", 10.0, 50.0, 22.0)
smoking = st.selectbox("Вы курите?", ["Нет", "Да"])
alcohol = st.selectbox("Вы употребляете алкоголь?", ["Нет", "Да"])
steps = st.slider("Число шагов в день", 0, 20000, 5000, step=500)
stress = st.slider("Уровень стресса (0 - нет стресса, 10 - высокий)", 0, 10, 5)

# Расчёт продолжительности жизни
life_expectancy = calculate_life_expectancy(age, bmi, smoking, alcohol, steps, stress)
remaining_years = round(life_expectancy - age, 1)

# Отображение результатов
st.subheader(f"Прогнозируемая продолжительность жизни: {life_expectancy} лет")
st.subheader(f"Прогнозируемые оставшиеся годы жизни: {remaining_years} лет")

# Рекомендации
st.markdown("### Рекомендации:")

# Преобразуем рекомендации в списки
recommendations = []

# BMI рекомендации
if bmi > 30:
    recommendations.append("❗ **Индекс массы тела выше нормы**. Рекомендуется снижение веса через здоровое питание и регулярные физические нагрузки.")
    recommendations.append("[Курс по снижению веса и здоровому питанию](https://www.coursera.org/learn/food-and-mood) - как улучшить здоровье через питание.")
elif bmi < 18.5:
    recommendations.append("❗ **Индекс массы тела слишком низкий**. Рекомендуется проконсультироваться с врачом и увеличить потребление питательных веществ.")
else:
    recommendations.append("✅ **Ваш индекс массы тела в пределах нормы**. Продолжайте вести здоровый образ жизни.")

# Курение
if smoking == "Да":
    recommendations.append("❗ **Вы курите**, что значительно сокращает продолжительность жизни. Рекомендуется бросить курить для улучшения здоровья.")
    recommendations.append("[Курс по отказу от курения](https://www.coursera.org/learn/quit-smoking) - научитесь бросать курить.")
else:
    recommendations.append("✅ **Вы не курите**, что способствует улучшению здоровья и продолжительности жизни.")

# Алкоголь
if alcohol == "Да":
    recommendations.append("❗ **Чрезмерное потребление алкоголя** может уменьшить продолжительность жизни. Рассмотрите возможность сокращения потребления.")
    recommendations.append("[Курс по отказу от алкоголя](https://www.coursera.org/learn/alcohol-abuse) - как контролировать потребление алкоголя.")
else:
    recommendations.append("✅ **Вы не употребляете алкоголь**, что положительно сказывается на вашем здоровье.")

# Шаги
if steps < 5000:
    recommendations.append("❗ **Малоподвижный образ жизни**. Рекомендуется увеличивать физическую активность, минимум 5000 шагов в день уже значительно улучшает здоровье.")
    recommendations.append("[Курс по фитнесу и физической активности](https://www.coursera.org/learn/fitness) - как начать заниматься спортом.")
elif 5000 <= steps <= 12000:
    recommendations.append("✅ **Вы в пределах нормы по физической активности**. Отличная работа!")
else:
    recommendations.append("🎯 **Вы активно занимаетесь физической активностью**! Это положительно скажется на вашем здоровье.")

# Стресс
if stress > 7:
    recommendations.append("❗ **Высокий уровень стресса** может быть вреден для здоровья. Рекомендуется применять методы снижения стресса, такие как медитация или физическая активность.")
    recommendations.append("[Курс по медитации и управлению стрессом](https://www.coursera.org/learn/meditation) - техники для управления стрессом.")
else:
    recommendations.append("✅ **Вы находитесь в пределах нормального уровня стресса**, что помогает поддерживать ваше здоровье в хорошем состоянии.")

# Отображаем рекомендации в виде списка
for recommendation in recommendations:
    st.write(recommendation)
