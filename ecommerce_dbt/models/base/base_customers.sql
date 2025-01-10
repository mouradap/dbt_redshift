{{ config(materialized='view') }}

select
    customer_id,
    customer_name,
    email,
    phone,
    address,
    cast(signup_date as date) as signup_date
from {{ source('public', 'customers') }}
