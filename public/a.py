class MyEnum(str, Enum):
    A = 'a',
    B = 'b',
    C = 'c'

enumT = TypeVar('enumT',bound=MyEnum)

class EnumContainer(GenericModel,Generic[enumT]):
    enum_value: enumT
    
containerT = TypeVar('containerT', bound=EnumContainer)

class OuterContainer(GenericModel,Generic[containerT]):
    container: containerT

class testEnumparsing(BaseModel):
    typer: OuterContainer[EnumContainer[MyEnum.B]]
    class Config:
        orm_mode = True

obj = testEnumparsing(
    typer= OuterContainer(
            container=EnumContainer(enum_value='a')
        )
)

parsed = testEnumparsing.from_orm(obj)
print(parsed)
