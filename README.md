# Кастомна обробка помилок 404 та 403 у Django

## Як це працює в Django

Помилкові адреси (**404**) обробляються вбудованим поданням  
`django.views.defaults.page_not_found`, яке автоматично шукає шаблон `404.html` і передає в нього контекст (в тому числі `exception`).

Для кастомної логіки достатньо підняти виняток у будь-якому view:

```python
from django.http import Http404
from django.core.exceptions import PermissionDenied

raise Http404("Сторінку не знайдено, бро")
raise PermissionDenied("Тобі сюди не можна")
```

Аналогічно для **403** — використовується `django.views.defaults.permission_denied` та шаблон `403.html`.

## Що було зроблено в проєкті

1. Створена спільна папка `templates/` на одному рівні з `manage.py`  
   (тобто в корені проєкту)

   ```
   company_site/
   ├── manage.py
   ├── templates/
   │   ├── 403.html
   │   ├── 404.html
   │   └── base.html (та інші шаблони)
   ├── core/
   ├── branches/
   └── ...
   ```

2. У цій папці створено два файли:
   - `403.html` — сторінка "Доступ заборонено"
   - `404.html` — сторінка "Сторінку не знайдено"

3. У файлі `company_site/settings.py` внесено такі зміни:

```python
# 1. Вимкнули DEBUG (обов'язково для показу кастомних 404/403)
DEBUG = False

# 2. Дозволені хости (без цього сервер не запуститься при DEBUG=False)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']      # або ['*'] для тестів

# 3. Додано шлях до кореневої папки templates у DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       ** 'DIRS': [
            os.path.join(BASE_DIR, 'templates'),   # !!! ключовий рядок!
        ],**
        'APP_DIRS': True,
        'OPTIONS'...
    },
]
```

## Результат

- При `DEBUG = True` буде стандартна технічна сторінка 404 (для розробки)
- При `DEBUG = False` буде кастомна `404.html` або `403.html`
- Винятки `Http404` та `PermissionDenied` автоматично обробляються вбудованими view

Тепер помилки виглядають професійно та дружньо до користувача.
