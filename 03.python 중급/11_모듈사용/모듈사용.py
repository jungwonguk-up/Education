# as 키워드를 이용해서 모듈 이름을 단축 시킬 수 있다.

from audioop import add
import calculator as cal  # 왜 없다고 나오지? 같은 폴더에만 있어야 하나?

cal. add(10, 20)

# from ~ as 키워드를 이용해서 모듈의 특정 기능만 사용할 수 있다.

from calculator import add

add(10,20)


# from calculator import * 모든기능 다 가져온다는 뜻
# from calculator import add, mul , sub 3가지 기능 가져온다는 뜻