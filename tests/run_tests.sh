#!/bin/bash
# filepath: /Users/admin/Documents/GitHub/python-sdk/tests/run_tests.sh

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Функция для запуска определенного теста
run_specific_test() {
    echo -e "${BLUE}Запуск теста: $1 ${NC}"
    python -m pytest "$1" -v
}

# Функция для запуска всех тестов в файле
run_file_tests() {
    echo -e "${BLUE}Запуск всех тестов из файла: $1 ${NC}"
    python -m pytest "$1" -v
}

# Функция для запуска всех тестов
run_all_tests() {
    echo -e "${BLUE}Запуск всех тестов ${NC}"
    python -m pytest -v
}

# Функция для вывода списка доступных тестов
list_tests() {
    echo -e "${YELLOW}Доступные файлы тестов:${NC}"
    find . -name "test_*.py" | sort
}

# Вывод справки
show_help() {
    echo -e "${GREEN}Запуск тестов для Remnawave SDK${NC}"
    echo ""
    echo "Использование:"
    echo "  ./run_tests.sh all                      - запустить все тесты"
    echo "  ./run_tests.sh list                     - показать список доступных тестов"
    echo "  ./run_tests.sh file <filename>          - запустить все тесты из указанного файла"
    echo "  ./run_tests.sh test <test_path>         - запустить указанный тест"
    echo ""
    echo "Примеры:"
    echo "  ./run_tests.sh file test_auth.py        - запустить все тесты аутентификации"
    echo "  ./run_tests.sh test test_auth.py::TestAuthentication::test_login_with_credentials"
    echo ""
}

# Основная логика скрипта
case "$1" in
    all)
        run_all_tests
        ;;
    list)
        list_tests
        ;;
    file)
        if [ -z "$2" ]; then
            echo -e "${RED}Ошибка: укажите имя файла${NC}"
            show_help
            exit 1
        fi
        run_file_tests "$2"
        ;;
    test)
        if [ -z "$2" ]; then
            echo -e "${RED}Ошибка: укажите путь к тесту${NC}"
            show_help
            exit 1
        fi
        run_specific_test "$2"
        ;;
    *)
        show_help
        ;;
esac