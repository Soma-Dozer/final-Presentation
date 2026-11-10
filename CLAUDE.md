# CLAUDE.md: DevFit 최종발표 덱 (팀 Dozer · AI·SW 마에스트로 17기 최종평가)

팀원과 팀원의 Claude가 이 덱을 고칠 때 읽는 가이드. **세부 규칙의 정본은 `final-deck/BUILD.md`다.** 이 파일과 어긋나면 BUILD.md를 따른다.

## 1. 바로 시작

```bash
# 1회 설치 (macOS)
brew install poppler            # pdftoppm, pdfinfo
npm i -g pptxgenjs              # PPTX 생성
# Google Chrome 필요 (다른 위치면 CHROME=/경로 환경변수)

# 미리보기: HTML만 (1초)
python3 final-deck/gen.py && open final-deck/index.html

# 전체 빌드: HTML → PDF → PPTX(+발표자 노트)
zsh final-deck/build/build.sh <내이름>
```

산출물: `final-deck/index.html`(발표용, 브라우저에서 방향키) · `11-최종발표-완성본.pdf` · `11-최종발표-완성본.pptx`

빌드가 `slides 66 · … · 노트 없는 장: 없음`으로 끝나면 정상이다.

## 2. 어디를 고치나

장표는 파이썬 파일 안의 HTML 문자열이다. 장표 하나 = `S.add(...)` 한 번 + 바로 다음 줄 `S.note('''발표자 노트''')`.

| 파일 | 내용 | 담당 |
|---|---|---|
| `final-deck/s1_intro.py` | 표지 · Problem · Solution · Key Features · Live Demo | 전반부 |
| `final-deck/s2_dev.py` | Development (수행과정·기술) | Dev |
| `final-deck/s3_effect.py` | Effect (성과·사업) | Effect |
| `final-deck/s4_closing.py` | 마무리 · 감사합니다 · 부록 목차 | 전반부 |
| `final-deck/s5_appendix.py` | 부록 A1~A14 | 전반부 |
| `final-deck/core.py` · `gen.py` | 공용 CSS·헬퍼 · 조립기 | 🔒 관리자만 |
| `final-deck/assets/` | 장표 이미지·로고 | |
| `final-deck/vendor/irdeck_new.html` | 중간평가 덱 사본 (공용 CSS·JS 원본, 고치지 말 것) | |

- **자기 담당 파일만 고친다.** 다른 파일이나 `core.py`·`gen.py`를 바꿔야 하면 담당자에게 요청.
- 새 CSS는 자기 파일의 `CSS = r"""…"""`에, 접두사(`in-` / `dv-` / `ef-`)를 붙여서.
- 장 순서는 파일 안 순서 그대로. 부록은 eyebrow `Appendix · A<n>` 번호순 자동 정렬.
- 다른 장을 «p32»처럼 쪽번호로 가리키면 장 수가 바뀔 때 틀어진다. 부록 쪽번호는 `{{PAGE:A<n>}}`를 쓴다.
- `final-deck/_legacy/`는 예전 버전 보관용. 빌드에 안 쓴다.

## 3. 반드시 지킬 것

1. **조작 금지.** 불리한 수치는 바꾸지 말고 장표에서 빼고 Q&A 노트로 옮긴다.
2. **수치 정본은 `collect/00-통합보고.md`**, 주장은 `claims.md`(C번호)와 최종보고서(`3-20. Dozer. 최종보고서.pdf`, 이 저장소 밖에 있는 확정본이라 수정하지 않음). 근거 없는 주장에 숫자를 붙이지 않는다.
3. **금지 주장:** «점수·랭킹 없음»(→ «합불 판정·랭킹 없음») · «유일/최초» · «특허 등록»(출원 단계) · «상표 등록»(출원공고 결정 단계) · «검증된/검수된 기출» · «RAG» · «매출» · «60% 절감» · «고객 확보»·«파일럿 진행 중»·«LOI» · «커밋 선별 LLM 0회» · «12% → 78%». 전체 목록과 이유는 BUILD.md «금지 주장».
4. **B2C/B2B 상태:** B2C는 운영 중이고 사용자가 있다. B2B는 개발 완료, 기업에 서비스 소개서를 보내는 단계다. B2B를 «운영 중»이라고 쓰지 않는다.
5. **진행 중 표현 금지.** 최종발표라 «~진행 중»·«심사 중»·«검수 중» 같은 미완료 상태를 장표에 쓰지 않는다.
6. **피드백 반영 기간(당일·N일 만에) 강조는 Dev 수행과정 요약 장에서만.**

## 4. 문구 스타일

- 사람이 쓴 보고서 문체. `.claude/skills/humanizer/SKILL.md` 기준 (Claude Code에서 `/humanizer`).
  - 제목·라벨에 «A — B» 대시 금지 → 콜론이나 괄호
  - «X가 아니라 Y» 대비 금지
  - 은유·경구 라벨 금지: 뒷면·갈래·막힌 길·정본·진단·처방·왜 → 변경 사유·원인·기준
  - 수사 의문문 라벨 금지
- Dev·Effect·부록은 명사형 종결. 전반부(표지~Live Demo)는 합쇼체 허용, 짧은 라벨만 명사형.
- « » 강조 금지. 실제 인용만 " ".
- 알약(pill)형 칩·배지 금지. 라벨이 꼭 필요하면 6px 사각 태그.
- 흐름도는 한 줄·ㄹ자·ㄷ자 금지. 구역·갈래·되돌림이 보이는 2D 다이어그램, 실제 쓰는 도구 로고만.
- 장표 하나에 핵심 메시지 하나. 표·긴 설명은 노트나 부록으로.
- 인물: 소마 멘토는 실명 OK. 외부인은 역할로만(예외는 BUILD.md «인물 표기»).
- 각주: `출처, 「자료명」, 연도.`

## 5. 개인정보 · 공유

- 이 저장소에는 **마스킹하지 않은 개인정보**(사업자등록증·특허/상표 통지서·실명이 담긴 캡처 등)가 있다. **private 저장소로만 유지**하고, 덱을 웹(GitHub Pages·Artifact·공개 링크)에 올리지 않는다. 발표는 로컬 `index.html` 또는 PDF/PPTX로.
- `.env`·토큰·API 키를 커밋하지 않는다.
- 커밋 메시지에 AI 도구 흔적(Co-Authored-By 등)을 넣지 않는다.

## 6. 폴더 지도

| 경로 | 내용 |
|---|---|
| `final-deck/` | 덱 소스와 빌드 (여기서 작업) |
| `collect/` | 수치 근거 보고서 A~K, `00-통합보고.md`(정본·Q&A 원고), `data/`(CSV), `exp-compare/`(범용 AI 비교 실험) |
| `research/` | 외부 근거 조사. `00-주장-근거-URL.md`가 입구 |
| `kpi/` · `metrics/` | KPI 이미지 원본 · 지표 수집 스크립트와 차트 |
| `claims.md` | 사용자가 정한 주장 목록(C번호)과 근거 상태 |
| `00`~`10-*.md` 등 | 평가 안내·초기 구성안·와이어프레임 (참고용, 현행 아님) |

`collect/exp-compare/work/`의 외부 레포 clone과 BE 소스 사본은 용량·보안 때문에 저장소에서 뺐다(`.gitignore`).
