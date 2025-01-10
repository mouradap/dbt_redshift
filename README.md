This is a dbt introductory project. It was designed to quickstart the integration between local files and AWS Redshift via dbt.
I have used mock data with the faker library, that you must run separately in ./data/generate_mock_data.py.
The generated files you can add to the seeds folder, in ./ecommerce_dbt/seeds

### Using the starter project

Try running the following commands:
- dbt run
- dbt test
