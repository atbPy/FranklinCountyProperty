from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, Float, Boolean
from sqlalchemy import select
from sqlalchemy import text

metadata = MetaData()

# Define the tables
conveyances = Table('conveyances', metadata,
                    Column('conveyance_number', String, primary_key=True),
                    Column('sale_date', Date),
                    Column('sale_amount', Float),
                    Column('sale_type', String),
                    Column('parcel_count', Integer),
                    Column('exempt', String),
                    Column('owner_name_1', String),
                    Column('owner_name_2', String),
                    Column('owner_address_1', String),
                    Column('owner_address_2', String)
                    )

conveyance_parcels = Table('conveyance_parcels', metadata,
                           Column('conveyance_parcel', String, primary_key=True),
                           Column('conveyance_number_id', String, ForeignKey('conveyances.conveyance_number')),
                           Column('parcel_number', String),
                           Column('conveyance_date', Date),
                           Column('LUC', String, ForeignKey('land_use_codes.land_use_code')),
                           Column('site_address', String)
                           )

conveyance_dates = Table('conveyance_dates', metadata,
                         Column('conveyance_date', String, primary_key=True),
                         Column('processed', Boolean),
                         Column('processed_date', Date),
                         Column('records_processed', Integer)
                         )

land_use_codes = Table('land_use_codes', metadata,
                       Column('land_use_code', String, primary_key=True),
                       Column('description', String),
                       Column('active', Boolean)
                       )

db_engine = create_engine('sqlite:///franklinCountyConveyances.sqlite', echo=True)
print(db_engine)


def create_db_tables():
    try:
        metadata.create_all(db_engine)
        print("Tables created")
    except Exception as e:
        print("Error occurred during Table creation!")
        print(e)


# Insert, Update, Delete
def execute_query(query=''):
    if query == '': return

    #print(query)
    with db_engine.connect() as connection:
        try:
            connection.execute(query)
        except Exception as e:
            print(e)


def execute_select_query(table, field, value):
    # query = select(conveyance_dates).where(conveyance_dates.c.conveyance_date == '2022-08-15')
    query = f"SELECT * FROM {table} WHERE {table}.{field} = '{value}'"

    with db_engine.connect() as connection:
        try:
            result = connection.execute(query)
        except Exception as e:
            print(e)
        else:
            results_length = len(result.all())
            result.close()
            return results_length


def print_all_data(table):
    query = f"SELECT * FROM {table};"
    print(query)

    with db_engine.connect() as connection:
        try:
            result = connection.execute(query)
        except Exception as e:
            print(e)
        else:
            for row in result:
                print(row)
            result.close()


def insert_record(table, data_dict):
    # Insert Data
    if table == "conveyances":
        stmt = conveyances.insert().values(data_dict)
    elif table == "conveyance_parcels":
        stmt = conveyance_parcels.insert().values(data_dict)
    elif table == "conveyance_dates":
        stmt = conveyance_dates.insert().values(data_dict)
    elif table == "land_use_codes":
        stmt = land_use_codes.insert().values(data_dict)
    else:
        print("The insert query has not been defined")
        return

    execute_query(stmt)


def update_record(table, where_clause, data_dict):
    # Update Data
    if table == "conveyances":
        stmt = conveyances.update().where(text(where_clause)).values(data_dict)
    elif table == "conveyance_parcels":
        stmt = conveyance_parcels.update().where(text(where_clause)).values(data_dict)
    elif table == "conveyance_dates":
        stmt = conveyance_dates.update().where(text(where_clause)).values(data_dict)
    else:
        return

    execute_query(stmt)

