from typing import Any, Dict

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    TESTING_ENV: bool = False
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    DB_DSN: str

    @validator("DB_DSN", pre=True)
    def assemble_db_connection(cls, v: str, values: Dict[str, Any]) -> Any:
        if values.get("TESTING_ENV"):
            return f"{v}_test"

        return v

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
