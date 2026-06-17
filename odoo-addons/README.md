# Livestock ERP (Odoo 17 CE 기반)

축산물(소/돼지/닭/수입우/수입돈) 유통·생산 ERP를 Odoo 17 Community Edition 위에 구축하는 커스텀 모듈 모음입니다.

## 라이선스/법적 메모
- 기반: Odoo 17 Community Edition (LGPL-3) — 자유 사용/수정 가능
- Enterprise 전용 모듈은 사용하지 않음
- 타사 ERP는 프로세스만 참고하여 직접 설계/구현 (코드 복제 없음)
- 축평원 공공데이터포털 API: 발급받은 키로 이용약관 준수하여 연동
- 미트와치 API: 별도 사업자 제휴/계약 필요 (법무 검토 별도 진행)

## 모듈 로드맵
| 단계 | 모듈 | 상태 |
|---|---|---|
| 1 | `livestock_base` (축종/등급/거래처 채널/품목 확장) | 완료 |
| 2 | `livestock_sale` (B2B/B2C/직영/가맹/외식 채널별 수주 → MRP 트리거) | 예정 |
| 3 | `livestock_mrp_integration` (수주 → 구매요청/작업지시 자동 연동) | 예정 |
| 4 | `livestock_logistics` (거래명세서 기준 배송준비/재고차감) | 예정 |
| 5 | `livestock_traceability` (축평원 이력번호 연동) | 예정 |
| 6 | `meatwatch_integration` (미트와치 API 연동) | 예정 |
| 7 | `livestock_account_fintech` (세금계산서 + 핀테크 회계 연동) | 예정 |

## livestock_base 모듈 구성 (제공받은 엑셀 분석 반영)
- `livestock.species`: 품종/축종 마스터 (한우/한돈/계육/수입우/수입돈)
- `livestock.cut`: 부위 마스터 (품종별 부위코드, 샘플 데이터 포함 — 전체 96건은 엑셀 일괄 업로드 권장)
- `livestock.grade`: 등급 마스터
- `livestock.product.account`: 품목계정등록 (01상품~10재공품, 회계계정 연동 필드 포함)
- `livestock.uom` / `livestock.uom.conversion`: 단위관리 / 환산단위관리 (부위별 단위 변환 규칙)
- `livestock.code.group` / `livestock.code`: 공통코드 마스터
  - 대/중/소분류, 성별, 친환경구분, 보관, 용도, 축산물유형, 박스종류
  - 유통구조, 거래처분류값, 거래처종류, 매출처유형(신고용)
- `res.partner`: 거래처 등록 양식 전체 필드 반영 (사업자번호, 신용등급, 법인/개인, 전자세금계산서 구분, 목장/도축장/가공장 여부, 미트와치교부번호, 계좌정보 등)
- `product.template`: 품목 등록 양식 전체 필드 반영 (품목계정, 대중소분류, 축산물 분류, 부가세, 생산유형, 포장/유통/이력 정보 등)

### 신규등록 화면 (전체화면 + 권한 제한)
- "거래처 신규등록" / "품목 신규등록" 메뉴는 `group_livestock_registrar` 권한 그룹에만 보입니다.
- 일반 사용자는 기존 거래처/품목 목록에서 조회·수정만 가능합니다.
- 권한 부여: 설정 → 사용자 → 해당 직원에게 "축산물ERP - 거래처/품목 신규등록 권한자" 그룹 추가.

### 남은 작업 (대량 데이터 일괄 등록)
- 품목소분류(263건), 부위코드(96건), 환산단위(220건) 등은 샘플만 입력해두었습니다.
- 추후 "엑셀 업로드" 기능(가져오기/내보내기)을 통해 전체 데이터를 일괄 등록하는 단계가 필요합니다.

## 설치 방법 (로컬 Docker 환경)
`odoo-docker-compose.yml`의 `./addons` 볼륨 경로를 이 `odoo-addons` 폴더로 매핑한 뒤,
Odoo 실행 시 `--addons-path`에 포함하거나 Apps 메뉴에서 업데이트 후 설치하세요.
