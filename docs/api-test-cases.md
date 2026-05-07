# Тест кейсы к rest api модуля системы диагностики пост-травматического расстройства

baseSchoolUrl для локального окружения: 
http://localhost:8080

   Сокращение ОР: ожидаемый результат

---

   ## 1 Позитивный тест регистрации пользователя

**Регистрация пользователя с валидными данными во всех полях

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "student@gmail.com", "password": "example_password", "verify_password": "example_password"}
   ```

   ОР: в логах api сервиса отображается сгенерированный код, тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
      }
   ```

   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": "code with api service logs"}
   ```

  ОР: Тело содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "user created"
        }
      }
   ```


   - Отправить запрос авторизации на эндпоинт /user/auth

   **Example json body:**
   ```json
   {"email": "student@gmail.com", "password": "example_password"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "user",
            "accessToken": "token value"
        }
      }
   ```
   ## 2 Создание пользователя с ранее использованным email

**Регистрация пользователя с email, который использовался ранее

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "student@gmail.com", "password": "U{('D#(5wKSVo^A9'>`R'0Dc%", "verify_password": "U{('D#(5wKSVo^A9'>`R'0Dc%"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email already in use"
        }
      }
   ```

   ## 3 Создание пользователя с пустым значением в поле email


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "", "password": "U{('D#(5wKSVo^A9'>`R'0Dc%", "verify_password": "U{('D#(5wKSVo^A9'>`R'0Dc%"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should not be empty"
        }
      }
   ```

   ## 4 Создание пользователя с null значением в поле email


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": null, "password": "U{('D#(5wKSVo^A9'>`R'0Dc%", "verify_password": "U{('D#(5wKSVo^A9'>`R'0Dc%"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should not be empty"
        }
      }
   ```


   ## 5 Создание пользователя со значением email без символа @

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "etcgmail.com", "password": ";%-QWLX#B(H", "verify_password": ";%-QWLX#B(H"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should be an email"
        }
      }
   ```


   ## 6 Создание пользователя со значением email без символа .

Шаги:
   - отправить post запрос на эндпоинт /user/register


   **Example json body:**
```json
   {"email": "stiv@gmailcom", "password": ";%-QWLX#B(H", "verify_password": ";%-QWLX#B(H"}
   ```


   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should be an email"
        }
      }
   ```


   ## 7 Создание пользователя со значением email без символов @ и .

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "examplegmailcom", "password": "pomidoro", "verify_password": "pomidoro"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should be an email"
        }
      }
   ```

   ### 8 Создание пользователя с паролем в 6 символов
**Анализ негативных граничных значений длины пароля, недопустимое значение пароля в 6 символов

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "128@gmail.com", "password": "tomato", "verify_password": "tomato"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "Password must be between 7 and 30 characters"
        }
      }
   ```


   ### 9 Создание пользователя с паролем в 7 символов
**Анализ граничных значений длины пароля, допустимое значение пароля в 7 символов

Шаги:
   - Отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "albukerke@cloud.com", "password": "testing", "verify_password": "testing"}
   ```

   ОР: в логах api сервиса отображается сгенерированный код, тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
      }
   ```

   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": "code with api service logs"}
   ```

   ОР: Тело содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "user created"
        }
      }
   ```


   - Отправить запрос авторизации на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": "albukerke@cloud.com", "password": "testing"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "user",
            "accessToken": "token value"
        }
      }
   ```

   ## 10 Создание пользователя с паролем в 8 символов
**Анализ граничных значений длины пароля, допустимое значение пароля в 8 символов

Шаги:
   - Отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "eshly@gmail.com", "password": "acapulka", "verify_password": "acapulka"}
   ```

   ОР: в логах api сервиса отображается сгенерированный код, тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
      }
   ```

   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": "code with api service logs"}
   ```

   ОР: Тело содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "user created"
        }
      }
   ```


   -    - Отправить post запрос авторизации на эндпоинт /user/auth

   **Example json body:**
```json
   {"email": "eshly@gmail.com", "password": "acapulka"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "user",
            "accessToken": "token value"
        }
      }
   ```

   ## 11 Создание пользователя с паролем в 29 символов
**Анализ граничных значений длины пароля, допустимое значение пароля в 29 символов

Шаги:
   - Отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "aliceStenf@domain.co", "password": "X{tt^R#hcfC(qj4zgFw!VEUx[Cf<y", "verify_password": "X{tt^R#hcfC(qj4zgFw!VEUx[Cf<y"}
   ```

   ОР: в логах api сервиса отображается сгенерированный код, тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
      }
   ```

   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": "code with api service logs"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "user created"
        }
      }
   ```

   -    - Отправить post запрос авторизации на эндпоинт /user/auth

   **Example json body:**
```json
   {"email": "aliceStenf@domain.co", "password": "X{tt^R#hcfC(qj4zgFw!VEUx[Cf<y"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "user",
            "accessToken": "token value"
        }
      }
   ```


   ## 12 Создание пользователя с паролем в 30 символов
**Анализ граничных значений длины пароля, допустимое значение пароля в 30 символов

Шаги:
   - Отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "premium-bagels@testDomain.us", "password": "r/1n;m{No;%@PLGm@mrOQ!D_Uy:OF~", "verify_password": "r/1n;m{No;%@PLGm@mrOQ!D_Uy:OF~"}
   ```

   ОР: в логах api сервиса отображается сгенерированный код, тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
      }
   ```

   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": "code with api service logs"}
   ```

   ОР: Тело содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "user created"
        }
      }
   ```

   -    - Отправить post запрос авторизации на эндпоинт /user/auth

   **Example json body:**
```json
   {"email": "premium-bagels@testDomain.us", "password": "r/1n;m{No;%@PLGm@mrOQ!D_Uy:OF~"}
   ```

   Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "user",
            "accessToken": "token value"
        }
      }
   ```


   ## 13 Создание пользователя с паролем в 31 символ
**Анализ негативных граничных значений длины пароля, недопустимое значение пароля в 31 символ

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "visual@inbox.org", "password": "Bq:>mB+YUME{2s]weJ6;j?l>WRc!(&V", "verify_password": "Bq:>mB+YUME{2s]weJ6;j?l>WRc!(&V"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "Password must be between 7 and 30 characters"
        }
      }
   ```


   ## 14 Создание пользователя со значением пароля из символов кириллицы

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "visual_user@domain.com", "password": "метро", "verify_password": "метро"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "invalid format of password"
        }
      }
   ```


   ## 15 Создание пользователя со значением пароля из символов латиницы и кириллицы

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "flour@rambler.su", "password": "passwordпароль", "verify_password": "passwordпароль"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "invalid format of password"
        }
      }
   ```

   ## 16 Создание пользователя со значением пароля из  спец символов и символов пробела

Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
```json
   {"email": "secret@exampleDomain.com", "password": "!`~_;.@#  ^", "verify_password": "!`~_;.@#  ^"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "invalid format of password"
        }
      }
   ```

   ## 17 Создание пользователя с пустым значением в поле password


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "email@electro.su", "password": "", "verify_password": "U{('D#(5wKSVo>"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "password should not be empty"
        }
      }
   ```

   ## 18 Создание пользователя с null значением в поле password


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "email@electro.su", "password": null, "verify_password": "U{('D#(5wKSVo>"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "password should not be empty"
        }
      }
   ```

   ## 19 Создание пользователя с разными значениями в полях password и verify_password


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "email@electro.su", "password": "U{('D#(5wKSVo>", "verify_password": "U{('D#(5wKSVo"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "input passwords don't match"
        }
      }
   ```

   ## 20 Создание пользователя с пустым значением в поле verify_password


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "email@electro.su", "password": "U{('D#(5wKSVo>", "verify_password": ""}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "input passwords don't match"
        }
      }
   ```


   ## 21 Создание пользователя с null значением в поле verify_password


Шаги:
   - отправить post запрос на эндпоинт /user/register

   **Example json body:**
   ```json
      {"email": "email@electro.su", "password": "U{('D#(5wKSVo>", "verify_password": null}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "input passwords don't match"
        }
      }
   ```

   ## 22 Активация пользователя с пустым значением в поле activation_code

   Предусловие: пользователь отправил запрос с корректными данными на регистрацию, код активации отображается в логах

   Шаги:
   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": ""}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "activation code is required"
        }
      }
   ```

   ## 23 Активация пользователя с null значением в поле activation_code

   Предусловие: пользователь отправил запрос с корректными данными на регистрацию, код активации отображается в логах

   Шаги:
   - Отправить post запрос на эндпоинт /user/activate

   **Example json body:**
   ```json
   {"activation_code": null}
   ```

   Тело содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "activation code is required"
        }
      }
   ```

   ## 24 Активация пользователя со  значением в поле activation_code, несовпадающим со значением в логах

   Предусловие: пользователь отправил запрос с корректными данными на регистрацию, код активации отображается в логах

   Шаги:
   - Отправить post запрос на эндпоинт /user/activate с некорректным значением кода активации

   **Example json body:**
   ```json
   {"activation_code": "unknown code"}
   ```

   ОР: Тело содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "invalid activation code"
        }
      }
   ```

   ## 25 Авторизация пользователя с ролью admin (тестовый аккаунт)

   Шаги:
   - Отправить запрос авторизации на эндпоинт /user/auth

   **Example json body:**
   ```json
   {"email": "example@domain.com", "password": "1234"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "role": "admin",
            "access_token": "token value",
            "refresh_token": "token value"
        }
      }
   ```

   ## 26 Авторизация пользователя с некорректными данными (валидный email, невалидный пароль)

   Предусловие: Используется существующий тестовый аккаунт администратора

   Шаги:
   - отправить post запрос на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": "example@domain.com", "password": "12349"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "invalid credantials"
        }
      }
   ```

   ## 27 Авторизация пользователя с пустым значением в поле email

   Предусловие: Используется существующий тестовый аккаунт администратора

   Шаги:
   - отправить post запрос на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": "", "password": "1234"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should not be empty"
        }
      }
   ```

   ## 28 Авторизация пользователя с null значением в поле email

   Предусловие: Используется существующий тестовый аккаунт администратора

Шаги:
   - отправить post запрос на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": null, "password": "1234"}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "email should not be empty"
        }
      }
   ```

   ## 29 Авторизация пользователя с пустым значением в поле password

   Предусловие: Используется существующий тестовый аккаунт администратора

   Шаги:
   - отправить post запрос на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": "example@domain.com", "password": ""}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "password should not be empty"
        }
      }
   ```

   ## 30 Авторизация пользователя с null значением в поле password

   Предусловие: Используется существующий тестовый аккаунт администратора

Шаги:
   - отправить post запрос на эндпоинт /user/auth

   **Example json body:**
   ```json
      {"email": "example@domain.com", "password": null}
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": False,
        "status": 400,
        "data": {
            "error_message": "password should not be empty"
        }
      }
   ```

   ## 31 Добавление вопроса – позитивный тест

   Предусловие: Пользователь отправил запрос на авторизацию с ролью admin

   Шаги:
   - Отправить post запрос на эндпоинт /questions, в заголовки добавить – Authorization bearer your_access_token_value

   **Example json body:**
   ```json
   {
      "text": "Example question",
      "answers": [
      {
        "variant": "Variant1",
        "score": 1,
        "position": 1
      },
      {
        "variant": "variant2",
        "score": 2,
        "position": 2
      }
      ]
   }
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
        "success": True,
        "status": 200,
        "data": {
            "message": "question inserted"
        }
      }
   ```

   - Отправить get запрос на эндпоинт /questions, в заголовки добавить токен авторизации админа

   ОР: Список вопросов содержит больше нуля элементов, в списке отображается ранее добавленный вопрос

   ## 32 Добавление вопроса без токена авторизации в заголовках

   Шаги:
   - Отправить post запрос на эндпоинт /questions без заголовка Authorization bearer your_access_token_value

   **Example json body:**
   ```json
   {
      "text": "Example question",
      "answers": [
      {
        "variant": "Variant1",
        "score": 1,
        "position": 1
      },
      {
        "variant": "variant2",
        "score": 2,
        "position": 2
      }
      ]
   }
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
      "detail": "forbidden for this user"
      }
   ```

   ## 33 Добавление вопроса с токеном авторизации в заголовках, идентифицирующего пользователя с ролью user

   Предусловие: Пользователь отправил запрос на авторизацию с ролью user

   Шаги:
   - Отправить post запрос на эндпоинт /questions, в заголовки добавить – Authorization bearer your_access_token_value

   **Example json body:**
   ```json
   {
      "text": "Example question",
      "answers": [
      {
        "variant": "Variant1",
        "score": 1,
        "position": 1
      },
      {
        "variant": "variant2",
        "score": 2,
        "position": 2
      }
      ]
   }
   ```

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
      "detail": "forbidden for this user"
      }
   ```

   ## 34 Удаление вопроса – позитивный тест

   Предусловие: Пользователь отправил запрос на авторизацию с ролью admin

   Шаги:
   - Отправить delete запрос на эндпоинт /questions/1, в заголовки добавить – Authorization bearer your_access_token_value

   ОР: Тело ответа не содержит данных, ответ приходит со статускодом 204

   ## 35 Удаление Не существующего вопроса 

   Предусловие: Пользователь отправил запрос на авторизацию с ролью admin

   Шаги:
   - Отправить delete запрос на эндпоинт /questions/220, в заголовки добавить – Authorization bearer your_access_token_value

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
      "detail": "question not found"
      }
   ```

   ## 36 Удаление вопроса без токена авторизации

   Шаги:
   - Отправить delete запрос на эндпоинт /questions/1 без токена авторизации в заголовках

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
      "detail": "token is required"
      }
   ```

   ## 37 Удаление вопроса с токеном авторизации в заголовках, идентифицирующего пользователя с ролью user

   Предусловие: Пользователь отправил запрос на авторизацию с ролью user

   Шаги:
   - Отправить delete запрос на эндпоинт /questions/1, в заголовки добавить – Authorization bearer your_access_token_value

   ОР: Тело ответа содержит следующие данные:
   ```json
      {
      "detail": "forbidden for this user"
      }
   ```
