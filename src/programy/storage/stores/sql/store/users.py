"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.storage.stores.sql.store.sqlstore import SQLStore
from programy.storage.entities.user import UserStore
from programy.storage.stores.sql.dao.user import User

class SQLUserStore(SQLStore, UserStore):

    def __init__(self, storage_engine):
        SQLStore.__init__(self, storage_engine)

    def empty(self):
        self._storage_engine.session.query(User).delete()

    def add_user(self, userid, client):
        user = User(userid=userid, client=client)
        self._storage_engine.session.add(user)
        return user

    def get_user(self, userid):
        db_users = self._storage_engine.session.query(User).filter(User.userid == userid)
        users = []
        for user in db_users:
            users.append({"userid": user.userid, "client": user.client})
        return users[0]

    def get_client_users(self, clientid):
        db_users = self._storage_engine.session.query(User).filter(User.client == clientid)
        users = []
        for user in db_users:
            users.append({"userid": user.userid, "client": user.client})
        return users