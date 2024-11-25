"""
    Schema to table jobs.csv file.
"""
schema_jobs = StructType([
    StructField("id", IntegerType(), True),
    StructField("job", StringType(), True)
])

"""
    Schema to table departments.csv file.
"""
schema_departments = StructType([
    StructField("Puesto", StringType(), True),
    StructField("Empresa", StringType(), True),
    StructField("Ubicación", StringType(), True),
    StructField("Modalidad", StringType(), True),
    StructField("Antigüedad", StringType(), True)
])

"""
    Schema to table hired_employess.csv file.
"""
schema_hired_employess = StructType([
    StructField("Puesto", StringType(), True),
    StructField("Empresa", StringType(), True),
    StructField("Ubicación", StringType(), True),
    StructField("Modalidad", StringType(), True),
    StructField("Antigüedad", StringType(), True)
])

"""
    Dictionary schemas
"""
schemas = {
    "jobs": schema_jobs,
    "departments": schema_departments,
    "hired_employess": schema_hired_employess
}
