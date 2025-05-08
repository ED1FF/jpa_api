# Run Project
docker compose up --build
docker compose exec api aerich upgrade

# Work with aerich
aerich migrate --name drop_column
docker compose exec api aerich migrate
docker compose exec api aerich downgrade
