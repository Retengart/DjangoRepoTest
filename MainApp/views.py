from django.shortcuts import render, HttpResponse, Http404

name = "*****"
surname = "******"
email = "*****"
phone = ".........."


def home(request):
    return render(request, "index.html")


def about(request):
    info = f"Автор: {name} {surname}"
    return HttpResponse(info)


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]


def item_page(request, id):
    for item in items:
        if item["id"] == id:
            # items_str = f"товар {item['name']} количество {item['quantity']}"
            # return HttpResponse(items_str)
            return render(request, "item_page.html", item)
    raise Http404(f"Товар c id = {id} не найден")


def item_list(request):
    items_result = "<ol>"
    for item in items:
        items_result += "<li>" + f"<a href = '/item{item['id']}'>" + item['name'] + "</a>" + "</li>"
    items_result += "</ol>"
    return HttpResponse(items_result)
