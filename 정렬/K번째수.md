### K번째수

commands의 각 조건 i,j,k에 맞게 슬라이싱 -> 정렬 -> 인덱싱을 통해 해당 값을 answer에 append 한다.

-java

- code
  ``` java
  import java.util.Arrays;

  class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length]; // command수만큼 길이 지정
        
        for (int i = 0; i < commands.length; i++) {
            int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }
        
        return answer;
    }
  }
  
  // 1. 범위 별 자른 배열을 저장
  // 2. 자른 배열을 정렬
  // 3. 배열의 해당 인덱스 값을 answer에 저장
  ```
- 풀이
  ```
  각 command 배열에 대해서 주어진 array를 자른다.
  자른 배열을 정렬
  정렬된 배열에서 해당하는 인덱스의 값을 answer에 추가
  ```
