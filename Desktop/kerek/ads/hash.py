def rabin_karp(text, pattern):
  """
  Ищет подстроку pattern в строке text.

  Args:
    text: Строка, в которой мы ищем подстроку.
    pattern: Подстрока, которую мы ищем.

  Returns:
    Индекс первого символа подстроки pattern в строке text, если она найдена,
    или None, если она не найдена.
  """

  # Вычисляем хэш-значение для подстроки pattern.
  pattern_hash = hash(pattern)

  # Итерируемся по строке text.
  for i in range(len(text)):
    # Вычисляем хэш-значение для подстроки, начинающейся с символа i в строке text.
    text_hash = hash(text[i:i + len(pattern)])

    # Если хэш-значения совпадают, проверяем, совпадают ли остальные символы подстроки.
    if pattern_hash == text_hash:
      # Если остальные символы подстроки также совпадают, мы нашли совпадение.
      for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
          break
      else:
        return i

  return None