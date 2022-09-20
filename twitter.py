from datetime import date

from database import database_helper


def run_queries(current_date):
    daily_highest_query = f"""SELECT * 
                        FROM conveyances 
                        WHERE
                            sale_amount = (
                                SELECT
                                    MAX(sale_amount)
                                FROM
                                    conveyances
                                WHERE
                                    sale_date = '{current_date}')"""

    total_conveyances_query = f"""SELECT COUNT(conveyance_number)
                            FROM conveyances
                            WHERE
                                sale_date = '{current_date}'"""

    total_money_transfers_query = f"""SELECT COUNT(conveyance_number)
                            FROM conveyances
                            WHERE
                                sale_date = '{current_date}' AND sale_type <> ''"""

    sales_average_query = f"""SELECT AVG(sale_amount)
                        FROM conveyances
                        WHERE 
                            sale_date = '{current_date}' AND sale_type <> ''"""

    highest = database_helper.execute_query_return_results(daily_highest_query)
    total = database_helper.execute_query_return_results(total_conveyances_query)
    total_money_transfer = database_helper.execute_query_return_results(total_money_transfers_query)
    sales_average = database_helper.execute_query_return_results(sales_average_query)

    print(f"""Here are the stats for {current_date.strftime("%m/%d/%Y")}
💰Highest Sale: ${highest[0][2]:,.2f}
🏠Total Transfers: {total[0][0]}
💵Total Sales: {total_money_transfer[0][0]}
🧮️Average of Sales: ${sales_average[0][0]:,.2f}
#FranklinCountyOH #Ohio #RealEstate""")


if __name__ == "__main__":
    current_date = date(2022, 9, 19)
    run_queries(current_date)


