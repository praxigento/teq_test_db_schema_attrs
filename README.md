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

[Read more](docs/config.md)

## Operations

### Get instance by id
Select random instance with all attributes by ID.

### Get instances by filter
Select set of instances filtered by attributes.

### Get ordered instances 
Select set of instances filtered and ordered by attributes.

### Get paged instances
Select paged set of instances filtered and ordered by attributes.