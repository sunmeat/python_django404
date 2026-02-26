import time
from django.http import HttpResponse

# функціональний middleware — логування запитів
def log_requests(get_response):
    """Логує кожен запит: метод, шлях, час виконання, статус відповіді"""
    
    def middleware(request):
        start_time = time.time()
        
        # тут можна щось додати до request, наприклад
        # request.custom_info = "Цей рядок доданий в middleware!"
        
        response = get_response(request)
        
        # після обробки view
        duration = time.time() - start_time
        status = response.status_code
        
        # друкуємо в консоль (можна замінити на логування в файл)
        print(f"[{status}] {request.method} {request.path} — {duration:.3f} секунд. Привіт із мідлварі!")
        
        return response
    
    return middleware


# класовий middleware — додає кастомний заголовок до всіх відповідей
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # додаємо свій заголовок (можна будь-яку логіку)
        response['X-Powered-By'] = 'Sunmeat 26/02/2026'
        response['X-Company-Name'] = 'Sunmeat Inc.'
        
        return response