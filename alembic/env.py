# alembic/env.py
from logging.config import fileConfig
from sqlalchemy.engine import Connection
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.db.base import Base  # imports all your models
from app.core.config import get_settings

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata

settings = get_settings()

# Use your async URL (works fine – Alembic syncs it internally)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL.replace("+asyncpg", "+psycopg"))

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,        # detects column type changes
            compare_server_default=True,
            include_schemas=True,     # if you use multiple schemas
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    ## run_migrations_offline()
else:
    run_migrations_online()