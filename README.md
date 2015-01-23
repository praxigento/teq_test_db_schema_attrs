# Test different DB structures

Test environment for comparison of the different schemas for entity with variable count of the attributes.

В качестве модели рассматривается одна Сущность, имеющая достаточно большое количество Атрибутов. При этом каждый 
отдельный экземпляр Сущности имеет лишь часть из этих Атрибутов. Примером может служить сущность Продукт в сфере 
электронной коммерции - например, техника и одежда имеют совершенно различные атрибуты. 

В данном проекте делается попытка оценить различные варианты представления подобных данных на уровне БД. Моделируется
предметная область (domain), состоящая из одной Сущности. Задаются характеристики генерации отдельных экземпляров 
(общее количество экземпляров, минимальное и максимальное количество атрибутов у одного экземпляра, доступные типы 
атриубтов, общее возможное количество различных атрибутов и т.п.).

Предметная область заполняется данными, согласно заданной конфигурации, а затем моделируются типовые запросы к данным
(получить отдельный экземпляр со всеми доступными атрибутами, получить список экземпляров с фильтрацией, сортировкой,
постраничной разбивкой) и оценивается время их выполнения.



## Configuration file

    {
        "domain": {},
        "operations": {}
    }

### Domain definition

    "domain": {
            "attrs_total": 50,
            "attrs_per_instance_min": 2,
            "attrs_per_instance_max": 10,
            "attr_types": {
                "int": {},
                "decimal": {},
                "string": {},
                "text": {}
            },
            "instances_total": 10
    }

* **attrs_total**: total number of the all

### Data manipulations

    "operations": {
        "get_instance": {
            "count": 100
        },
        "get_by_filter": {
            "count": 100,
            "attrs_in_filter_max": 5
        },
        "get_sorted": {
            "count": 100,
            "attrs_to_sort_max": 5
        },
        "get_paged": {
            "count": 100,
            "attrs_in_filter_max": 4,
            "attrs_to_sort_max": 3,
            "page_size": 10
        }
    }