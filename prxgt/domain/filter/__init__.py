__author__ = 'Alex Gusev <alex@flancer64.com>'
"""
Filter related classes (WHERE clause in SQL).

Фильтр представляет собой примерно такую структу:
    * Filter = [ConditionRule | FunctionRule]
    * ConditionRule = (Condition, Filter1, Filter2, ...)
    * Expression = [FunctionRule | Alias | Value]
    * FunctionRule = (Function, Expression1, Expression2, ...)

Т.е.,
* любой Фильтр может представлять из себя либо Правило-Условие, либо Выражение;
* Правило-Условие представляет собой некоторое Условие, применяемое к набору других Фильтров (F1 AND F2 AND F3 AND ...,
    или F1 OR F2 OR ..., или NOT F1); если нужно делать сложные условия, то получается нечто типа ((F1 AND F2) OR F3)
    или (F1 AND (F2 OR F3))
* Выражение - это либо Правило-Функция, либо некий Алиас, либо некоторое Значение; например, "order_id" - это Алиас
    атрибута, "32" - это Значение, "id > 100" - Правило-Функция;
* Правило-Функция - это сама Функция (имя функции), и набор параметров к ней, каждый из которых представляет собой
    Выражение; например, "min(order_total)": "min" - Функция, "order_total" - параметр, Выражение, которое является
    Алиасом атрибута; или "id > 1024": здесь Функция - ">", первый параметр - Алиас атрибута "id", второй -
    Значение "1024".

Алиас также может соответствовать некоторой функции SELECT'а (например, MIN):
    SELECT MIN(order.total) AS total_min FROM order WHERE total_min > 100 GROUP BY order.customer_id
"""
