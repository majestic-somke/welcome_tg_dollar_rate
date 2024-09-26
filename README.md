1. **Создайте локально новый проект**. В качестве интерпретатора используйте **Python 3.10** или выше.
2. **Создайте виртуальное окружение** в корне вашего проекта:
   ```bash
   python -m venv venv
3. **Активируйте виртуальное окружение**:
   ```bash
   venv\Scripts\activate
4. **Загрузите проект с github** используя:
   ```bash  
   git clone https://github.com/majestic-somke/welcome_tg_dollar_rate.git
5. **Перейдите в директорию клонированного репозитория**:
   ```bash
   cd welcome_tg_dollar_rate
6. **Создайте файл с названием** - ".env.dev" в директории **welcome_tg_dollar_rate**.
7. **Поместите токен своего телеграм бота в созданный файл.** Пример:
    ```plaintext
    TG_TOKEN="YOUR_TOKEN_HERE"
8. **Установите необходимые библиотеки**, введя в терминале:
   ```bash
   pip install -r requirements.txt
9. **Запустите бота**, введя в терминале:
   ```bash
   python main.py  
 
