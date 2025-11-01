from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.contact import Contact

DATABASE_URL = "mongodb://localhost:27017"

async def init_db():
    """ 初始化数据库连接和 Beanie """
    print("正在连接到本地 MongoDB...")
    client = AsyncIOMotorClient(DATABASE_URL)

    # Beanie 会自动检测 'Contact' 模型的变更
    await init_beanie(database=client.contacts_db, document_models=[Contact])
    print("数据库连接成功。")