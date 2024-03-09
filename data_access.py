from datetime import datetime
import sqlalchemy
import tkinter as tk
from tkinter import filedialog

def get_database_path():
    root = tk.Tk()
    root.withdraw() #Hide the main Tkinter window
        # Open a dialog to choose the database file path
    file_path = filedialog.asksaveasfilename(
        defaultextension='.db',
        filetypes=[('SQLite Database Files', '*.db')],
        title="Select Database File"
    )

    root.destroy()  # Close the Tkinter window

    return file_path


def database():
    db_path = get_database_path()
    if db_path:       
        db = sqlalchemy.create_engine(f'sqlite:///{db_path}')
        return db
    else:
        return None

def save_to_db(df, db, append: bool = True):
    if db is None:
        print("Database engine not provided.")
        return
    
    create_date = datetime.now()
    df['create_date'] = create_date
    if not append:
            with db.connect() as conn:
                conn.execute(f"DROP TABLE IF EXISTS simulation_results")

        # Add an index column to serve as the primary key
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)

    rows, columns = df.shape
    appending = 'append' if append else 'replace'
    print(f'loading df to db, {rows} row(s)')
    df.to_sql('simulation_results', db, index=False, if_exists=appending)
    print('data loaded successfully!')

        # Add a primary key constraint to the 'id' column if creating a new table
    if not append:
        with db.connect() as conn:
            conn.execute(f"ALTER TABLE simulation_results ADD PRIMARY KEY (id)")
