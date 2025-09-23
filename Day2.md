# Git 공부함
1. git 의 영역
    * Working directory
    * Staging Area
    * Repository (Local)

2. W.D => S.A
  * `git add <파일명>`

3. S.A => Repo
  * `git commit -m "커밋메세지"`

4. 커밋메세지 수정하기
  * `git commit --amend`
    - 커밋 메세지도 수정할 수 있지만
    - 커밋 자체를 수정하는게 목적
    - 사용을 할 때는 주의 해야 함
      - 팀플이라면 충분한 커뮤니케이션이 필요
      - S.A 에 있는 파일도 커밋이 수정되면서 같이 Repo에 올라가기 때문에
        S.A체크가 필요함

5. 현재 어느 영역에 어느 파일이 위치하는지 확인
  *`git status`
    * Red colo : W.D
    * Green color : S.A

6. remote Repo
  * `github`, `gitlab`

7. Local => Remote
  * `git push 별칭 master`
    * 올리기 전에 반드시 remote 등록을 해야 함
      * `git remote add 별칭 주소`

8. Remote => Local
  * `git pull 별칭 master(브랜치명)`
  * git 환경이 준비되지 않은 zero에서는 
    * `git clone 리모트레포주소`


