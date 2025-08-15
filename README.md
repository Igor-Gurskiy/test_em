# Effective Mobile UI Tests

## Установка
1. Клонирование репозитория
```
git clone https://github.com/Igor-Gurskiy/test_em.git
```
```
cd test_em
```
2. Установка зависимостей
```
pip install -r requirements.txt
```
```
playwright install
```

## Запуск тестов
```
pytest tests/ -v
```

## Docker
1. Сборка образа
```
docker build -t test-em .
```
2. Запуск тестов
```
docker run test-em
```