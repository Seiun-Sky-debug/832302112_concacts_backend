from pydantic import BaseModel, Field
from beanie import Document, PydanticObjectId
from typing import Optional, List

class Contact(Document):
    """ 代表数据库中“联系人”的模型。 """
    name: str = Field(..., max_length=50)
    phone: str = Field(..., max_length=20)
    group: Optional[str] = Field(None, max_length=50)
    is_pinned: bool = Field(default=False)

class CreateContactModel(BaseModel):
    """ 用于“创建”联系人的输入模型。 'name' 和 'phone' 是必需的。 'group' 和 'is_pinned' 是可选的 """
    name: str = Field(..., max_length=50)
    phone: str = Field(..., max_length=20)
    group: Optional[str] = Field(None, max_length=50)
    is_pinned: bool = Field(default=False) # 给予默认值

class Settings:
    # MongoDB 中的 collection (表) 名称
    name = "contacts"

class UpdateContactModel(BaseModel):
    """ 用于“更新”操作的模型，所有字段都是可选的。 (我们使用 'Optional[str] = None' 来确保它们都不是必需的) """
    name: Optional[str] = None
    phone: Optional[str] = None
    group: Optional[str] = None
    is_pinned: Optional[bool] = None

class PinContactModel(BaseModel):
    """ 专门用于置顶/取消置顶的模型 """
    is_pinned: bool

