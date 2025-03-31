import json
import time
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import ErrorReport
from .models import Cabinets
from .algorithm.usingLocation import getFrameRu, getFrameEn
from .algorithm.map_routing import MapRouting

# Константы для ограничений
MESSAGE_RESTRICTION_END_TIME = 3600  # 1 час в секундах
MAX_MESSAGES_PER_IP = 3  # Максимальное количество сообщений за период
MAX_DESCRIPTION_LENGTH = 500  # Максимальная длина описания
ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png', 'image/jpg']  # Разрешенные типы файлов
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

svg_url1 = f"https://map.spbgasu.ru/images/maps/{2}.svg"
startingMap = requests.get(svg_url1).text

def UserLocationRU(request, location_id):
    try:
        location = Cabinets.objects.get(cabinetsId=location_id)
        context = {
            "htmlLanguage": "ru",
            "language": "En",
            "indexTitle": "Схема ГАСУ | Интерактивная карта СПбГАСУ",
            "buildingName": "Главный корпус",
            "search": "поиск...",
            "errorMessage": "Сообщение об ошибке",
            "userName": "Имя",
            "namePlaceholder": "Введите имя",
            "problemPlaceholder": f"Опишите проблему (Максимум {MAX_DESCRIPTION_LENGTH} символов)",
            "userProblem": "Проблема",
            "userImg": "Фотографии",
            "userSend": "Отправить",
            "routeTitle": "Маршрут",
            "allResults": "Все результаты",
            "NoResults": "Ничего не найдено",
            "frequentRequests": "Частые запросы",
            "diningRoom": "Столовая",
            "womenToilet": "Женский туалет",
            "menToilet": "Мужской туалет",
            "recentRequests": "Недавние запросы",
            "clearCabinets": "Очистить",
            "cabinetName": location.cabinetsName,
            "startPlaceholder": "Текущее местоположение",
            "endPlaceholder": "Куда направляетесь?",
            "map": startingMap,
        }
        return render(request, "map/index.html", context)
    except:
        context = {
            'title': "Несуществующая локация",
            'message': "Изменение параметра location, может привести к непредсказуемым последствиям :(",
            'name_button': 'На главную',
        }
        return render(request, "message/error.html", context)

def UserLocationEN(request, location_id):
    try:
        svg_url1 = f"https://map.spbgasu.ru/images/maps/{2}.svg"
        startingMap = requests.get(svg_url1).text
        location = Cabinets.objects.get(cabinetsId__exact=location_id)
        context = {
            "htmlLanguage": "en",
            "language": "Ру",
            "indexTitle": "GASU scheme | Interactive map of St. Petersburg State University",
            "buildingName": "Main building",
            "search": "search....",
            "errorMessage": "Error message",
            "userName": "Name",
            "namePlaceholder": "Enter a name",
            "userProblem": "Problem",
            "problemPlaceholder": f"Describe the problem (Maximum {MAX_DESCRIPTION_LENGTH} characters)",
            "userImg": "Photo",
            "userSend": "Send",
            "routeTitle": "Route",
            "allResults": "All results",
            "NoResults": "Nothing was found",
            "frequentRequests": "Frequent requests",
            "diningRoom": "Canteen",
            "womenToilet": "Women's restroom",
            "menToilet": "Men's restroom",
            "recentRequests": "Recent requests",
            "clearCabinets": "Clear",
            "cabinetName": location.cabinetsName,
            "startPlaceholder": "Current location",
            "endPlaceholder": "Where are you going?",
            "map": startingMap,
        }
        return render(request, "map/index.html", context)
    except:
        context = {
            'title': "Non-existent location",
            'message': "Changing the location parameter may lead to unpredictable consequences :(",
            'name_button': 'Go to Home',
        }
        return render(request, "message/error.html", context)


def UserRU(request):
    context = {
        "htmlLanguage": "ru",
        "language": "En",
        "indexTitle": "Схема ГАСУ | Интерактивная карта СПбГАСУ",
        "buildingName": "Главный корпус",
        "search": "поиск...",
        "errorMessage": "Сообщение об ошибке",
        "userName": "Имя",
        "namePlaceholder": "Введите имя",
        "problemPlaceholder": f"Опишите проблему (Максимум {MAX_DESCRIPTION_LENGTH} символов)",
        "userProblem": "Проблема",
        "userImg": "Фотографии",
        "userSend": "Отправить",
        "routeTitle": "Маршрут",
        "allResults": "Все результаты",
        "NoResults": "Ничего не найдено",
        "frequentRequests": "Частые запросы",
        "diningRoom": "Столовая",
        "womenToilet": "Женский туалет",
        "menToilet": "Мужской туалет",
        "recentRequests": "Недавние запросы",
        "clearCabinets": "Очистить",
        "startPlaceholder": "Текущее местоположение",
        "endPlaceholder": "Куда направляетесь?",
        "map": startingMap,
    }
    return render(request, "map/index.html", context)

def UserEN(request):
    context = {
        "htmlLanguage": "en",
        "language": "Ру",
        "indexTitle": "GASU scheme | Interactive map of St. Petersburg State University",
        "buildingName": "Main building",
        "search": "search....",
        "errorMessage": "Error message",
        "userName": "Name",
        "namePlaceholder": "Enter a name",
        "userProblem": "Problem",
        "problemPlaceholder": f"Describe the problem (Maximum {MAX_DESCRIPTION_LENGTH} characters)",
        "userImg": "Photo",
        "userSend": "Send",
        "routeTitle": "Route",
        "allResults": "All results",
        "NoResults": "Nothing was found",
        "frequentRequests": "Frequent requests",
        "diningRoom": "Canteen",
        "womenToilet": "Women's restroom",
        "menToilet": "Men's restroom",
        "recentRequests": "Recent requests",
        "clearCabinets": "Clear",
        "startPlaceholder": "Current location",
        "endPlaceholder": "Where are you going?",
        "map": startingMap,
    }
    return render(request, "map/index.html", context)


def HomePage(request):
    return render(request, "main.html")


# получение и запись в SQL сообщений об ошибке
@ensure_csrf_cookie
def create_error_report(request):

    if request.method != "POST":
        return JsonResponse({"error": "Метод запроса не поддерживается"}, status=405)

    try:
        # Получаем IP-адрес пользователя
        user_ip = request.META.get("REMOTE_ADDR")
        if not user_ip:
            return JsonResponse({"error": "Не удалось определить IP-адрес"}, status=400)

        # Получаем список сообщений, отправленных с этого IP за последний час
        cache_key = f"error_reports:{user_ip}"
        messages = cache.get(cache_key, [])

        # Фильтруем старые сообщения (старше 1 часа)
        current_time = time.time()
        messages = [msg_time for msg_time in messages if current_time - msg_time <= MESSAGE_RESTRICTION_END_TIME]

        # Если лимит сообщений превышен, возвращаем ошибку
        if len(messages) >= MAX_MESSAGES_PER_IP:
            return JsonResponse(
                {"error": "Вы превысили лимит отправки сообщений. Попробуйте снова, через 1 час."},
                status=403,
            )

        # Добавляем текущее время в список сообщений
        messages.append(current_time)
        cache.set(cache_key, messages, timeout=MESSAGE_RESTRICTION_END_TIME)

        # Загружаем данные из тела запроса
        user = request.POST.get("user", "")
        description = request.POST.get("description", "")

        # Проверяем длину описания
        if len(description) > MAX_DESCRIPTION_LENGTH:
            return JsonResponse(
                {"error": f"Сообщение слишком большое! Максимальная длина: {MAX_DESCRIPTION_LENGTH} символов."},
                status=400,
            )

        # Обработка файла, если он есть
        uploaded_file = None
        if 'file' in request.FILES:
            file = request.FILES['file']

            # Проверка типа файла
            if file.content_type not in ALLOWED_FILE_TYPES:
                return JsonResponse({"error": "Недопустимый тип файла"}, status=400)

            # Проверка размера файла
            if file.size > MAX_FILE_SIZE:
                return JsonResponse({"error": "Файл слишком большой. Максимальный размер: 10 МБ"}, status=400)

            uploaded_file = file

        # Создаем новый отчет об ошибке
        error_report = ErrorReport.objects.create(
            user=user,
            description=description,
            file=uploaded_file,  # Сохраняем файл, если он был загружен
        )

        return JsonResponse(
            {"message": "Спасибо, что помогаете нам стать лучше!"},
            status=201,
        )

    except Exception as e:
        return JsonResponse({"error": f"Произошла ошибка: {str(e)}"}, status=500)
# def create_error_report(request):
#     message_restriction_end_time = 3600
#     if request.method == "POST":
#         try:
#             # Получаем IP-адрес пользователя
#             user_ip = request.META.get("REMOTE_ADDR")
#
#             # Получаем список сообщений, отправленных с этого IP за последние 10 минут
#             cache_key = f"error_reports:{user_ip}"
#             messages = cache.get(cache_key, [])
#
#             # Фильтруем старые сообщения, которые были отправлены более 10 минут назад
#             ten_minutes_ago = time.time() - message_restriction_end_time
#             messages = [msg_time for msg_time in messages if msg_time > ten_minutes_ago]
#
#             # Если сообщений больше 3, блокируем отправку на 1 час
#             if len(messages) >= 3:
#                 return JsonResponse(
#                     {
#                         "error": f"Вы превысили лимит отправки сообщений. Попробуйте снова через 10 минут."
#                     },
#                     status=403,
#                 )
#
#             # Добавляем время отправки сообщения в список
#             messages.append(time.time())
#             cache.set(
#                 cache_key, messages, timeout=message_restriction_end_time
#             )  # Храним список сообщений в кеше 1 час
#
#             # Загружаем данные из тела запроса
#             data = json.loads(request.body)
#             user = data.get("user", "")
#             description = data.get("description", "")
#
#             if len(description) > 500:
#                 return JsonResponse(
#                     {
#                         "error": "Сообщение слишком большое! Повторите попытку...",
#                     },
#                     status=201,
#                 )
#             # Создаем новый отчет об ошибке
#             error_report = ErrorReport.objects.create(
#                 user=user,
#                 description=description,
#             )
#
#             return JsonResponse(
#                 {
#                     "message": "Сообщение успешно отправлено! Спасибо, что помогаете нам стать лучше!",
#                 },
#                 status=201,
#             )
#
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#
#     return JsonResponse({"error": "Ошибка запроса"}, status=405)


@ensure_csrf_cookie
def search_location(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            cabinet_name = data.get("cabinet", "").strip().upper()
            language = data.get("language", "")
            results = Cabinets.objects.filter(cabinetsName__icontains=cabinet_name)

            if not results.exists() or len(cabinet_name) == 0:
                return JsonResponse({"results": []}, status=200)

            if (language == 'ru'):
                response_data = [
                    {"nameCabinet": cabinet.cabinetsName, "frame":getFrameRu(cabinet.cabinetsId), "location": cabinet.cabinetsId}
                    for cabinet in results
                ]
                return JsonResponse({"results": response_data}, status=200)
            else:
                response_data = [
                    {"nameCabinet": cabinet.cabinetsName, "frame": getFrameEn(cabinet.cabinetsId),
                     "location": cabinet.cabinetsId}
                    for cabinet in results
                ]
                return JsonResponse({"results": response_data}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@ensure_csrf_cookie
def getMapFromPoints(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            location_start = data.get("location_start")
            location_end = data.get("location_end")

            if not (Cabinets.objects.filter(cabinetsId=location_start).exists() and
                    Cabinets.objects.filter(cabinetsId=location_end).exists()):
                return JsonResponse({"error": "Invalid location"}, status=400)
            if location_start == location_end:
                return JsonResponse({"error": "the beginning and the end cannot be at the same point"}, status=400)

            return JsonResponse({"results": MapRouting(location_start, location_end)}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)