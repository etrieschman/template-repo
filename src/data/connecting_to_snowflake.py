"""
This file provides examples on how to query/upload data from/to Snowflake
using the indigo.dsm-utils package that has already been included in the
requirements (pip install indigo.dsm-utils). You should explore what this
package has to offer and contirbute to it when you can:
https://github.com/indigo-ag/ds-toolkit-utils-module

Note: Your snowflake account information should be stored in a hidden `.env`
file that you can place at the root directory of your project folder.
Make sure to enter the following information:

# Snowflake login info:
SNOWFLAKE_USER=jdoe@indigoag.com #Indigo email address
SNOWFLAKE_PASS=abdcef #SF password
SNOWFLAKE_HOST=indigoproduction.us-east-1
SNOWFLAKE_DATABASE=SCRATCH  #Name of the database (for uploading data to SF)
SNOWFLAKE_SCHEMA=jdoe #Name of the schema in your database
"""

import pandas as pd

# This sql.py file has a lot of great utility functions, you should check it out!
from indigo.dsm_utils import sql

# Query some test data
QUERY = """
select *
from PARTHENON.CARBON.QUALIFIED_FIELD
limit 10
"""

# Get your authenticated Snowflake database connection
ENGINE = sql.connect_to_snowflake()

# Executes your query and saves the results in a pandas dataframe
df = pd.read_sql(QUERY, ENGINE)

# Good practice to have the columns in lower case
df.columns = df.columns.str.lower()

# Write the dataframe into your scratch space on Snowflake
sql.create_snowflake_table_from_df(
    df, ENGINE, "test_SCS", if_exists="replace", index=False
)
