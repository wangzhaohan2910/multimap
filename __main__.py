# Prototype
class multimap(defaultdict[str, set[str]]):
    def __init__(self, *args, **kwargs) -> None
    def __str__(self) -> str
    def __repr__(self) -> str
    def __bool__(self) -> bool
    def __nonzero__(self) -> bool
    def __enter__(self) -> 'multimap'
    def __exit__(self, *args, **kwargs) -> bool
    def __copy__(self) -> 'multimap'
    def __deepcopy__(self, memo: dict) -> 'multimap'
    def __len__(self) -> int
    def __getitem__(self, key: str) -> set[str]
    def __setitem__(self, key: str, value: Union[str, set[str]]) -> None
    def __contains__(self, item: tuple[str]) -> Optional[bool]
    def remove_key(self, key: str)
    def remove_value(self, value: str)
    def remove_item(self, key: str, value: str)
    def change_key(self, old: str, new: str)
    def change_value(self, old: str, new: str)
    def change_item(self, key: str, old: str, new: str)
    def move_value(self, value: str, old: str, new: str)
    def keys(self) -> Iterator[str]
    def values(self) -> Iterator[str]
    def items(self) -> Iterator[tuple[str]]
    def asdict(self) -> dict[str, set[str]]
    def clear(self) -> None
    def update(self, other: 'multimap') -> None
