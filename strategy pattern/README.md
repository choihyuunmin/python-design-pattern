# strategy pattern
전략 패턴은 알고리즘의 패밀리를 정의, 각 패밀리들을 별도의 클래스에 넣고 서로 상호작용하도록 정의.
동물 인형을 만드는데, 해당 인형의 기능(소리가 난다, 날개가 달렸다, 바퀴가 달렸다 등)이 하나씩 늘어날 때마다 클래스에서
수정하고 구현해야 하는 기능들이 많아서 무거워지게됨. 해당 기능을 따로 분리시켜주어 수정이나 추가해 용이하도록 한다.