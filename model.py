import psycopg2


class Schema:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=items, user=postgres, password=qmkj9c7m53sj0233, host=app-4e678ec6-e0ff-4f72-8b83-73ede6496c9d-do-user-8299413-0.b.db.ondigitalocean.com, port=25060 ")

        self.create_user_table()
        self.create_to_do_table()
     

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)
    def create_user_table(self):
        # create user table in similar fashion
        # come on give it a try it's okay if you make mistakes
        pass
