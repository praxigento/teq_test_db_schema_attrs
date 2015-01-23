# Configuration file

## Overview
Configuration file `config.json` contains all parameters to generate data in domain, to perform test operations and
to save results.

## Structure

    {
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
            "instances_total": 100
        },
        "operations": {
            "get_instance": {
                "count": 100
            },
            "get_by_filter": {
                "count": 100,
                "attrs_in_filter_max": 5
            },
            "get_ordered": {
                "count": 100,
                "attrs_to_order_max": 5
            },
            "get_paged": {
                "count": 100,
                "attrs_in_filter_max": 4,
                "attrs_to_order_max": 3,
                "page_size": 10
            }
        },
        "results": {}
    }
    
* **domain**: configuration for stored data 
    * **attrs_total**: total number of all different attributes for the entity;
    * **attrs_per_instance**: average number of attributes per one instance of the entity;
    * **attr_types**: available types for the attributes; 
    * **instances_total**: total number of all instances of the entity;
* **operations**: configuration for typical operations;
    * **get_instance**: get one entity instance with all available attributes;
        * **count**: total number of the iterations;
    * **get_by_filter**: get all instances by filter;
        * **count**: total number of the iterations;
        * **attrs_in_filter_max**: max number of the attributes in filter;
    * **get_ordered**: get all instances ordered by some attributes;
        * **count**: total number of the iterations;
        * **attrs_to_order_max**: max number of the attributes to order; 
    * **get_paged**: get one page from filtered and ordered set of instances;
        * **count**: total number of the iterations;
        * **attrs_in_filter_max**: max number of the attributes in filter;
        * **attrs_to_order_max**: max number of the attributes to order;
        * **page_size**: count of the items on the page;
* **results**: configuration for results storing;