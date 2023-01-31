# Reporter - a reporting tool for Data Science Project

This notebook is part of a set of standardize data science tools I am creating. This intend to automate a data science projects and the reporting of it.
It handles multiples notebook execution, parametrization and exporting. 

This code can be easily adapted to match the needs of a data science project. Querying data, Raising error, configure how notebooks are merged, etc.

**Note** : due to limitation to get notebook's directory, notebook executed by Reporter will work from current working directory of reporter.ipynb. This can pose problem when your notebooks input or output data.

This can be overcome in several ways : 
- use hardcoded path : it gives you the freedom of your project's structure (not recommended)
- give path as parameter of your notebooks (used in this example)
- use relative path and set Reporter at the same level in the tree structure as the notebooks you are executing (temp folder can be located anywhere)) :

***Project folder***

    - Prediction model

        - model.ipynb

    - Dashboard

        - dashboard.ipynb

    - Reporter

        - reporter.ipynb 
