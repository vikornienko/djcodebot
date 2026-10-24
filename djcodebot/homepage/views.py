# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    lang_list: list[str] = [
        "markup",
        "css",
        "clike",
        "javascript",
        "Django",
        "makefile",
        "markdown",
        "markup-templating",
        "plsql",
        "python",
        "rust",
        "sql",
        "toml",
        "typescript",
        "yaml",
    ]

    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]
        return render(
            request, "home.html", {"lang_list": lang_list, "code": code, "lang": lang}
        )
    return render(request, "home.html", {"lang_list": lang_list})
