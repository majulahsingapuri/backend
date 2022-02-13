import os

from pydantic import BaseSettings


class Config(BaseSettings):
    secret_key: str = (
        "django-insecure-4a!3*+%!45ch^48wfay1_31u^&pci^q6(+=%59$#j$$1nvgw_q"
    )
    debug: bool = True
    allowed_hosts: list = []

    google_client_id: str = ""
    google_client_secret: str = ""

    # whether to require emails to verify their email address
    # valid values: "mandatory", "optional", or "none"
    account_email_verification: str = "none"

    # default protocol for allauth-generated URLs, either "http" or "https"
    account_default_http_protocol: str = "http"

    email_host: str = ""
    email_port: int = 587
    email_host_user: str = ""
    email_host_password: str = ""

    fe_url: str = ""
    be_url: str = ""


env_file = os.getenv("ENV_FILE", ".env")
config = Config(_env_file=env_file, _env_file_encoding="utf-8")
