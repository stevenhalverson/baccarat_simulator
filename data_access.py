from datetime import datetime
import sqlalchemy


db = sqlalchemy.create_engine('sqlite:///baccarat_simulation.db')

def save_to_db(df, append: bool = True):
    create_date = datetime.now()
    df['create_date'] = create_date
        # using shape to get column and row counts
    rows, columns = df.shape
    appending = 'append' if append else 'replace'
    print(f'loading df to db, {rows} row(s)')
    df.to_sql('simulation_results', db, index=False, if_exists=appending)
    print('data loaded successfully!')
