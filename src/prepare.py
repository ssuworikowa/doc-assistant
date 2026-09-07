import pandas as pd
import os

def main():
    print("Запуск пайплайна очистки данных...")

    # Получаем путь к папке, где лежит сам скрипт prepare.py (то есть к папке src)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Пути к файлам
    #input_path = "data\\raw\\data.csv"
    # Корректно собираем путь к файлу: выходим из src, заходим в data/raw/data.csv
    input_path = os.path.join(current_dir, "..", "data", "raw", "data.csv")
    output_dir = "data/processed"
    output_path = os.path.join(output_dir, "clean.csv")

    # Проверяем наличие папки для сохранения
    os.makedirs(output_dir, exist_ok=True)

    # Шаги обработки
    df = pd.read_csv(input_path)
    df = df.dropna(subset=["text"]).drop_duplicates(subset=["text"])
    df["text"] = df["text"].str.strip().str.replace(r"\s+", " ", regex=True)
    df = df[df["text"].str.len() > 50]

    # Сохранение результата
    df.to_csv(output_path, index=False)
    print(f"Готово: {len(df)} документов -> {output_path}")

if __name__ == "__main__":
    main()