import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute('SELECT * FROM users WHERE age > 40')
        results = cursor.fetchall()
        return results

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print('All users:', users)
    print('Users older that 40:', older_users)

asyncio.run(fetch_concurrently())