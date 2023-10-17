"""
unit of work classes
"""
from __future__ import annotations


from src.blog.adapters.repositories import BlogRepository

class FCMUnitOfWork(EdgeDbUnitOfWork):
    repository_class = BlogRepository