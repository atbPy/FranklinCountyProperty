from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, Float, Boolean

db_engine = None

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
                    Column('owner_address_2', String),
                    Column('LUC', String),
                    Column('site_address', String)
                    )

conveyance_parcels = Table('conveyance_parcels', metadata,
                           Column('conveyance_parcel', String, primary_key=True),
                           Column('conveyance_number_id', String, ForeignKey('conveyances.conveyance_number')),
                           Column('parcel_number', String)
                           )

conveyance_dates = Table('conveyance_dates', metadata,
                         Column('conveyance_date', String, primary_key=True),
                         Column('processed', Boolean),
                         Column('processed_date', Date),
                         Column('records_processed', Integer)
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

    print(query)
    with db_engine.connect() as connection:
        try:
            connection.execute(query)
        except Exception as e:
            print(e)


def execute_select_query(query=''):
    if query == '': return

    print(query)
    with db_engine.connect() as connection:
        try:
            result = connection.execute(query)
        except Exception as e:
            print(e)
        else:
            result.close()
            return result


def print_all_data(table=''):
    query = "SELECT * FROM '{}';".format(table)
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
    if table == "conveyance":
        stmt = conveyances.insert().values(data_dict)
    elif table == "conveyance_parcels":
        stmt = conveyance_parcels.insert().values(data_dict)
    elif table == "conveyance_dates":
        stmt = conveyance_dates.insert().values(data_dict)
    else:
        return

    execute_query(stmt)

def update_record(table, data_dict):
    # Update Data
    if table == "conveyance":
        stmt = conveyances.update().values(data_dict)
    elif table == "conveyance_parcels":
        stmt = conveyance_parcels.update().values(data_dict)
    elif table == "conveyance_dates":
        stmt = conveyance_dates.update().values(data_dict)
    else:
        return

    execute_query(stmt)

