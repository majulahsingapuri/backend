from os import environ

bind = "0.0.0.0:" + environ.get("PORT", "8000")
backlog = 2048
workers = 4
timeout = 300
