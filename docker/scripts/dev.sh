#!/bin/bash

# Make the script executable from anywhere
cd "$(dirname "$0")/../.." || exit

# Command to run tests
run_tests() {
    docker compose run --rm test
}

# Command to create superuser
create_superuser() {
    docker compose exec app python manage.py createsuperuser
}

# Command to run migrations
run_migrations() {
    docker compose exec app python manage.py migrate
}

# Command to make migrations
make_migrations() {
    docker compose exec app python manage.py makemigrations
}

# Command to open a Django shell
django_shell() {
    docker compose exec app python manage.py shell_plus
}

# Command to show logs
show_logs() {
    docker compose logs -f "$1"
}

# Display help
show_help() {
    echo "Development helper script"
    echo "Usage: ./docker/scripts/dev.sh [command]"
    echo ""
    echo "Commands:"
    echo "  test            Run tests"
    echo "  superuser       Create superuser"
    echo "  migrate         Run migrations"
    echo "  makemigrations  Make migrations"
    echo "  shell           Open Django shell"
    echo "  logs [service]  Show logs (optional: specify service name)"
    echo "  help            Show this help message"
}

# Process command line arguments
case "$1" in
    test)
        run_tests
        ;;
    superuser)
        create_superuser
        ;;
    migrate)
        run_migrations
        ;;
    makemigrations)
        make_migrations
        ;;
    shell)
        django_shell
        ;;
    logs)
        show_logs "$2"
        ;;
    help|*)
        show_help
        ;;
esac