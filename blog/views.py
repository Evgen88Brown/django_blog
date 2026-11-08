from django.shortcuts import render
from .data import POSTS


def post_list(request):
    published = []
    page_title = "Лента публикаций"

    for post in POSTS:
        if post["is_published"]:
            published.append(post)

    return render(
        request,
        "blog/post_list.html",
        {"title": page_title, "posts": published},
    )
