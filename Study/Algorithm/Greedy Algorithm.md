## **❗️탐욕 알고리즘(Greedy Algorithm)이란?**

- **Greedy**는 **‘탐욕스러운, 욕심 많은’** 이란 뜻이다.
- **탐욕 알고리즘**은 말 그대로 **선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답에 도달**하는 방법이다.
- 탐욕 알고리즘은 최적해를 구하는 데에 사용되는 근사적인 방법이다.
- 탐욕 알고리즘은 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
- 순간마다 하는 선택은 그 순간에 대해 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적(전역적)인 해답을 만들었다고 해서, 그것이 최적이라는 보장은 없다.
- 하지만 탐욕 알고리즘을 적용할 수 있는 문제들은 지역적으로 최적이면서 전역적으로 최적인 문제들이다.

### **👉 탐욕 알고리즘 문제를 해결하는 방법**

1. 선택 절차(Selection Procedure): 현재 상태에서의 최적의 해답을 선택한다.
2. 적절성 검사(Feasibility Check): 선택된 해가 문제의 조건을 만족하는지 검사한다.
3. 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복한다.

### **👉 탐욕 알고리즘을 적용하려면 문제가 다음 2가지 조건을 성립하여야 한다.**

- 탐욕 알고리즘이 잘 작동하는 문제는 대부분 탐욕스런 선택 조건(greedy choice property)과 최적 부분 구조 조건(optimal substructure)이라는 두 가지 조건이 만족된다.
- 탐욕스런 선택 조건은 앞의 선택이 이후의 선택에 영향을 주지 않는다는 것이며, 최적 부분 구조 조건은 문제에 대한 최적해가 부분문제에 대해서도 역시 최적해라는 것이다.
1. 탐욕적 선택 속성(Greedy Choice Property) : 앞의 선택이 이후의 선택에 영향을 주지 않는다.
2. 최적 부분 구조(Optimal Substructure) : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성된다.
- 이러한 조건이 성립하지 않는 경우에는 탐욕 알고리즘은 최적해를 구하지 못한다.
- 하지만, 이러한 경우에도 탐욕 알고리즘은 근사 알고리즘으로 사용이 가능할 수 있으며, 대부분의 경우 계산 속도가 빠르기 때문에 실용적으로 사용할 수 있다.
- 이 경우 역시 어느 정도까지 최적해에 가까운 해를 구할 수 있는지를 보장하려면 엄밀한 증명이 필요하다.
- 어떤 특별한 구조가 있는 문제에 대해서는 탐욕 알고리즘이 언제나 최적해를 찾아낼 수 있다.
- 이 구조를 매트로이드라 한다.
- 매트로이드는 모든 문제에서 나타나는 것은 아니나, 여러 곳에서 발견되기 때문에 탐욕 알고리즘의 활용도를 높여 준다.

> #### **탐욕 알고리즘은 항상 최적의 결과를 도출하는 것은 아니지만, 어느 정도 최적에 근사한 값을 빠르게 도출할 수 있는 장점이 있다. 이 장점으로 인해 탐욕 알고리즘은 근사 알고리즘으로 사용할 수 있다.**

> #### **탐욕 알고리즘을 적용해도 언제나 최적해를 구할 수 있는 문제(매트로이드)가 있고, 이러한 문제에 탐욕 알고리즘을 사용해서 빠른 계산 속도로 답을 구할 수 있다. 그래서 실용적으로 사용할 수 있다.**

### **👉 근사 알고리즘(Approximation Algorithm)이란?**

- 근사 알고리즘(approximation algorithm)은 어떤 최적화 문제에 대한 해의 근사값을 구하는 알고리즘을 의미한다.
- 이 알고리즘은 가장 최적화되는 답을 구할 수는 없지만, 비교적 빠른 시간에 계산이 가능하며 어느 정도 보장된 근사해를 계산할 수 있다.