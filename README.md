# mini-project-3
Bot for the third project

![Alt text](image-1.png)

Отримує інформацію про мапу

![Alt text](image-2.png)

Отримуємо інформацію про фігуру, яку бот має розмістити


![Alt text](image-3.png)


Стратегія:
Визначається, який символ відповідає гравцю і супернику.
Фігура гравця замінюється на символ гравця.
Створюється список можливих ходів.
Визначаються позиції суперника на полі.
Для кожної можливої позиції фігури на полі розраховується кількість перекриттів з символами гравця і перевіряється, чи не перекриває фігура символи суперника.
Якщо фігура може бути розміщена на даній позиції, розраховується відстань до найближчої позиції суперника. Якщо фігура розміщується на межі території суперника, вага відстані зменшується.
Всі можливі ходи сортуються за відстанню до суперника (з урахуванням ваги), і повертається список ходів.
Ця модифікація змусить бота робити ходи більш швидкими і різкими, а після досягнення території суперника бот буде намагатися ізолювати найбільшу частину карти.
Функція повертає хід за вагою.

![Alt text](image-4.png)

Вибирає крок з можливих за допомогою функції calculate_moves

![Alt text](image-5.png)

Починає гру, отримує інформацію про ходи суперника та функція мейн