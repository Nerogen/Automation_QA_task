#### Task description 📝
    С помощью инструментов тестирования Selenium WebDriver (from selenium import webdriver)
    и Pytest (import pytest) необходимо создать тест, содержащий данные шаги и проверки, описанные ниже.
1. Перейти по ссылке https://www.a1.by/ru/shop/c/phones
2. На странице выбрать случайным образом блок со смартфоном и нажать на кнопку «Перейти к покупке»
![image](https://user-images.githubusercontent.com/72101790/199803565-95910456-4514-47ea-a58f-2e2f7f1ca153.png)
3. Справа из выпадающего списка выбрать вариант оплаты в рассрочку на 6 месяцев: «6 мес по ххх руб/мес»
![image](https://user-images.githubusercontent.com/72101790/199803794-2efd60ae-cd14-4379-a588-9314793b621d.png)
4. Нажать кнопку «Войти и купить»
![image](https://user-images.githubusercontent.com/72101790/199803979-3041b31c-4805-43de-b218-904d1e4fea5d.png)
5. Вывести сообщение с названием выбранного оборудования и текст выбранного варианта оплаты, включая стоимость.
(Например: «Выбран Xiaomi 11T 128GB небесный голубой, вариант оплаты: 6 мес по 229,82 руб/мес»)


#### Usage ▶️
    run module "test_ui" in IDE (automatioly configure start for pytest)

#### Example of output ✨
    Выбран Vivo Y22 64GB синий космос [V2207], вариант оплаты: 6 мес по 93,16 руб/мес'