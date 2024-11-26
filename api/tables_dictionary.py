from pyspark.sql.types import *

"""
    Schema to table jobs.csv file.
"""
schema_jobs = StructType([
    StructField("id", IntegerType(), False),
    StructField("job", StringType(), True)
])

"""
    Schema to table departments.csv file.
"""
schema_departments = StructType([
    StructField("id", IntegerType(), False),
    StructField("department", StringType(), True)
])

"""
    Schema to table hired_employees.csv file.
"""
schema_hired_employees = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("datetime", StringType(), True),
    StructField("department_id", IntegerType(), True),
    StructField("job_id", IntegerType(), True)
])

"""
    Dictionary schemas
"""
schemas = {
    "jobs": schema_jobs,
    "departments": schema_departments,
    "hired_employees": schema_hired_employees
}
