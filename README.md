# Run Project
docker compose up --build
docker compose exec api aerich init-db
docker compose exec api aerich migrate
