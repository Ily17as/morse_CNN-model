
# Morse CNN Model

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Оглавление
- [Описание](#описание)
- [Структура проекта](#структура-проекта)
- [Требования](#требования)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Обучение модели](#обучение-модели)
- [Предсказание](#предсказание)
- [Оценка результатов](#оценка-результатов)
- [Тестирование](#тестирование)
- [Contributing](#contributing)
- [Лицензия](#лицензия)

## Описание
Проект по распознаванию сигналов азбуки Морзе из аудиофайлов с помощью сверточной нейронной сети (CNN). Включает этапы предобработки данных, обучения модели и оценки результатов.

## Структура проекта
```
morse_CNN-model/
├── data/
│   ├── raw/                # Исходные (сырьевые) аудиоданные
│   └── processed/          # Обработанные данные (спектрограммы, MFCC и т.п.)
├── notebooks/              # Jupyter-ноутбуки для анализа и экспериментов
├── src/                    # Исходный код проекта
│   ├── data/               # Скрипты загрузки и предобработки данных
│   ├── models/             # Определение, обучение и сохранение моделей
│   └── utils/              # Вспомогательные функции и утилиты
├── outputs/
│   ├── models/             # Сохраненные модели (.pth)
│   └── submissions/        # Результаты предсказаний (CSV, JSON)
├── config/                 # Конфигурационные файлы (YAML)
├── tests/                  # Юнит-тесты для кода
├── requirements.txt        # Зависимости проекта
├── README.md               # Описание проекта (этот файл)
└── .gitignore              # Список игнорируемых Git-файлов
```

## Требования
- Python 3.7 или новее
- PyTorch
- NumPy, SciPy, librosa
- другие зависимости перечислены в `requirements.txt`

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Ily17as/morse_CNN-model.git
   cd morse_CNN-model
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация
Все параметры обучения и пути к данным задаются в файле `config/config.yaml`. Пример:
```yaml
data:
  raw_path: data/raw
  processed_path: data/processed
model:
  type: cnn
  input_shape: [1, 128, 128]
train:
  epochs: 50
  batch_size: 32
  learning_rate: 0.001
``` 

## Обучение модели
Для запуска обучения выполните:
```bash
python src/models/train.py \
  --config config/config.yaml
```

## Предсказание
Для получения предсказаний с обученной модели:
```bash
python src/models/predict.py \
  --model outputs/models/best_model.pth \
  --input data/processed/test_data.csv \
  --output outputs/submissions/predictions.csv
```

## Оценка результатов
Скрипт `src/models/evaluate.py` вычисляет метрики качества (точность, F1-score и т.д.). Пример запуска:
```bash
python src/models/evaluate.py \
  --predictions outputs/submissions/predictions.csv \
  --ground_truth data/processed/labels.csv
```

## Тестирование
Запуск юнит-тестов через pytest:
```bash
pytest tests/
```

## Contributing
Благодарим за вклад! Пожалуйста, откройте issue для обсуждения и отправьте pull request с вашими изменениями. Соблюдайте код-стайл и добавляйте тесты.

## Лицензия
Этот проект лицензирован под MIT License. См. файл `LICENSE` для деталей.
