def month(num, lang):
    months_en = [
        "January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"
    ]
    months_ru = [
        "Январь", "Февраль", "Март",
        "Апрель", "Май", "Июнь", "Июль",
        "Август", "Сентябрь", "Октябрь",
        "Ноябрь", "Декабрь"
    ]

    if lang == "en":
        return months_en[num - 1]
    if lang == "ru":
        return months_ru[num - 1]
